import os
import shutil

from rich.console import Console

CONSOLE = Console()
history_dir = os.path.dirname(__file__)
CACHE_DIR = os.path.join(history_dir, ".cache_apbs")


def cache_manager(input_filepath: str):
    """
    All the output APBS input files will be saved as cache in .cache_apbs dir.
    Symlink will be made from .cache to user's cwd
    Args:
        input_filepath (str): The path to the input file.
    """
    # Create cache directory if not exists
    if not os.path.exists(CACHE_DIR):
        CONSOLE.print("Warning! APBS input cache directory not found.", style="yellow")
        os.makedirs(CACHE_DIR)
        CONSOLE.print(f"Created cache directory at: {CACHE_DIR}", style="green")
        CONSOLE.print(
            "Note, all your APBS input files will be saved there, for your future reference.",
            style="yellow",
        )

    # Move the file to the cache directory
    filename = os.path.basename(input_filepath)
    cached_filepath = os.path.join(CACHE_DIR, filename)
    shutil.move(input_filepath, cached_filepath)

    # Create symlink to cache directory
    err = symlink_cache(cached_filepath, input_filepath)
    if not err:
        CONSOLE.print(
            "Successfully created symlink to cache_apbs directory",
            style="green",
        )


def symlink_cache(cached_filepath: str, input_filepath: str):
    """
    Symlink the cache directory to the user's current working directory.
    Args:
        cached_filepath (str): The path to the cached file.
        input_filepath (str): The path to the input file
    """
    # Create symlink to cache directory
    err = False
    try:
        os.symlink(cached_filepath, input_filepath)

    except Exception as e:
        CONSOLE.print(f"Error in creating symlink. Error: {e}", style="red")
        err = True

    return err


def clear_apbs_cache():
    """
    Clears the cache directory of APBS input files.
    """
    try:
        shutil.rmtree(CACHE_DIR)
        CONSOLE.print("Successfully cleared APBS input cache directory.", style="green")
    except Exception as e:
        CONSOLE.print(
            f"Error in clearing APBS input cache directory. Error: {e}", style="red"
        )

    return
