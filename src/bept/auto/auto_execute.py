import os
import subprocess

from beaupy import prompt
from rich.console import Console
from bept.history.his_utils import save_to_history
from bept.history.cache_apbs import cache_manager

CONSOLE = Console()


def p_interactive(pdb_file: str) -> str:
    """
    Interactive pdb2pqr execution on input command present in input_file.
    Args:
        pdb_file - input pdb file of protein.
    """
    pdb_name = os.path.splitext(os.path.basename(pdb_file))[0]
    pdb2pqr_template = f"pdb2pqr --ff=AMBER --apbs-input={pdb_name}.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 {pdb_file} {pdb_name}.pqr"

    CONSOLE.print(
        "Input the pdb2pqr command to run on input PDB file. You can edit this template command for ease. For more information on parameters, see pdb2pqr --help.",
        style="bold blue",
    )
    cmd = prompt("PDB2PQR COMMAND: ", initial_value=pdb2pqr_template)
    return cmd


def apbs_interactive(input_file: str) -> str:
    """
    Interactive apbs execution on input command present in input_file.
    Args:
        input_file - input apbs file.
    """
    apbs_template = f"apbs {input_file}"

    CONSOLE.print(
        "Input the apbs command to run for APBS input file. You can edit this template command for ease. For more information on parameters, see apbs --help.",
        style="bold blue",
    )
    cmd = prompt("APBS COMMAND: ", initial_value=apbs_template)
    return cmd


def p_exec(pdb2pqr_cmd: str, interative: bool, save: bool = True) -> None:
    """
    Execution of pdb2pqr flag on input command.
    Args:
        pdb_file - input pdb file
        interative - flag for interactive mode
        save - flag for saving command to history
    """
    cmd = pdb2pqr_cmd
    if interative:
        cmd = p_interactive(pdb2pqr_cmd)

    if save:
        save_to_history(cmd, "pdb2pqr")
    print(f"Executing command: {cmd}")

    process = subprocess.run(cmd.split())
    if process.returncode != 0:
        CONSOLE.print(
            "Error in executing pdb2pqr command. Please check the command and try again.",
            style="red",
        )
        return
    cache_manager(cmd)


def apbs_exec(apbs_cmd, interative: bool, save: bool = True) -> None:
    """
    Execution of apbs command on input flag
    Args:
        input_file: .in input file for apbs
        interative: flag for interactive mode
    """
    cmd = apbs_cmd
    if interative:
        cmd = apbs_interactive(apbs_cmd)

    if save:
        save_to_history(cmd, "apbs")
    print(f"Executing command: {cmd}")
    print(cmd)

    process = subprocess.run(cmd.split())
    if process.returncode != 0:
        CONSOLE.print(
            "Error in executing APBS command. Please check the command and try again.",
            style="red",
        )
        return
    # Get input filepath, which is text containing .in
    input_filepath = next((arg for arg in cmd.split() if ".in" in arg), None)
    if input_filepath is None:
        CONSOLE.print(
            "APBS command coudn't find `.in` input file found in the command. Skipping cache creation.",
            style="red",
        )
        return
    cache_manager(input_filepath)
