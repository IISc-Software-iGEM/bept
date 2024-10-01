from rich.console import Console

from bept.auto.auto_execute import apbs_exec, p_exec

CONSOLE = Console()


def status_log_print(status_log: list):
    """
    Status log for the processes run in file_load automation at the end.
    Args:
        status_log: list of tuples containing command and status
    """
    print()
    CONSOLE.print("STATUS LOG", style="bold blue")
    for cmd, return_code in status_log:
        if return_code == 0:
            CONSOLE.print(cmd.strip(), end="")
            CONSOLE.print(" - SUCCESS", style="bold green")

        elif return_code == 999:
            CONSOLE.print(cmd.strip(), end="")
            CONSOLE.print(" - INVALID COMMAND", style="bold yellow")

        else:
            CONSOLE.print(cmd.strip(), end="")
            CONSOLE.print(" - FAILED", style="bold red")

    return


def file_runner(input_file: str, interactive: bool = False):
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

    # status log for the processes
    status_log = []

    for cmd in opers:
        return_code = 0
        if not cmd.strip():
            continue
        if cmd.split()[0] == "pdb2pqr":
            try:
                # :? is indicator to run that command interactively
                if " :?" in cmd:
                    return_code = p_exec(cmd, interactive=True)
                else:
                    return_code = p_exec(cmd, interactive=interactive)
                CONSOLE.print("BEPT PROCESS RAN SUCCESSFULLY", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")

            status_log.append((cmd, return_code))

        elif cmd.split()[0] == "apbs":
            try:
                # :? is indicator to run that command interactively
                if " :?" in cmd:
                    apbs_exec(cmd, interactive=True)
                else:
                    apbs_exec(cmd, interactive=interactive)
                CONSOLE.print("BEPT PROCESS RAN SUCCESSFULLY", style="bold green")
            except Exception as e:
                CONSOLE.print(f"PROCESS FAILED. Error: {e}", style="bold red")

            status_log.append((cmd, return_code))
        elif cmd.split()[0].strip() == "#":
            continue
        else:
            CONSOLE.print(f"INVALID COMMAND. SKIPPING {cmd}", style="bold red")
            status_log.append((cmd, 999))

    status_log_print(status_log)
    return
