import os
import shutil

import rich_click as click
from beaupy import confirm, select_multiple
from rich.console import Console
from trogon import tui

from bept.analysis.bept_csv_make import bept_make, csv_make
from bept.analysis.opt_files.cube import cube_make
from bept.analysis.opt_files.surface_pdb_sasa import calc_sasa, get_surface_resi
from bept.analysis.opt_files.xyz import xyz_make
from bept.auto.auto_execute import apbs_exec, p_exec
from bept.auto.auto_file import file_runner
from bept.docs.docs_viewer import run_docs_viewer
from bept.gen.app_runner import apbs_gen, pdb2pqr_gen
from bept.gen.pdb2pqr_beaupy import inter_pqr_gen_beaupy
from bept.gen.toml_in_converter import in_toml, toml_in
from bept.history.cache_apbs import CACHE_DIR as APBS_CACHE_DIR
from bept.history.cache_apbs import clear_apbs_cache as apbs_cache_clear
from bept.history.cache_vnr import cache_view, restore_selected_cache
from bept.history.his_main import history_choose, history_clear
from bept.pymol.mol_ext import pymol_main
from bept.validator import (
    validate_apbs,
    validate_dx,
    validate_into,
    validate_pdb2pqr,
    validate_pqr,
    validate_toin,
)

CONSOLE = Console()

__package__ = "bept"
__version__ = "0.1.0"


BEPT_AUTH_MSG = """
-----------------------------------
Thank you for using BEPT - Beginner friendly Electrostatics for Protein analysis Tool.
This is developed by IISc-Software Team for iGEM 2024, from Indian Institute of Science, Bangalore.

To see documentation, run `bept docs`.
For more information, visit the official github page at https://github.com/IISc-Software-iGEM/bept.
-----------------------------------
"""

print(BEPT_AUTH_MSG)


@tui(command="ui", help="Make bept commands with a user interface.")
@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(
    f"{__package__} v{__version__}", "--version", "-v", message="%(version)s"
)
def main():
    """
    BEPT is a Beginner friendly Electrostatics for Protein analysis Tool. Bept gives you an interactive, colorful, easy-to-use interface to automate your protein analysis with PDB2PQR commands and APBS.
    This was built as part of the project IMPROVISeD, by IISc-Software-iGEM Team 2024.

    To know more information about each option, run `bept COMMAND --help`. To generate BEPT command interactively, run `bept ui`. To see the documentation of BEPT, run `bept docs`.
    """
    pass


@main.command(short_help="Automate calculation of pdb2pqr and APBS.")
@click.option(
    "--pdb2pqr",
    "-p",
    type=click.Path(exists=True),
    callback=validate_pdb2pqr,
    help="Run one pdb2pqr command. Input single PDB file path.",
)
@click.option(
    "--apbs",
    "-a",
    type=click.Path(exists=True),
    callback=validate_apbs,
    help="Run one apbs command. Input single APBS input file path.",
)
@click.option(
    "--file-load",
    "-f",
    type=click.Path(exists=True),
    help="Load list of protein or input files to automate.",
)
@click.option(
    "--interactive",
    "-i",
    is_flag=True,
    help="Run the loaded file commands interactively.",
)
def auto(pdb2pqr, apbs, file_load, interactive):
    """
    Automate pdb2pqr, apbs commands for multiple proteins. You can run all at once or interactively with -i flag.
    Note: To halt auto file execution, add a ` :?` inside your command to run that command interactively.
    Run `bept auto --help` for more information.
    """
    if file_load:
        file_runner(file_load, interactive)
        return

    # Command processing based on provided arguments or history
    if apbs:
        input_file = apbs
        apbs_cmd = f"apbs {input_file}"
        apbs_exec(apbs_cmd, interactive)
        return

    if pdb2pqr:
        pdb_file = pdb2pqr
        pdb2pqr_cmd = f"pdb2pqr --ff=AMBER --apbs-input={pdb_file[:-4]}.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 {pdb_file} {pdb_file[:-4]}.pqr"
        p_exec(pdb2pqr_cmd, interactive)
        return


