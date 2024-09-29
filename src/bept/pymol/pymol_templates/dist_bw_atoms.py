## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd


def measure_distance(
    protein: str, selection1: str, selection2: str, fetch: bool = True
):
    """
    Measures the distance between two selected atoms.
    Args:
        protein: Path to the protein file (PDB format)
        selection1: PyMOL selection for the first atom (e.g., "chain A and resi 50 and name CA")
        selection2: PyMOL selection for the second atom (e.g., "chain B and resi 100 and name CA")
        fetch: Whether to fetch the protein from the PDB database (default: True)
    """

    # Load the protein structure
    if fetch:
        cmd.fetch(protein)
    else:
        cmd.load(protein, "protein")

    # Measure the distance between the two atoms
    distance = cmd.distance("dist", selection1, selection2)
    print(f"Distance between the two atoms: {distance} Å")

    # Cleanup
    cmd.delete("protein")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

## Selections for the two atoms
selection1 = "chain A and resi 50 and name CA"  # Example selection
selection2 = "chain B and resi 100 and name CA"  # Example selection

if __name__ == "__main__":
    measure_distance(
        protein=protein,
        selection1=selection1,
        selection2=selection2,
        fetch=fetch,
    )
