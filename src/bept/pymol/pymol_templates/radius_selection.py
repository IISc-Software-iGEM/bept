## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd
import os


def radial_residue(
    pdb_file: str,
    atom: str,
    output_path: str = os.path.join(os.getcwd(), "radial_residues.txt"),
    fetch: bool = True,
    chain_id: str = "A",
    radius: float = 10,
):
    # Load the pdb file
    if fetch:
        pdb_file = os.path.basename(pdb_file).split(".")[
            0
        ]  # Get the name of the pdb file
        cmd.fetch(pdb_file)
    else:
        cmd.load(pdb_file)

    # Naming the selection of Na atoms
    cmd.select(f"{atom}_atoms", f"name {atom}")

    # Selecting the residues with 'within' command
    # The number after 'within' is the radius in Angstrom
    cmd.select("radial_residues", f"chain {chain_id} within {radius} of Na_atoms")

    # Printing the residue names & number of residues
    radial_residues = []
    cmd.iterate("radial_residues", "radial_residues.append((resi,resn))")

    # Write to output file
    with open(output_path, "w") as f:
        f.write(f"Total residues: {len(radial_residues)}\n")
        for resi, resn in radial_residues:
            f.write(f"{resn} {resi}\n")

    print(f"Results written to {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
pdb_file = "PDB_ID_or_path_to_pdb_file"

## Set the atom name to select around which the residues are to be selected
atom = "Na"  # Example

## Set the chain ID from which residues to select from
chain_id = "A"

## Set the radius in Angstrom
radius = 10  # Default is 10 Angstrom

## Output path to write the residues to
output_path = os.path.join(os.getcwd(), "radial_residues.txt")

if __name__ == "__main__":
    residue = radial_residue(
        pdb_file=pdb_file, atom=atom, fetch=fetch, chain_id=chain_id, radius=radius
    )