@main.command(short_help="Generate pdb2pqr, apbs commands interactively")
@click.option(
    "--pdb2pqr",
    "-p",
    callback=validate_pdb2pqr,
    help="Generate pdb2pqr command interactively. Input PDB ID or PDB file path.",
)
@click.option(
    "--no-tui",
    "-nu",
    is_flag=True,
    help="Generate pdb2pqr command without UI i.e. inside main terminal. Default: False, a UI to generate command will be shown.",
)
@click.option(
    "--apbs",
    "-a",
    type=click.Path(exists=True),
    callback=validate_apbs,
    help="Generate apbs command interactively. Input `.in` file path.",
)
@click.option(
    "--in-to-toml",
    "-into",
    type=click.Path(exists=True),
    callback=validate_into,
    help="Convert .in file to .toml file.",
)
@click.option(
    "--toml-to-in",
    "-toin",
    type=click.Path(exists=True),
    callback=validate_toin,
    help="Convert .toml file to .in file.",
)
def gen(pdb2pqr, no_tui, apbs, in_to_toml, toml_to_in):
    """
    Generate pdb2pqr commands and APBS input file interactively.
    Bept allows conversion between `.in` & `.toml`.
    """
    # PDB2PQR command generation
    if pdb2pqr:
        if no_tui:
            pdb2pqr_cmd = inter_pqr_gen_beaupy(pdb2pqr)
        else:
            pdb2pqr_cmd = pdb2pqr_gen(pdb2pqr)

        if pdb2pqr_cmd:
            p_exec(pdb2pqr_cmd)
        return

    # APBS command generation and options
    if apbs:
        in_path_toml, out_path_toml = apbs_gen(apbs)
        if in_path_toml and out_path_toml:
            CONSOLE.print(
                "Successfully generated APBS input files along with respective toml files.",
                style="green",
            )
        # Create .bept directory if it doesn't exist
        bept_dir = os.path.join(os.path.dirname(out_path_toml), ".bept")
        os.makedirs(bept_dir, exist_ok=True)

        # Define new paths
        bept_in_path_toml = os.path.join(bept_dir, os.path.basename(in_path_toml))
        bept_out_path_toml = os.path.join(bept_dir, os.path.basename(out_path_toml))

    # Move files to .bept directory
    try:
        shutil.move(in_path_toml, bept_in_path_toml)
        shutil.move(out_path_toml, bept_out_path_toml)
        CONSOLE.print("Moved the toml files to the .bept directory.", style="yellow")
    except Exception as e:
        CONSOLE.print(
            f"Error in moving the toml files to the .bept directory. Error: {e}",
            style="red",
        )

    # Exclusively convert in to toml
    if in_to_toml:
        try:
            in_toml(in_to_toml)
            CONSOLE.print(
                "Successfully converted .in file to .toml file.", style="green"
            )
        except Exception as e:
            CONSOLE.print(
                f"Error in converting .in file to .toml file. Error: {e}", style="red"
            )
        return

    # Exclusively convert toml to in
    if toml_to_in:
        try:
            toml_in(toml_to_in)
            CONSOLE.print(
                "Successfully converted .toml file to .in file.", style="green"
            )
        except Exception as e:
            CONSOLE.print(
                f"Error in converting .toml file to .in file. Error: {e}", style="red"
            )
        return

    return 1


@main.command(short_help="Output File generation for potential output files")
@click.option(
    "--dx",
    "-d",
    type=click.Path(exists=True),
    required=True,
    callback=validate_dx,
    help="Input APBS pot_dx file path.",
)
@click.option(
    "--pqr",
    "-q",
    type=click.Path(exists=True),
    required=True,
    callback=validate_pqr,
    help="Input PQR file path.",
)
@click.option(
    "--pdb",
    "-p",
    type=click.Path(exists=True),
    callback=validate_pdb2pqr,
    help="Input PDB file path. Recommended for generating surface residues and calculating SASA.",
)
@click.option(
    "--interactive",
    "-i",
    is_flag=True,
    help="Interactively select which files to generate. Default: only .bept",
)
@click.option(
    "--all-types",
    "-all",
    is_flag=True,
    help="Generate all other supported output files.",
)
@click.option(
    "--out-dir",
    "-o",
    type=click.Path(),
    help="Output directory to save the files. Default: current directory.",
)
def out(interactive, dx, pqr, pdb, all_types, out_dir):
    """
    Generate output files including PQR, Potential DX and default `.bept` and `<protein>_bept.csv` file.
    Run `bept gen --help` for more information.
    """
    # Check if the input files are provided
    input_dx, input_pqr = dx, pqr
    # set output directory
    output_dir = out_dir if out_dir else os.getcwd()

    file_options = [
        "cube: Gaussian .cube file",
        "xyz: .xyz format for input protein",
        "Surface Residues with Potential",
        "Calculate and print SASA value for protein",
        "Cancel and generate default",  # Always last option
    ]
    types = ["bept: .bept file containing all data"]

    if interactive and not all_types:
        CONSOLE.print(
            "A csv containing all data will be generated. Choose among the following types of files you would also like to choose.",
            style="bold blue",
        )
        types += select_multiple(file_options)
    else:
        # Nothing apart from default
        types = []

    if all_types:
        types += file_options[:-1]

    if file_options[-1] in types and len(types) > 3 and not all_types:
        CONSOLE.print(
            "Warning! You selected Cancel along with other options. Only default files will be generated.",
            style="bold yellow",
        )

    bept_csv, err_csv = csv_make(input_pqr, input_dx, output_dir)
    bept_main_path, err_bept = bept_make(input_pqr, input_dx, bept_csv, output_dir)

    if not pdb and (file_options[2] in types or file_options[3] in types):
        protein_path = input(
            "For calculating the surface residues and SASA, we need the PDB file path. Please provide the path: "
        )
    else:
        protein_path = pdb

    if err_csv or err_bept:
        CONSOLE.print("Error in generating BEPT default files.", style="red")
        return 0

    err_xyz = False

    def if_err_file(err, name: str, destination: str) -> bool:
        """Common output if error in generating file."""
        if err:
            CONSOLE.print(f"Error in generating {name} file.", style="red")
            return True
        CONSOLE.print(
            f"Successfully generated {name} file at: {destination}", style="green"
        )
        return False

    # TODO: Add more type of files here
    for _typ in types:
        if _typ == file_options[-1]:
            ## The csv and bept are already generated. Simply exit
            break
        if "cube" in str(_typ):
            destination_cube, err_cube = cube_make(input_dx, input_pqr, output_dir)
            if_err_file(err_cube, "cube", destination_cube)

        if "xyz" in str(_typ):
            destination_xyz, err_xyz = xyz_make(bept_csv, bept_main_path, output_dir)
            if_err_file(err_xyz, "xyz", destination_xyz)

        if "Surface" in str(_typ) or "SASA" in str(_typ):
            if "SASA" in str(_typ):
                calc_sasa(protein_path)

            else:
                destination_surf, err_surf = get_surface_resi(
                    protein_path, bept_csv, output_dir
                )
                if_err_file(
                    err_surf, "Surface Residues with Potential", destination_surf
                )
                if not err_surf:
                    CONSOLE.print(
                        "Note: The surface residues CSV file has been generated and stored in .bept directory.",
                        style="yellow",
                    )

    return 1


