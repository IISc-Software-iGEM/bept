import os
import subprocess

from beaupy import prompt, select, select_multiple
from rich.console import Console
from bept.history.his_utils import save_to_history, delete_from_history, history_access
from bept.auto.auto_execute import p_exec, apbs_exec

history_dir = os.path.dirname(__file__)

CONSOLE = Console()


def history_clear():
    """
    Clears command history from history_{ana_cmd}.txt
    """
    CONSOLE.print(
        "Clear command history of which of the following commands - ", style="yellow"
    )
    cmd_choice = select(
        ["apbs", "pdb2pqr", "all", "exit with clearing any"],
        cursor=">",
        cursor_style="bold cyan",
    )
    if cmd_choice == "exit with clearing any":
        CONSOLE.print("No command history cleared.", style="bold red")
        return

    cmds_to_clear = [cmd_choice]
    if cmd_choice == "all":
        cmds_to_clear = ["apbs", "pdb2pqr"]

    for cmd in cmds_to_clear:
        his_path = os.path.join(history_dir, f"history_{cmd}.txt")
        try:
            with open(his_path, "w") as file:
                file.write("")
            CONSOLE.print(
                f"Successfully cleared {cmd} command history.", style="bold green"
            )
        except Exception as e:
            CONSOLE.print(
                f"Error in clearing {cmd} command history. Error: {e}", style="bold red"
            )


def history_choose(ana_cmd: str):
    """
    Presents a history of a given command for selection using beaupy.

    The user can choose a command from the history to execute, edit,
    save back to history, or delete from history.

    Args:
        ana_cmd (str): The command whose history is to be managed.
    """
    CONSOLE.print(
        f"Command History of {ana_cmd} in pages. Choose one command among the following.",
        style="bold blue",
    )

    his_cmds = history_access(ana_cmd)

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

    # add new
    if his_cmd_options[0] in actions:
        cmd = prompt(
            "Add new command below with chosen command as base:",
            initial_value=cmd,
        )

    # delete command
    if his_cmd_options[4] in actions:
        if cmd in his_cmds:
            err = delete_from_history(cmd, ana_cmd)
            if not err:
                CONSOLE.print("Command deleted from history.", style="bold green")

    # edit command
    if his_cmd_options[2] in actions:
        cmd = prompt("Edit the command below:", initial_value=cmd)
        print(cmd)

    # Save command
    save = False
    if his_cmd_options[3] in actions:
        save = True
        if "Edit" in actions:
            err = save_to_history(cmd, ana_cmd)
            if not err:
                CONSOLE.print("Command saved to history.", style="bold green")
        else:
            CONSOLE.print(
                "Cannot save the command without editing it, to avoid repetition in history.",
                style="bold red",
            )

    # execute command
    if his_cmd_options[1] in actions:
        if ana_cmd == "pdb2pqr":
            p_exec(str(cmd), False, save=save)
        elif ana_cmd == "apbs":
            apbs_exec(str(cmd), False, save=save)

    return
