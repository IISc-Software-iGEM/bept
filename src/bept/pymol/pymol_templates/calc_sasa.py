## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd


def calculate_sasa(protein: str, fetch: bool = True):
    """
    Calculates the solvent-accessible surface area (SASA) of a protein.
    Args:
        protein: Path to the protein file (PDB format)
        fetch: Whether to fetch the protein from the PDB database (default: True)
    """

    # Load the protein structure
    if fetch:
        cmd.fetch(protein)
    else:
        cmd.load(protein, "protein")

    # Calculate SASA and print the result
    cmd.set("dot_solvent", 1)  # Include solvent-accessible surface
    sasa = cmd.get_area("protein")
    print(f"SASA: {sasa} Å²")

    # Cleanup
    cmd.delete("protein")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

if __name__ == "__main__":
    calculate_sasa(
        protein=protein,
        fetch=fetch,
    )
