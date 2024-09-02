import rich_click as click
from beaupy import select_multiple

from bept.analysis.pot_main import csv_make, bept_make, CONSOLE
from bept.analysis.xyz import xyz_make
from bept.auto.auto_execute import p_exec, apbs_exec
from bept.auto.auto_file import file_runner
from bept.auto.his_main import history_clear, history_choose
from bept.validator import validate_apbs, validate_dx, validate_pdb2pqr


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option("some_name v1.0.0", "--version", "-v")
def main():
    """
    BEPT is a Beginner friendly Protein Analysis Tool to start with protein analysis. You can perform APBS calculations using pdb2pqr and apbs interactively along with automating your work on multiple input proteins. <more_stuff>

    This was built as part of the project IMPROVISeD, by IISc-Software-iGEM Team 2024.
    """
    pass


@main.command(short_help="Automate calculation of pdb2pqr and APBS.")
@click.option(
    "--clear-history",
    "-cl",
    is_flag=True,
    default=False,
    help="Clear command history stored of pdb2pqr or apbs commands used previously.",
)
@click.option(
    "--pdb2pqr",
    "-p",
    multiple=True,
    type=click.Path(exists=True),
    callback=validate_pdb2pqr,
    help="Run pdb2pqr command. Input PDB file path.",
)
@click.option(
    "--apbs",
    "-a",
    type=click.Path(exists=True),
    multiple=True,
    callback=validate_apbs,
    help="Run apbs command. Input APBS input file path.",
)
@click.option(
    "--cmd-history",
    "-c",
    is_flag=True,
    help="Use previously generated commands from history",
)
@click.option(
    "--file-load",
    "-f",
    type=click.Path(exists=True),
    help="Load list of protein or input files to automate.",
)
def auto(clear_history, pdb2pqr, apbs, cmd_history, file_load):
    """
    Automate pdb2pqr, apbs commands for multiple proteins. You can run this command as ....
    """
    # clear history
    if clear_history:
        history_clear()
        return

    if file_load:
        file_runner(file_load)
        return

    if not (apbs or pdb2pqr) and not cmd_history:
        click.echo(
            "Either one of -a or -p must be chosen, or use -c for command history. Refer bept auto -h for more information."
        )
        return

    tool = "apbs" if apbs else "pdb2pqr"
    if cmd_history:
        history_choose(tool)

    # Command processing based on provided arguments or history
    if apbs:
        input_file = apbs[0]
        apbs_exec(input_file)
        return

    if pdb2pqr:
        pdb_file = pdb2pqr[0]
        p_exec(pdb_file)
        return


@main.command(short_help="Generate pdb2pqr, apbs commands interactively")
@click.option(
    "--pdb2pqr",
    "-p",
    multiple=True,
    callback=validate_pdb2pqr,
    help="Run pdb2pqr command. Input PDB file path.",
)
@click.option(
    "--apbs",
    "-a",
    multiple=True,
    callback=validate_apbs,
    help="Run apbs command. Input APBS input file path.",
)
@click.option(
    "--interactive", "-i", is_flag=True, help="Generate commands interactively"
)
def gen(pdb2qr, apbs, interactive):
    """
    Generate pdb2pqr, apbs commands interactively. You can run this command as ....
    """
    pass


@main.command(short_help="Output File generation for potential output files")
@click.option(
    "--dx",
    "-d",
    type=click.Path(exists=True),
    required=True,
    nargs=2,
    callback=validate_dx,
    help="Input PQR file and corresponding APBS pot_dx file.",
)
@click.option(
    "--interactive",
    "-i",
    is_flag=True,
    help="Interactively select which files to generate. Default: only .bept",
)
@click.option(
    "--all",
    "-a",
    is_flag=True,
    help="Generate all other supported output files.",
)
def out(interactive, dx, all):
    """
    Generate output files for potential output files. You can run this command as ....
    """
    # using dx direcly since its REQUIRED
    input_pqr, input_dx = dx  # unpacking the tuple

    file_options = [
        "cube: Gaussian .cube file",
        "xyz: .xyz format for input protein",
        "Cancel and generate default",  # Always last option
    ]
    types = "bept: .bept file containing all data"
    if all:
        types = file_options

    if interactive:
        CONSOLE.print(
            "A csv containing all data will be generated. Choose among the following types of files you would also like to choose.",
            style="bold blue",
        )
        types = select_multiple(file_options)

    bept_csv, err_csv = csv_make(input_pqr, input_dx)
    bept_main_path, err_bept = bept_make(input_pqr, input_dx, bept_csv)
    if err_csv or err_bept:
        CONSOLE.print("Error in generating default files.")
        return 0

    for _typ in types:
        if _typ == file_options[-1]:
            ## The csv and bept are already generated. Simply exit
            CONSOLE.print("Default files are already generated.")
            break
        # if _typ == file_options[0]:
        #   cube_make(input_pqr, input_dx)
        if _typ == file_options[1]:
            xyz_make(bept_csv, bept_main_path)
