import subprocess

from beaupy import prompt
from rich.console import Console
from bept.history.his_utils import save_to_history
from bept.history.cache_apbs import cache_manager

CONSOLE = Console()


def p_interactive(pdb2pqr_cmd: str) -> str:
    """
    Interactive pdb2pqr execution on input command present in input_file.
    Args:
        pdb2pqr_cmd - input pdb2pqr command by user
    """
    ## get pdb name from the protein.pdb present in the command
    pdb_name = next((arg for arg in pdb2pqr_cmd.split() if ".pdb" in arg), None)
    if pdb_name is None:
        CONSOLE.print(
            "Error in extracting pdb file name. Please provide the pdb file name in the command.",
            style="red",
        )
        return pdb2pqr_cmd

    pdb2pqr_template = f"pdb2pqr --ff=AMBER --apbs-input={pdb_name[:-4]}.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 {pdb_name} {pdb_name[:-4]}.pqr"

    CONSOLE.print(
        "Input the pdb2pqr command to run on input PDB file. You can copy and user this template command for ease. For more information on parameters, see pdb2pqr --help.",
        style="bold blue",
    )
    print(f"Template command: {pdb2pqr_template}")
    cmd = prompt("PDB2PQR COMMAND: ", initial_value=pdb2pqr_cmd)
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


def p_exec(pdb2pqr_cmd: str, interactive: bool = False, save: bool = True) -> None:
    """
    Execution of pdb2pqr flag on input command.
    Args:
        pdb2pqr_cmd - input pdb2pqr command
        interactive - flag for interactive mode
        save - flag for saving command to history
    """
    cmd = pdb2pqr_cmd
    if interactive:
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

    else:
        CONSOLE.print("PDB2PQR command executed successfully!", style="green")

    # Get input filepath, which is text containing .pqr
    input_flag = next((arg for arg in cmd.split() if ".in" in arg), None)
    if input_flag is None:
        CONSOLE.print(
            "PDB2PQR command coudn't find `.in` input file found in the command. Skipping cache creation.",
            style="red",
        )
        return
    input_filepath = input_flag.split("=")[1]
    cache_manager(input_filepath)


def apbs_exec(apbs_cmd: str, interactive: bool = False, save: bool = True) -> None:
    """
    Execution of apbs command on input flag
    Args:
        apbs_cmd - input apbs command
        interactive - flag for interactive mode
        save - flag for saving command to history
    """
    cmd = apbs_cmd
    if interactive:
        cmd = apbs_interactive(apbs_cmd)

    if save:
        save_to_history(cmd, "apbs")
    print(f"Executing command: {cmd}")

    process = subprocess.run(cmd.split())
    if process.returncode != 0:
        CONSOLE.print(
            "Error in executing APBS command. Please check the command and try again.",
            style="red",
        )
        return

    else:
        CONSOLE.print("APBS command executed successfully!", style="green")
    # Get input filepath, which is text containing .in
    input_filepath = next((arg for arg in cmd.split() if ".in" in arg), None)
    if input_filepath is None:
        CONSOLE.print(
            "APBS command coudn't find `.in` input file found in the command. Skipping cache creation.",
            style="red",
        )
        return
    cache_manager(input_filepath)
