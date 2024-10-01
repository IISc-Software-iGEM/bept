import os
from rich.console import Console
from beaupy import select_multiple
import shutil

CONSOLE = Console()
TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "pymol_templates")


def template_copy(template_name: str, output_dir: str):
    """
    Copy the template to the output directory.
    Args:
        template_name: The name of the template file.
        output_dir: The output directory where the template file will be copied.
    """
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    output_path = os.path.join(output_dir, template_name)

    try:
        shutil.copy(template_path, output_path)
        CONSOLE.print(f"Template {template_name} copied to {output_dir}")
    except Exception as e:
        CONSOLE.print(
            f"Error copying template {template_name} to {output_dir}. Error: {e}",
            style="red",
        )

    return


def pymol_main(output_dir: str):
    """
    Template codes for various PyMOL operations are provided here.
    User has to modify the codes as per the requirement.
    Args:
        output_dir: The output directory where the template files will be copied.
    """
    # List of pymol template codes
    pymol_code_opts = {
        "Morphing two proteins": "morphing_two_proteins.py",
        "Aligning two proteins": "aligning_two_proteins.py",
        "Superimposing two proteins": "superimpose_two_proteins.py",
        "Mutagenisis": "point_mutagenesis.py",
        "Bulk Mutagenisis": "bulk_mutagenesis.py",
        "Selecting residues in a radius around atom": "radius_selection.py",
        "Show bumps": "show_bumps.py",
        "Cartoon representation of protein": "cartoon_representation.py",
        "Create and Color a surface": "create_color_surface.py",
        "Distance between two atoms": "dist_bw_atoms.py",
        "Calculate SASA": "calc_sasa.py",
    }

    # Select the codes to be copied
    CONSOLE.print("Select the PyMOL template codes to be copied:")
    codes_selected = select_multiple(
        list(pymol_code_opts.keys()),
        tick_character="*",
        ticked_indices=[0],
        maximal_count=len(pymol_code_opts),
    )
    if not codes_selected:
        CONSOLE.print("No code template selected.", style="yellow")
        return

    for opt in codes_selected:
        code = pymol_code_opts[opt]
        template_copy(code, output_dir)

    return
