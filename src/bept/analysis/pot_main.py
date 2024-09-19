import csv

import pandas as pd
from rich.console import Console
from tabulate import tabulate

from bept.analysis.coord_conv import coord_to_int
from bept.analysis.elec_calc import elec
from bept.analysis.pot_extract import extract
from bept.analysis.pot_val import val_potential

CONSOLE = Console()


def Error():
    """
    Error function to return error message
    """
    return True


def bept_make(pqr_file, pot_dx_file, input_csv):
    """
    This will make our custom potential file.
    We want the coordinate, and the potential at that coordinate.
    also each line will have x, y, z in integer.
    INFO x y z cx cy cz potential ex ey ez
    The INFO should be pqr file's data
    ATOM   N  Residue A Resi_num    x y z cx cy cz q r ex ey ez potential

    Also some pre data, which tells origin and grid length, etc.
    """
    # Read the CSV file using pandas
    csv_data = pd.read_csv(input_csv)

    # Extract metadata from the pot_dx_file
    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz = extract(pot_dx_file)

    # Write metadata to the destination file
    protein = pqr_file.split(".")[0]
    destination_file = protein + ".bept"

    err = False
    with open(destination_file, "w") as p:
        p.write("Protein structure: " + protein + "\n")
        p.write(
            "Origin(xmin, ymin, zmin): "
            + str(xmin)
            + " "
            + str(ymin)
            + " "
            + str(zmin)
            + "\n"
        )
        p.write(
            "Grid Box Size(x y z): " + str(nx) + " " + str(ny) + " " + str(nz) + "\n"
        )
        p.write(
            "Grid length(cx cy cz): " + str(hx) + " " + str(hy) + " " + str(hz) + "\n"
        )
        p.write("Reference pqr file: " + pqr_file + "\n")
        p.write("Reference dx potential file: " + pot_dx_file + "\n\n")
        print("Written Header Files.")

    # Append the CSV data to the destination file in a clean tabular form
    table = tabulate(csv_data, headers="keys", tablefmt="plain", showindex=False)

    # Append the formatted table to the destination file
    try:
        with open(destination_file, "a") as p:
            p.write(table)
    except Exception as e:
        CONSOLE.print(f"Error in writing the BEPT file. Error: {e}", style="red")
        err = Error()

    return destination_file, err


def csv_make(pqr_file, pot_dx_file):
    """
    This will make the csv file containing all the info
    """
    err = False
    try:
        with open(pqr_file, "r") as f:
            pqr_data = f.readlines()
        with open(pot_dx_file, "r"):
            pass
        CONSOLE.print(f"Input PQR File: {pqr_file}")
        CONSOLE.print(f"Input Potential DX file: {pot_dx_file}")
    except Exception as e:
        CONSOLE.print(
            f"Error in accepting input files.\n Recieved paths: {pqr_file} & {pot_dx_file}. Error: {e}",
            style="red",
        )
        err = Error()
        return 0

    destination_path = pqr_file.split(".")[0] + "_bept.csv"

    try:
        with open(destination_path, "w", newline="") as p:
            writer = csv.writer(p)
            CONSOLE.print(
                f"Successfully generated BEPT CSV file at: {destination_path}"
            )
            # Write column headers for the data
            writer.writerow(
                [
                    "Type",
                    "Num",
                    "Atom",
                    "Resi",
                    "Chain",
                    "Cx",
                    "Cy",
                    "Cz",
                    "Q",
                    "R",
                    "X",
                    "Y",
                    "Z",
                    "Ex",
                    "Ey",
                    "Ez",
                    "Potential",
                ]
            )

            for line in pqr_data:
                line = line.split()
                cx, cy, cz, q, r = (
                    line[-5],
                    line[-4],
                    line[-3],
                    line[-2],
                    line[-1],
                )  # PQR file data
                x, y, z = coord_to_int(cx, cy, cz, pot_dx_file)  # Convert to integer
                ex, ey, ez = elec(x, y, z, pot_dx_file)  # Electric field
                potential = val_potential(cx, cy, cz, pot_dx_file)  # Potential
                typ, num, atom, resi, chain = (
                    line[0],
                    line[1],
                    line[2],
                    line[3],
                    line[4],
                )

                # Write the data row
                writer.writerow(
                    [
                        typ,
                        num,
                        atom,
                        resi,
                        chain,
                        cx,
                        cy,
                        cz,
                        q,
                        r,
                        x,
                        y,
                        z,
                        ex,
                        ey,
                        ez,
                        potential,
                    ]
                )

    except Exception as e:
        CONSOLE.print(f"Error in generating BEPT CSV file. Error: {e}", style="red")
        err = Error()

    return destination_path, err
