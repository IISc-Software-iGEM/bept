## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

import os
from pymol import cmd


def align_proteins(
    protein1: str,
    protein2: str,
    fetch: bool = True,
    output_path: str = os.path.join(os.getcwd(), "aligned_protein.pdb"),
):
    """
    Aligns two proteins using PyMOL, saves the aligned version of protein1,
    and prints the RMSD.

    Args:
        protein1: Path to the first protein file (PDB format)
        protein2: Path to the second protein file (PDB format)
        fetch: Whether to fetch the proteins from the PDB database
        output_path: Path where the aligned protein will be saved
    """

    # Load the two protein structures
    if fetch:
        cmd.fetch(protein1, type="pdb", async_=0)
        cmd.fetch(protein2, type="pdb", async_=0)
    else:
        cmd.load(protein1, "protein1")
        cmd.load(protein2, "protein2")

    # Align protein1 to protein2
    alignment_result = cmd.align("protein1", "protein2")

    # Extract RMSD from the alignment result (it’s the first value returned)
    rmsd = alignment_result[0]
    print(f"RMSD: {rmsd} Å")

    # Save the aligned structure
    cmd.save(output_path)

    # Cleanup
    cmd.delete("protein1")
    cmd.delete("protein2")

    print(f"Aligned protein saved to: {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein1 = "protein1_PDB_ID/path_to_pdb_file"
protein2 = "protein2_PDB_ID/path_to_pdb_file"

## Output path to write the aligned protein to
output_path = os.path.join(os.getcwd(), "aligned_protein.pdb")  # Default

if __name__ == "__main__":
    align_proteins(
        protein1=protein1, protein2=protein2, fetch=fetch, output_path=output_path
    )
