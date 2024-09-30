import os
import csv
from collections import defaultdict
from tabulate import tabulate

from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley


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


def calc_sasa(protein_file: str):
    """
    Args:
    protein_file: the pdb id of protein(without the .pdb)

    Output:
    SASA: The solvent accessible surface area
    """
    struct, _ = biop_fetch(protein_file)
    sr = ShrakeRupley()
    sr.compute(struct, level="S")
    return round(struct.sasa, 2)


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
    # Store the surface residues in .bept
    bept_cache_dir = os.path.join(output_dir, ".bept")
    os.makedirs(bept_cache_dir, exist_ok=True)

    output_csv_file = os.path.join(bept_cache_dir, f"{protein_file}_surface_data.csv")
    output_tabulated_file = os.path.join(output_dir, f"{protein_file}_surface_data.txt")

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

    # Write the tabulated data to a file
    with open(output_tabulated_file, "w") as tabfile:
        tabfile.write(
            tabulate(table_data, headers="keys", tablefmt="plain", showindex=False)
        )
