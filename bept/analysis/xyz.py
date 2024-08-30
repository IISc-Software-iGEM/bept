import pandas as pd
from tabulate import tabulate


def xyz_make(input_csv: str, bept_file: str):
    """
    This file creates the .xyz format for our protein. This will take the data from the master file.
    XYZ file format-

    Number of atoms
    Comment line(inclue protein.pdb and origin coordinates)
    Atom1 x y z
    . . .
    """
    with open(bept_file, "r") as m:
        bept_data = m.readlines()

    protein = bept_file.split(".")[0]
    destination_path = protein + ".xyz"

    with open(input_csv, "r") as f:
        csv_data = pd.read_csv(f)

    no_of_atoms = len(csv_data)
    origin = bept_data[1].split(":")[1].strip()

    with open(destination_path, "w") as p:
        # use tabulate for better formatting
        p.write(str(no_of_atoms) + "\n")
        p.write("Protein: " + protein + " Origin: " + origin + "\n")
        # only take TYPE, X, Y, Z columns
        table = tabulate(
            csv_data[["Atom", "X", "Y", "Z"]],
            headers="keys",
            tablefmt="plain",
            showindex=False,
        )
        p.write(table)

    return destination_path