@main.command(short_help="Manage command history")
@click.option(
    "--clear-history",
    "-cl",
    is_flag=True,
    help="Clear command history of pdb2pqr or apbs commands used previously.",
)
@click.option(
    "--pdb2pqr",
    "-p",
    is_flag=True,
    help="Access history of pdb2pqr commands.",
)
@click.option(
    "--apbs",
    "-a",
    is_flag=True,
    help="Access history of apbs commands.",
)
@click.option(
    "--view-execute",
    "-v",
    is_flag=True,
    help="View and execute history of pdb2pqr or apbs commands.",
)
@click.option(
    "--clear-apbs-cache",
    "-cac",
    is_flag=True,
    help="Clear cache of APBS input files automatically saved.",
)
@click.option(
    "--view-apbs-cache", "-vc", is_flag=True, help="View APBS cache files in $EDITOR."
)
@click.option(
    "--print-cache-path", "-pc", is_flag=True, help="Print the apbs cache path."
)
def history(
    clear_history,
    pdb2pqr,
    apbs,
    view_execute,
    clear_apbs_cache,
    view_apbs_cache,
    print_cache_path,
):
    """
    Manage command history of pdb2pqr and apbs input files. Bept allows history and cache management for all APBS commands and input files generated.
    Run `bept history --help` for more information.
    """
    if (pdb2pqr or apbs) and not view_execute:
        CONSOLE.print(
            "Please provide -v or --view-execute along with -p or -a to view history of pdb2pqr or apbs commands.",
            style="red",
        )
        return

    if clear_history:
        history_clear()
        return

    if clear_apbs_cache:
        apbs_cache_clear()
        return

    if print_cache_path:
        CONSOLE.print("APBS cache path:", style="bold yellow")
        CONSOLE.print(f"{APBS_CACHE_DIR}")
        return

    if view_execute:
        if not (pdb2pqr or apbs):
            CONSOLE.print(
                "Please provide either -p or -a along with -v to view.", style="red"
            )
            return
        tool = "apbs" if apbs else "pdb2pqr"
        history_choose(tool)
        return

    if view_apbs_cache:
        in_sel_filepath = cache_view()
        if in_sel_filepath is None or in_sel_filepath.endswith("/.cache_apbs/"):
            CONSOLE.print("No file selected.", style="red")
            return
        prompt = "Do you want to restore the selected APBS input file? This will only create a symlink to the original file in your directory."
        if confirm(prompt):
            # Restor from cache to user's cwd
            restore_selected_cache(in_sel_filepath, os.getcwd())
        else:
            CONSOLE.print("Process restored omitted.", style="yellow")

        return

    else:
        CONSOLE.print(
            "Invalid option. Please refer `bept history --help` for more info.",
            style="red",
        )


@main.command(short_help="Generate PyMol template python codes to use with BEPT.")
@click.option(
    "--output-dir",
    "-o",
    type=click.Path(),
    help="Output directory to save the PyMol template python codes.",
)
def pymol(output_dir):
    """
    Generate PyMol template python codes to be run in PyMol terminal. You can run these files ONLY inside PyMol terminal as `run <functional_code>.py`.
    Note: These files are generated are simply templates. You will have to edit the inputs and maybe edits parts of code as per your requirement.
    """
    if not output_dir:
        output_dir = os.getcwd()
    pymol_main(output_dir)


@main.command(short_help="See Bept Documentation.")
def docs():
    """
    View Bept documentation in your terminal with a detailed information on how to use and what each command.
    """
    run_docs_viewer()
