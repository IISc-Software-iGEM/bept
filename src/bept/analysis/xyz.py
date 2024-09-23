import pandas as pd
import os
from tabulate import tabulate
from rich.console import Console

CONSOLE = Console()


def xyz_make(input_csv: str, bept_file: str, output_dir: str = os.getcwd()):
    """
    This file creates the .xyz format for our protein. This will take the data from the master file.
    XYZ file format-

    Number of atoms
    Comment line(inclue protein.pdb and origin coordinates)
    Atom1 x y z
    . . .

    Args:
        input_csv (str): Path to the input CSV file
        bept_file (str): Path to the BEPT file
        output_dir (str): Path to the output directory
    """
    destination_path, err = "", False
    try:
        # Read BEPT file
        with open(bept_file, "r") as m:
            bept_data = m.readlines()

        # Extract protein name and determine the destination path
        protein = os.path.splitext(os.path.basename(bept_file))[0]
        destination_path = os.path.join(output_dir, protein + ".xyz")

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
                csv_data[["Atom", "Cx", "Cy", "Cz"]],
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
