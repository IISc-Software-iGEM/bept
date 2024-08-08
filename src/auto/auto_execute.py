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
    cmd_temp = f"pdb2pqr --ff=AMBER --apbs-input={pdb_name}.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 {pdb_name}.pdb {pdb_name}.pqr"

    CONSOLE.print(
        "Input the pdb2pqr command to run on input PDB file. You can edit this template command for ease.",
        style="bold blue",
    )
    cmd = prompt("PDB2PQR COMMAND: ", initial_value=cmd_temp)
    print(f"Executing command: {cmd}")

    subprocess.run(cmd.split())


p_exec("7y6i.pdb")
