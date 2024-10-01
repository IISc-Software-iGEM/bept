import csv
import os
from collections import defaultdict

from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley
from rich.console import Console
from tabulate import tabulate
from beaupy.spinners import Spinner, DOTS

CONSOLE = Console()


def biop_fetch(protein_file: str):
    """
    Returns the struct and pdb_id of the protein
    """
    p = PDBParser(QUIET=1)
    protein_id = (
        os.path.splitext(protein_file)[0]
        if protein_file.endswith(".pdb")
        else protein_file
    )
    return p.get_structure(protein_id, protein_file), protein_id


def calc_sasa(protein_file: str) -> None:
    """
    Args:
    protein_file: The PDB file path of the protein

    Output:
    SASA: The solvent accessible surface area
    """
    struct, _ = biop_fetch(protein_file)

    CONSOLE.print(
        f"Calculating SASA for {protein_file}. This is going to take a while."
    )
    spinner = Spinner(DOTS, text="Calculating SASA... Hold on tight!")
    spinner.start()

    sr = ShrakeRupley()
    sr.compute(struct, level="S")
    sasa_value = round(struct.sasa, 6)

    spinner.stop()

    CONSOLE.print(f"SASA value for {protein_file}: {sasa_value} Å²")
    return


def meta_data_surface(protein_file: str, surface_residue_csvpath: str):
    """
    To write the metadata in the surface residues file at top.
    Args:
    protein_file: the pdb file of protein
    surface_residue_csvpath: the path to the surface residues csv file
    """
    _, protein_id = biop_fetch(protein_file)

    with open(surface_residue_csvpath, "r") as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Calculate metadata
    num_residues = len(data) - 1  # Subtracting 1 for the header row
    sum_potentials = sum(float(row[2]) for row in data[1:])

    # Prepare metadata
    metadata = [
        f"Surface residues data for {protein_file} generate by BEPT.",
        f"Protein ID: {protein_id}",
        f"Number of residues: {num_residues}",
        f"Sum of all potentials: {sum_potentials}",
    ]

    return "\n".join(metadata)


def get_surface_resi(
    protein_file: str, protein_bept_csvpath: str, output_dir: str = os.getcwd()
):
    """
    Output the surface residues of the protein in csv format and tabulated format

    Args:
    protein_file: the pdb file of protein
    protein_bept_csvpath: the path to the protein's bept csv file
    output_dir: the directory to store the output csv file
    """
    if protein_file is None or protein_file.strip() == "":
        CONSOLE.print("No protein file provided", style="red")
        return "", True

    _, protein_id = biop_fetch(protein_file)
    err_surface_calc = False
    destination_surface_resi_path = ""
    try:
        # Store the surface residues in .bept
        bept_cache_dir = os.path.join(output_dir, ".bept")
        os.makedirs(bept_cache_dir, exist_ok=True)

        output_csv_file = os.path.join(bept_cache_dir, f"{protein_id}_surface_data.csv")
        output_tabulated_file = os.path.join(
            output_dir, f"{protein_id}_surface_data.txt"
        )

        # Read the input CSV file and sum potentials
        resi_potentials = defaultdict(float)
        resi_names = {}

        with open(protein_bept_csvpath, "r") as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                resi_seq = row["Resi_Seq"]
                potential = float(row["Potential"])
                resi_potentials[resi_seq] += potential
                resi_names[resi_seq] = row["Resi"]

        # Write the output CSV file
        with open(output_csv_file, "w", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Resi", "Resi_Seq", "Resi_Potential"])
            for resi_seq, potential in resi_potentials.items():
                csvwriter.writerow([resi_names[resi_seq], resi_seq, potential])

        # Prepare data for tabulation
        table_data = [
            {
                "Resi": resi_names[resi_seq],
                "Resi_Seq": resi_seq,
                "Resi_Potential": potential,
            }
            for resi_seq, potential in resi_potentials.items()
        ]

        with open(output_tabulated_file, "w") as tabfile:
            tabfile.write(meta_data_surface(protein_file, output_csv_file) + "\n\n")

        # Write the tabulated data to a file
        with open(output_tabulated_file, "a") as tabfile:
            tabfile.write(
                tabulate(table_data, headers="keys", tablefmt="plain", showindex=False)
            )

        destination_surface_resi_path = output_tabulated_file

        CONSOLE.print(
            f"Successfully calculated surface residues for {protein_file}",
            style="green",
        )

    except Exception as e:
        CONSOLE.print(f"Error in calculating surface residues. Error: {e}", style="red")
        err_surface_calc = True

    return destination_surface_resi_path, err_surface_calc
