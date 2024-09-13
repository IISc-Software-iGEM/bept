import os

from rich.console import Console

CONSOLE = Console()
history_dir = os.path.dirname(__file__)


def create_history():
    """
    Creates a history files if it does not exist.
    """
    ana_cmd = ["apbs", "pdb2pqr"]
    err = False
    try:
        for cmd in ana_cmd:
            his_path = os.path.join(history_dir, f"history_{cmd}.txt")
            if not os.path.exists(his_path):
                with open(his_path, "w") as his_file:
                    his_file.write("")
                CONSOLE.print(f"History file for {cmd} created.", style="bold green")
    except Exception as e:
        CONSOLE.print(f"Error in creating history file. Error: {e}", style="bold red")
        err = True

    return err


def history_access(ana_cmd: str):
    """
    Accesses the history file and returns the commands.
    Args:
        ana_cmd: command type {apbs, pdb2pqr}
    """
    his_path = os.path.join(history_dir, f"history_{ana_cmd}.txt")
    try:
        with open(his_path, "r") as his_file:
            his_cmds = his_file.readlines()
        return his_cmds

    except FileNotFoundError as e:
        CONSOLE.print(f"Error in accessing history file. Error: {e}", style="bold red")
        CONSOLE.print(f"Creating new history file for {ana_cmd}.", style="bold yellow")
        err = create_history()

        if err:
            return None

    except Exception as e:
        """
        Error in accessing history file, except FileNotFoundError.
        """
        CONSOLE.print(f"Error in accessing history file. Error: {e}", style="bold red")
        return None


def save_to_history(cmd: str, ana_cmd: str):
    """
    Saves the command to history file.
    Args:
        cmd: command to save
        ana_cmd: command type {apbs, pdb2pqr}
    """
    his_path = os.path.join(history_dir, f"history_{ana_cmd}.txt")
    err = False
    try:
        with open(his_path, "a") as his_file:
            prev_cmds = history_access(ana_cmd)
            if cmd not in prev_cmds:
                his_file.write(f"\n{cmd}")
    except Exception as e:
        CONSOLE.print(f"Error in saving to history file. Error: {e}", style="bold red")
        err = True

    return err


def delete_from_history(cmd: str, ana_cmd: str):
    """
    Deletes the command from history file.
    Args:
        cmd: command to delete
        ana_cmd: command type {apbs, pdb2pqr}
    """
    his_path = os.path.join(history_dir, f"history_{ana_cmd}.txt")
    his_cmds = history_access(ana_cmd)
    if his_cmds is None:
        CONSOLE.print(
            "Error in deleting from history. History file not found.", style="bold red"
        )
        return
    err = False

    try:
        his_cmds.remove(cmd)
        with open(his_path, "w") as his_file:
            his_file.writelines(his_cmds)

    except Exception as e:
        CONSOLE.print(
            f"Error in deleting from history file. Error: {e}", style="bold red"
        )
        err = True

    return err
