import os
import subprocess

from beaupy import prompt, select, select_multiple
from rich.console import Console

history_dir = os.path.dirname(__file__)


def execute(cmd):
    _cmd = cmd.split()
    subprocess.run(_cmd)


def his_choose(cmd: str):
    """
    history of command will be opened and using beaupy, someone can choose and select it.
    cmd = {"apbs", "pdb2pqr"}
    """
    history_dir = os.path.dirname(__file__)
    his_path = os.path.join(history_dir, f"history_{cmd}.txt")

    with open(his_path, "r") as his:
        his_cmds = his.readlines()

    cmd = select(
        his_cmds, cursor=">", cursor_style="cyan", pagination=True, page_size=10
    )

    console = Console()
    if len(cmd) == 0:
        console.out(f"No command in {cmd} history", style="bold red")
        return

    console.print(
        "What would you like to do with selected command?", style="bold yellow"
    )
    print(cmd)

    yn = select_multiple(
        ["execute", "edit", "save to history", "delete from history"],
        cursor_style="bold cyan",
    )

    if "delete from history" in yn:
        if cmd in his_cmds:
            his_cmds.remove(cmd)
        with open(his_path, "w") as _his:
            _his.write("".join(his_cmds))

    if "edit" in yn:
        cmd = prompt("Edit the below command:", initial_value=cmd)

    if "save to history" in yn:
        if "edit" in yn:
            with open(his_path, "a") as _his:
                _his.write(cmd)
            print("cmd saved")
        else:
            console.print(
                "You cannot save a command without editing it, to avoid repition of commands in history"
            )

        print("deleted")
    if "execute" in yn:
        execute(cmd)

    return


his_choose("pdb2pqr")
