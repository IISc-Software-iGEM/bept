from pymol import cmd


def redial_residue(pdb_file: str, radius: float = 10)
    # Radius variable
    r = radius

    # Load the pdb file
    cmd.load(pdb_file)

    # Naming the selection of Na atoms
    cmd.select("Na_atoms", "name Na")

    # Selecting the residues with 'within' command
    # The number after 'within' is the radius in Angstrom
    cmd.select("radial_residues", f"chain A within {r} of Na_atoms")

    # Save as pdb
    # cmd.save(fr"C:\Users\LENOVO\Desktop\iGEM\Mutations\gtlmn-7y6i\gtm-{n}-{mutant}-{fnum}.pdb")

    # Printing the residue names & number of residues
    radial_residues = []
    cmd.iterate("radial_residues", "radial_residues.append((resi,resn))")
    print(len(radial_residues))
    radial_residues = tuple(set(radial_residues))  # otherwise each aa is counted 4 times
    print(len(radial_residues))
    print(radial_residues)
