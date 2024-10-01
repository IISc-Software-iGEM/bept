import csv
import os

import pandas as pd
from rich.console import Console
from tabulate import tabulate

from bept.analysis.coord_conv import coord_to_int
from bept.analysis.elec_calc import elec
from bept.analysis.pot_extract import extract_dx_data
from bept.analysis.pot_val import val_potential
from bept.analysis.pqr_utils import pqr_line_parser

CONSOLE = Console()


def Error():
    """
    Error function to return error message
    """
    return True


def bept_make(
    pqr_file: str, pot_dx_file: str, input_csv: str, output_dir: str = os.getcwd()
):
    """
    This will make our custom potential file.
    We want the coordinate, and the potential at that coordinate.
    also each line will have x, y, z in integer.
    INFO x y z cx cy cz potential ex ey ez
    The INFO should be pqr file's data
    ATOM   N  Residue A Resi_num    x y z cx cy cz q r ex ey ez potential

    Also some pre data, which tells origin and grid length, etc.

    Args:
        pqr_file (str): Path to the PQR file
        pot_dx_file (str): Path to the potential DX file
        input_csv (str): Path to the input CSV file
        output_dir (str): Path to the output directory

    """
    # Read the CSV file using pandas
    csv_data = pd.read_csv(input_csv)

    # Extract metadata from the pot_dx_file
    data_dict = extract_dx_data(pot_dx_file)
    nx, ny, nz = data_dict["dimensions"]
    hx, hy, hz = data_dict["grid spacing"]
    hx, hy, hz = hx[0], hy[1], hz[2]
    xmin, ymin, zmin = data_dict["origin"]

    # Write metadata to the destination file
    protein = os.path.splitext(os.path.basename(pqr_file))[0]
    destination_file = os.path.join(output_dir, protein + ".bept")

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
            "Grid length(hx hy hz): " + str(hx) + " " + str(hy) + " " + str(hz) + "\n"
        )
        p.write("Reference pqr file: " + pqr_file + "\n")
        p.write("Reference dx potential file: " + pot_dx_file + "\n\n")
        CONSOLE.print("Metadata written to the BEPT file.", style="yellow")

    # Append the CSV data to the destination file in a clean tabular form
    table = tabulate(csv_data, headers="keys", tablefmt="plain", showindex=False)

    # Append the formatted table to the destination file
    try:
        with open(destination_file, "a") as p:
            p.write(table)
        CONSOLE.print(
            f"Successfully written the BEPT file for {pqr_file} : " + destination_file
        )
    except Exception as e:
        CONSOLE.print(f"Error in writing the BEPT file. Error: {e}", style="red")
        err = Error()

    return destination_file, err


def csv_make(pqr_file: str, pot_dx_file: str, output_dir: str = os.getcwd()):
    """
    This function will generate a BEPT CSV file.
    Args:
        pqr_file (str): Path to the PQR file
        pot_dx_file (str): Path to the potential DX file
        output_dir (str): Path to the output directory
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

    bept_dir = os.path.join(output_dir, ".bept")
    os.makedirs(bept_dir, exist_ok=True)

    destination_path = os.path.join(
        bept_dir, os.path.splitext(os.path.basename(pqr_file))[0] + "_bept.csv"
    )

    try:
        with open(destination_path, "w", newline="") as p:
            writer = csv.writer(p)
            # Write column headers for the data
            writer.writerow(
                [
                    "Type",
                    "Num",
                    "Atom",
                    "Resi",
                    "Chain",
                    "Resi_Seq",
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
                atom = pqr_line_parser(line)
                if atom is None:
                    continue

                # set data
                cx, cy, cz, q, r = atom.cx, atom.cy, atom.cz, atom.charge, atom.radius
                x, y, z = coord_to_int(cx, cy, cz, pot_dx_file)  # Convert to integer
                ex, ey, ez = elec(x, y, z, pot_dx_file)  # Electric field
                typ, num, atom_name = atom.type, atom.serial, atom.name
                resi, chain, resi_num = atom.res_name, atom.chain_id, atom.res_seq

                # Calculate the potential at the given coordinates
                potential = val_potential(cx, cy, cz, pot_dx_file)  # Potential

                # Write the data row
                writer.writerow(
                    [
                        typ,
                        num,
                        atom_name,
                        resi,
                        chain,
                        resi_num,
                        f"{cx:.6f}",
                        f"{cy:.6f}",
                        f"{cz:.6f}",
                        f"{q:.6f}",
                        f"{r:.6f}",
                        x,
                        y,
                        z,
                        f"{ex:>20.20f}",
                        f"{ey:>20.20f}",
                        f"{ez:>20.20f}",
                        f"{potential:>.6f}",
                    ]
                )

            CONSOLE.print(
                f"Successfully generated BEPT CSV file at: {destination_path}",
                style="green",
            )

    except Exception as e:
        CONSOLE.print(f"Error in generating BEPT CSV file. Error: {e}", style="red")
        err = Error()

    return destination_path, err
