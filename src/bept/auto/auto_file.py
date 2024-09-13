from rich.console import Console

from bept.auto.auto_execute import apbs_exec, p_exec

CONSOLE = Console()


def file_runner(input_file: str, interative: bool = False):
    """
    Loads the functions and loads to executor function.
    Each line has pdb file name for pdb2pqr and input file name for apbs.
    Args:
        input_file: contains the file with name,
        FORMAT:
            pdb2pqr protein.
            apbs protein1.in

    """
    with open(input_file, "r") as f:
        opers = f.readlines()

    for cmd in opers:
        if cmd[0] == "pdb2pqr":
            try:
                # :? is indicator to run that command interactively
                if ":?" in cmd:
                    p_exec(cmd, True)
                else:
                    p_exec(cmd, interative)
                CONSOLE.print("PROCESS SUCCESS", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")

        elif cmd[0] == "apbs":
            try:
                # :? is indicator to run that command interactively
                if ":?" in cmd:
                    apbs_exec(cmd, True)
                else:
                    apbs_exec(cmd, interative)
                CONSOLE.print("PROCESS SUCCESS", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")
        else:
            CONSOLE.print(
                f"INVALID COMMAND. SKIPPING {cmd[0], cmd[1]}", style="bold red"
            )

    return
