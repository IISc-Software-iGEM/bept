from rich.console import Console

from bept.main import main

CONSOLE = Console()


def bept():
    header_msg_1 = "Thanks for running BEPT - your beginner friendly neighbourhood protein analysis tool.\n"
    CONSOLE.print(header_msg_1, style="bold green")
    main()
