import os
import subprocess

from beaupy import prompt, select, select_multiple
from rich.console import Console

history_dir = os.path.dirname(__file__)

CONSOLE = Console()


def history_clear():
    """
    Clears command history from history_{ana_cmd}.txt
    """
    cmd_choice = select(["apbs", "pdb2pqr"], cursor=">", cursor_style="bold cyan")
    his_path = os.path.join(history_dir, f"history_{cmd_choice}.txt")
    with open(his_path, "w") as file:
        file.write("")
    CONSOLE.print(f"Successfully cleared {cmd_choice} command history.")


def history_choose(ana_cmd: str):
    """
    Presents a history of a given command for selection using beaupy.

    The user can choose a command from the history to execute, edit,
    save back to history, or delete from history.

    Args:
        ana_cmd (str): The command whose history is to be managed.
    """
    his_path = os.path.join(history_dir, f"history_{ana_cmd}.txt")

    try:
        with open(his_path, "r") as his_file:
            his_cmds = his_file.readlines()
    except FileNotFoundError:
        CONSOLE.print(f"No history found for {ana_cmd}.", style="bold red")
        return

    CONSOLE.print(
        f"Command History of {ana_cmd} in pages. Choose one command among the following.",
        style="bold blue",
    )

    cmd = select(
        his_cmds, cursor=">", cursor_style="cyan", pagination=True, page_size=10
    )

    if not cmd:
        CONSOLE.print(f"No command selected from {ana_cmd} history.", style="bold red")
        return

    CONSOLE.print(
        "What would you like to do with the selected command?", style="bold yellow"
    )
    print(cmd)
    his_cmd_options = [
        "Add new: To write your own command. NOTE: Check below boxes to execute/edit/save your new command",
        "Execute: To execute chosen/new command.",
        "Edit: To edit chosen/new command.",
        "Save to History: To save your/new command in command history.",
        "Delete from History: To delete your chosen command from history.",
    ]

    actions = select_multiple(
        his_cmd_options,
        cursor_style="bold cyan",
    )

    old_cmd = cmd
    # add new
    if his_cmd_options[0] in actions:
        cmd = prompt(
            "Add new command below with chosen command as base:",
            initial_value=cmd,
        )

    # delete command
    if his_cmd_options[4] in actions:
        if cmd in his_cmds:
            his_cmds.remove(old_cmd)
            with open(his_path, "w") as his_file:
                his_file.writelines(his_cmds)
            CONSOLE.print("Command deleted from history.", style="bold green")

    # edit command
    if his_cmd_options[2] in actions:
        cmd = prompt("Edit the command below:", initial_value=cmd)
        print(cmd)

    # Save command
    if his_cmd_options[3] in actions:
        if "Edit" in actions:
            with open(his_path, "a") as his_file:
                his_file.write(cmd)
            CONSOLE.print("Command saved to history.", style="bold green")
        else:
            CONSOLE.print(
                "Cannot save the command without editing it, to avoid repetition in history.",
                style="bold red",
            )

    # execute command
    if his_cmd_options[1] in actions:
        _cmd = str(cmd).split()
        subprocess.run(_cmd)

    return
