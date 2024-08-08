import os

import rich_click as click

from .analysis.pot_main import *


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option("some_name v1.0.0", "--version", "-v")
def main():
    """
    <my_tool> is a beginner friendly CLI to start with protein analysis. You can perform APBS calculations using pdb2pqr and apbs interactively along with automating your work on multiple input proteins. <more_stuff>

    This was built as part of the project IMPROVISeD, by IISc-Software-iGEM Team 2024.
    """
    pass


@main.command(short_help="Generate pdb2pqr, apbs commands interactively")
@click.option(
    "--pdb2pqr",
    "-p",
    is_flag=True,
    type=click.Path(exists=True),
    help="Path to the pdb file",
)
@click.option(
    "--apbs",
    "-a",
    is_flag=True,
    type=click.Path(exists=True),
    help="Path to the apbs input file",
)
@click.option(
    "--interactive", "-i", is_flag=True, help="Generate commands interactively"
)
def gen(pdb, apbs, interactive_gen):
    """
    Generate pdb2pqr, apbs commands interactively. You can run this command as ....
    """
    pass


@main.command(short_help="Automate calculation of pdb2pqr and APBS.")
@click.option(
    "--clear-history",
    "-cl",
    is_flag=True,
    default=False,
    short_help="Clear command history stored of pdb2pqr or apbs commands used previously.",
)
@click.option(
    "--pdb2pqr",
    "-p",
    is_flag=True,
    type=click.Path(exists=True),
    help="Path to the pdb file",
)
@click.option(
    "--apbs",
    "-a",
    is_flag=True,
    type=click.Path(exists=True),
    help="Path to the apbs input file",
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
def auto(clear_history, pdb, apbs, cmd_history, file_load):
    """
    Automate pdb2pqr, apbs commands for multiple proteins. You can run this command as ....
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
