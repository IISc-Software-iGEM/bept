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
            pdb2pqr --some-flags protein.
            apbs --some-flags protein1.in

    """
    with open(input_file, "r") as f:
        opers = f.readlines()

    for cmd in opers:
        if not cmd.strip():
            continue
        if cmd.split()[0] == "pdb2pqr":
            try:
                # :? is indicator to run that command interactively
                if ":?" in cmd:
                    p_exec(cmd, interactive=True)
                else:
                    p_exec(cmd)
                CONSOLE.print("BEPT PROCESS RAN SUCCESSFULLY", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")

        elif cmd.split()[0] == "apbs":
            try:
                # :? is indicator to run that command interactively
                if ":?" in cmd:
                    apbs_exec(cmd, True)
                else:
                    apbs_exec(cmd, interative)
                CONSOLE.print("BEPT PROCESS RAN SUCCESSFULLY", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")
        else:
            CONSOLE.print(f"INVALID COMMAND. SKIPPING {cmd}", style="bold red")

    return
