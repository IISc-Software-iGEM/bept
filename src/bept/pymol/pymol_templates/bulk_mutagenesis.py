## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd
import os


# Validation
def validate_mutations(mutations_path: str):
    """Checks if the mutations.txt file is in correct format or not"""
    is_file_correct = True
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

    with open(mutations_path, "r") as f:
        lines = f.readlines()

    for line_number, line in enumerate(lines):
        if line.strip() == "":
            continue

        n, mutant, chain = line.strip().split()
        if not chain.isalpha() or len(chain) > 1:
            is_file_correct = False
            print(f"Line {line_number}: chain {chain} is not acceptable")
        if not n.isnumeric():
            is_file_correct = False
            print(f"Line {line_number}: n {n} is not acceptable")
        if mutant.upper() not in amino_acids:
            is_file_correct = False
            print(f"Line {line_number}: mutant '{mutant}' is not acceptable.")

    if not is_file_correct:
        print("Please correct the mutations file.")

    return is_file_correct


def mutate_func(chain: str, residue_number: int, new_residue: str):
    cmd.wizard("mutagenesis")

    # Select the residue to mutate
    cmd.get_wizard().do_select(f"chain {chain} and resid {residue_number}")

    # Set the new residue type
    cmd.get_wizard().set_mode(new_residue)

    # Apply the mutation
    cmd.get_wizard().apply()


def mutate_protein(
    protein: str,
    mutations_path: str,
    fetch: bool = True,
    separate_mutations: bool = True,
    output_dir: str = os.getcwd(),
):
    """
    Performs a mutagenesis on the protein structure for each mutation in the mutations file separately or together.

    Args:
        protein: Path to the protein file (PDB format)
        fetch: Whether to fetch the protein structure using PyMOL
        output_path: Path where the mutated structure will be saved
        mutations_path: Path to the mutations file
        separate_mutations: Whether to apply each mutation
    """

    # Read the mutations file
    with open(mutations_path, "r") as f:
        lines = f.readlines()

    if separate_mutations:
        # Load the protein structure
        if fetch:
            cmd.fetch(protein)
        else:
            cmd.load(protein, "protein")

        for line in lines:
            if line.strip() == "":
                continue
            residue_number, new_residue, chain = line.strip().split()
            mutate_func(chain, int(residue_number), new_residue)

            # Save the mutated structure
            cmd.save(
                output_dir, "protein_" + residue_number + "_" + new_residue + ".pdb"
            )
            # Cleanup
            cmd.set_wizard()

    else:
        # Load the protein structure
        if fetch:
            cmd.fetch(protein)
        else:
            cmd.load(protein, "protein")

        for line in lines:
            if line.strip() == "":
                continue
            residue_number, new_residue, chain = line.strip().split()
            mutate_func(chain, int(residue_number), new_residue)

        # Save the mutated structure
        cmd.save(os.path.join(output_dir, "mutated_protein.pdb"))

        # Cleanup
        cmd.set_wizard()


# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein = "protein_PDB_ID/path_to_pdb_file"

## Seperate mutations or ALL mutations to a single protein(not recommended for a protein with multiple mutations)
separate_mutations = True

## Output path to write the aligned protein to
output_dir = os.getcwd()

## Mutation details
mutations_path = "mutations.txt"  # Path to the mutations file

if __name__ == "__main__":
    if not validate_mutations(mutations_path):
        exit(-1)

    mutate_protein(
        protein=protein,
        mutations_path=mutations_path,
        separate_mutations=separate_mutations,
        fetch=fetch,
        output_dir=output_dir,
    )
