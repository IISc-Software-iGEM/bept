import os
import shutil
import subprocess

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.theme import Theme
from beaupy import select

CONSOLE = Console()
history_dir = os.path.dirname(__file__)
CACHE_DIR = os.path.join(history_dir, ".cache_apbs")

__all__ = [
    "cache_view",
    "restore_selected_cache",
]


def tool_existance():
    """
    Check if fzf exists or not, if not fallback to cat and beaupy.
    """
    try:
        ## Check if fzf exists
        os.system("fzf --version > /dev/null")
    except Exception:  # as e:
        # CONSOLE.print(f"Fzf not found. Error: {e}", style="red")
        return False
    return True


def cache_view():
    """
    View the contents of cache directory, by opening it with fzf.
    """
    input_file_selected = None
    ## Assume FZF exists, if not, fallback to beaupy
    which_tool = "fzf" if tool_existance() else "fallback"
    if which_tool == "fzf":
        try:
            # List files in the cache directory
            files = os.listdir(CACHE_DIR)
            # Create the fzf command with preview
            fzf_prev_cmd = "echo '{}' | fzf --height 50% --preview \"sh -c 'if [ -d {}/{} ]; then ls {}/{}; else cat {}/{}; fi'\" --preview-window=right:70%:wrap".format(
                "\n".join(files), CACHE_DIR, "{}", CACHE_DIR, "{}", CACHE_DIR, "{}"
            )
            # Run the fzf command to get selected file id
            selected_file = (
                subprocess.run(fzf_prev_cmd, shell=True, capture_output=True)
                .stdout.decode()
                .strip()
            )
            input_file_selected = os.path.join(CACHE_DIR, selected_file)

        except Exception as e:
            CONSOLE.print(f"Error in viewing cache directory. Error: {e}", style="red")

    else:
        CONSOLE.print("Fzf not found. Fallback to beaupy.", style="blue")
        options = [input_file for input_file in os.listdir(CACHE_DIR)]
        options = ["EXIT View"] + options
        selected = None

        # While true ot Ctrl C is pressed
        while True:
            CONSOLE.print(
                "\nSelect the file to view from cache directory. Choose EXIT View to exit.",
                style="yellow",
            )
            CONSOLE.print(
                "Note: Your last selection will be considered for restoration, if wished.",
                style="yellow",
            )
            selected = select(options, cursor=">")
            selected_filepath = os.path.join(CACHE_DIR, str(selected))

            if selected == "EXIT View":
                input_file_selected = selected_filepath
                break

            try:
                with open(selected_filepath, "r") as file:
                    lines = file.readlines()
                    numbered_lines = "".join(
                        f"[bold cyan]{i+1:>4}[/bold cyan] │ [bold]{line}[/bold]"
                        for i, line in enumerate(lines)
                    )

                    # Use rich to display the contents in a box with line numbers
                    custom_theme = Theme(
                        {
                            "title": "bold magenta",
                            "line_number": "bold",
                            "content": "white",
                        }
                    )
                    console = Console(theme=custom_theme)
                    text = Text.from_markup(numbered_lines)
                    panel = Panel(
                        text, title=f"[title]{selected}[/title]", expand=False
                    )
                    console.print(panel)
            except Exception as e:
                CONSOLE.print(f"Error in viewing cache file. Error: {e}", style="red")

    return input_file_selected


def restore_selected_cache(in_cache_selected: str, in_cwd: str):
    """
    Restore the selected cache file to the user's current working directory.
    Args:
        in_cache_selected (str): The path to the selected cache file.
        in_cwd (str): The path to the user's current working directory.
    """
    try:
        print(in_cache_selected, in_cwd)
        # symlink the selected cache file to the user's cwd
        os.symlink(
            in_cache_selected, os.path.join(in_cwd, os.path.basename(in_cache_selected))
        )
        CONSOLE.print(
            f"Successfully restored the selected cache file to {in_cwd}", style="green"
        )
    except Exception as e:
        CONSOLE.print(f"Error in restoring cache file. Error: {e}", style="red")

    return
