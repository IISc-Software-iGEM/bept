import os

import rich_click as click

from .analysis.pot_main import *
from .auto.his_main import *


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option("some_name v1.0.0", "--version", "-v")
def main():
    """
    <my_tool> is a beginner friendly CLI to start with protein analysis. You can perform APBS calculations using pdb2pqr and apbs interactively along with automating your work on multiple input proteins. <more_stuff>

    This was built as part of the project IMPROVISeD, by IISc-Software-iGEM Team 2024.
    """
    pass


def validate_pdb2pqr(ctx, param, value):
    if ctx.params.get("cmd_history"):
        return value
    if value:
        if len(value) != 1:
            raise click.BadParameter(
                "pdb2pqr requires exactly one arguments: <pdb_filepath>.pdb."
            )
        if not (value[0].endswith(".pdb")):
            raise click.BadParameter("The first argument must be a .pdb file.")
    return value


def validate_apbs(ctx, param, value):
    if ctx.params.get("cmd_history"):
        return value
    if value:
        if len(value) != 1 or not value[0].endswith(".in"):
            raise click.BadParameter(
                "apbs requires exactly one argument with .in file type."
            )
    return value


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
    "--cmd-history",
    "-c",
    is_flag=True,
    help="Use previously generated commands from history",
)
@click.option(
    "--file-load",
    "-f",
    is_flag=True,
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

    if not (apbs or pdb2pqr) and not cmd_history:
        click.echo(
            "Either one of -a or -p must be chosen, or use -c for command history."
        )
        return

    tool = "apbs" if apbs else "pdb2pqr"
    if cmd_history:
        history_choose(tool)

    # Command processing based on provided arguments or history
    if apbs:
        input_file = apbs[0]

    if pdb2pqr:
        pdb_file = pdb2pqr[0]


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
    "--interactive",
    "-i",
    is_flag=True,
    help="Interactively select which files to generate.",
)
@click.option("--all", "-a", is_flag=True, help="Generate all output files.")
def out(interactive, all):
    """
    Generate output files for potential output files. You can run this command as ....
    """
    pass


if __name__ == "__main__":
    main()
