## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd
import os


def superimpose_proteins(
    protein1: str,
    protein2: str,
    fetch: bool = True,
    output_path: str = os.path.join(os.getcwd(), "superimposed_protein.pdb"),
):
    """
    Superimposes two protein structures and saves the result.
    Args:
        protein1: Path to the first protein file (PDB format)
        protein2: Path to the second protein file (PDB format)
        output_path: Path where the superimposed structure will be saved
    """

    # Load the two proteins
    if fetch:
        cmd.fetch(protein1)
        cmd.fetch(protein2)
    else:
        cmd.load(protein1, "protein1")
        cmd.load(protein2, "protein2")

    # Superimpose protein1 onto protein2
    rmsd = cmd.super("protein1", "protein2")

    print(f"Superimposition RMSD: {rmsd} Å")

    # Save the superimposed version of protein1
    cmd.save(output_path)

    # Cleanup
    cmd.delete("protein1")
    cmd.delete("protein2")

    print(f"Superimposed protein saved to: {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein1 = "protein1_PDB_ID/path_to_pdb_file"
protein2 = "protein2_PDB_ID/path_to_pdb_file"

## Output path to write the superimposed protein to
output_path = os.path.join(os.getcwd(), "superimposed_protein.pdb")

if __name__ == "__main__":
    superimpose_proteins(
        protein1=protein1,
        protein2=protein2,
        fetch=fetch,
        output_path=output_path,
    )
