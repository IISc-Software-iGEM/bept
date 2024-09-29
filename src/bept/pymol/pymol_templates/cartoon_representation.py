## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd
import os


def create_cartoon_representation(
    protein: str,
    output_path: str = os.path.join(os.getcwd(), "cartoon_protein.pdb"),
    fetch: bool = True,
):
    """
    Generates a cartoon representation of the protein and saves the image.

    Args:
        protein: Path to the protein file (PDB format)
        output_path: Path where the cartoon image will be saved
        fetch: Boolean flag to indicate whether to fetch the protein structure
    """

    # Load the protein
    if fetch:
        cmd.fetch(protein)
    else:
        cmd.load(protein, "protein")

    # Show cartoon representation
    cmd.show("cartoon", "protein")

    # Color the cartoon by secondary structure
    cmd.color("cyan", "ss h")  # Helices in cyan
    cmd.color("yellow", "ss s")  # Beta-sheets in yellow

    # Save the view as an image
    cmd.png(output_path)

    # Cleanup
    cmd.delete("protein")

    print(f"Cartoon representation saved to: {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

## Output path to write the cartoon image to
output_path = os.path.join(os.getcwd(), "cartoon_protein.pdb")

if __name__ == "__main__":
    create_cartoon_representation(
        protein=protein,
        fetch=fetch,
        output_path=output_path,
    )
