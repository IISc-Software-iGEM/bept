## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd
import os


def create_colored_surface(
    protein: str,
    output_path: str = os.path.join(os.getcwd(), "surface_protein.png"),
    fetch: bool = True,
):
    """
    Creates a surface representation of the protein and colors it by electrostatic potential.
    Args:
        protein: Path to the protein file (PDB format)
        output_path: Path where the surface image will be saved
        fetch: Boolean flag to indicate whether to fetch the
    """

    # Load the protein
    if fetch:
        cmd.fetch(protein)
    else:
        cmd.load(protein, "protein")

    # Show the surface
    cmd.show("surface", "protein")

    # Color the surface by electrostatic potential
    cmd.color("electrostatic", "protein")

    # Save the view as an image
    cmd.png(output_path)

    # Cleanup
    cmd.delete("protein")

    print(f"Surface image saved to: {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

## Output path to write the surface image to
output_path = os.path.join(os.getcwd(), "surface_protein.png")

if __name__ == "__main__":
    create_colored_surface(
        protein=protein,
        output_path=output_path,
        fetch=fetch,
    )
