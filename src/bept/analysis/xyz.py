import pandas as pd
from tabulate import tabulate
from rich.console import Console

CONSOLE = Console()


def xyz_make(input_csv: str, bept_file: str):
    """
    This file creates the .xyz format for our protein. This will take the data from the master file.
    XYZ file format-

    Number of atoms
    Comment line(inclue protein.pdb and origin coordinates)
    Atom1 x y z
    . . .
    """
    destination_path, err = "", False
    try:
        # Read BEPT file
        with open(bept_file, "r") as m:
            bept_data = m.readlines()

        # Extract protein name and determine the destination path
        protein = bept_file.split(".")[0]
        destination_path = protein + ".xyz"

        # Read CSV file
        with open(input_csv, "r") as f:
            csv_data = pd.read_csv(f)

        # Calculate number of atoms and extract origin
        no_of_atoms = len(csv_data)
        origin = bept_data[1].split(":")[1].strip()

        # Write to destination file using tabulate for better formatting
        with open(destination_path, "w") as p:
            p.write(str(no_of_atoms) + "\n")
            p.write("Protein: " + protein + " Origin: " + origin + "\n")
            table = tabulate(
                csv_data[["Atom", "X", "Y", "Z"]],
                headers="keys",
                tablefmt="plain",
                showindex=False,
            )
            p.write(table)

        return destination_path, err

    except FileNotFoundError as e:
        CONSOLE.print(f"Error: {e}. The file {e.filename} does not exist.", style="red")
    except pd.errors.EmptyDataError:
        CONSOLE.print("Error: The input CSV file is empty.", style="red")
    except KeyError as e:
        CONSOLE.print(f"Error: Missing column in CSV data: {e}", style="red")
    except IndexError:
        CONSOLE.print("Error: Unexpected file format in BEPT file.", style="red")
    except Exception as e:
        CONSOLE.print(f"An unexpected error occurred: {e}", style="red")

    err = True

    return destination_path, err
