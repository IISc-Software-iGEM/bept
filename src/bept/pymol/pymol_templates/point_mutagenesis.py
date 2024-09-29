## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

import os
from pymol import cmd

amino_acids = [
    "ALA",
    "ARG",
    "ASN",
    "ASP",
    "CYS",
    "GLN",
    "GLU",
    "GLY",
    "HIS",
    "ILE",
    "LEU",
    "LYS",
    "MET",
    "PHE",
    "PRO",
    "SER",
    "THR",
    "TRP",
    "TYR",
    "VAL",
]


def mutate_protein(
    protein: str,
    residue_number: int,
    new_residue: str,
    fetch: bool = True,
    chain: str = "A",
    output_path: str = os.path.join(os.getcwd(), "mutated_protein.pdb"),
):
    """
    Performs a mutagenesis on the protein structure, replacing an amino acid at a given position.

    Args:
        protein: Path to the protein file (PDB format)
        residue_number: The residue number to mutate (e.g., 45)
        new_residue: The new amino acid (3-letter code, e.g., 'ALA' for alanine)
        fetch: Whether to fetch the protein structure using PyMOL
        chain: The chain ID where the residue is located (e.g., 'A')
        output_path: Path where the mutated structure will be saved
    """

    # Load the protein structure
    if fetch:
        cmd.fetch(protein)
    else:
        cmd.load(protein, "protein")

    # Use the mutagenesis wizard
    cmd.wizard("mutagenesis")

    # Select the residue to mutate
    cmd.get_wizard().do_select(f"chain {chain} and resid {residue_number}")

    # Set the new residue type
    cmd.get_wizard().set_mode(new_residue)

    # Apply the mutation
    cmd.get_wizard().apply()

    # Save the mutated structure
    cmd.save(output_path)

    # Cleanup
    cmd.set_wizard()  # Turn off the mutagenesis wizard
    cmd.delete("protein")

    print(f"Mutated protein saved to: {output_path}")


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

## Output path to write the aligned protein to
output_path = os.path.join(os.getcwd(), "mutated_protein_protein.pdb")  # Default

## Mutation details
residue_number = 1  # Residue number to mutate
new_residue = "ALA"  # New amino acid (3-letter code)
chain = "A"  # Chain ID where the residue is located

if __name__ == "__main__":
    if new_residue.upper() not in amino_acids:
        print(f"Invalid amino acid: {new_residue}")
        exit(-1)

    mutate_protein(
        protein=protein,
        residue_number=residue_number,
        new_residue=new_residue,
        fetch=fetch,
        chain=chain,
        output_path=output_path,
    )
