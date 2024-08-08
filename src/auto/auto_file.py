from rich.console import Console

from .auto_execute import *

CONSOLE = Console()


def file_runner(input_file):
    """
    Loads the functions and loads to executor function.
    Each line has pdb file name for pdb2pqr and input file name for apbs.
    Args:
        input_file: contains the file with name,
        FORMAT:
            pdb2pqr protein.
            apbs protein1.in
            ...

    """
    with open(input_file, "r") as f:
        opers = f.readlines()

    operations = [
        (oper.split()[0], oper.split()[1]) for oper in opers if len(oper.split()) == 2
    ]

    for cmd in operations:
        if cmd[0] == "pdb2pqr":
            try:
                p_exec(cmd[1])
                CONSOLE.print("PROCESS SUCCESS", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")
        elif cmd[0] == "apbs":
            try:
                apbs_exec(cmd[1])
                CONSOLE.print("PROCESS SUCCESS", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")
        else:
            CONSOLE.print(
                f"INVALID COMMAND. SKIPPING {cmd[0], cmd[1]}", style="bold red"
            )

    return
