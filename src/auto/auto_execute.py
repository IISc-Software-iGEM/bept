import os
import subprocess

from beaupy import prompt
from rich.console import Console

CONSOLE = Console()


def p_exec(pdb_file):
    """
    Execution of pdb2pqr flag on input command.
    Args:
        pdb_file - input pdb file
    """
    pdb_name = os.path.splitext(os.path.basename(pdb_file))[0]
    pdb2pqr_template = f"pdb2pqr --ff=AMBER --apbs-input={pdb_name}.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 {pdb_file} {pdb_name}.pqr"

    CONSOLE.print(
        "Input the pdb2pqr command to run on input PDB file. You can edit this template command for ease. For more information on parameters, see pdb2pqr --help.",
        style="bold blue",
    )
    cmd = prompt("PDB2PQR COMMAND: ", initial_value=pdb2pqr_template)
    print(f"Executing command: {cmd}")

    subprocess.run(cmd.split())


def apbs_exec(input_file):
    """
    Execution of apbs command on input flag
    Args:
        input_file: .in input file for apbs
    """

    apbs_template = f"apbs {input_file}"

    CONSOLE.print(
        "Input the apbs command to run for APBS input file. You can edit this template command for ease. For more information on parameters, see apbs --help."
    )
    cmd = prompt("APBS COMMAND: {cmd}", initial_value=apbs_template)
    print(f"Executing command: {cmd}")

    subprocess.run(cmd.split())
