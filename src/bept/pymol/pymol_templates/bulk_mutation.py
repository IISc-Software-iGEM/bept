# This file is to be run in pymol, after directing into the directory where it is saved.
# This file lets you save all the morph states of the first rotamer in a mutation given the residue number and mutant 


from pymol import cmd

# Validation
def validate_mutations(lines):
    """Checks if the mutations.txt file is in correct format or not"""
    is_file_correct = True
    amino_acids = ["ALA", "ARG", "ASN", "ASP", "CYS", "GLN", "GLU", "GLY", "HIS", "ILE", "LEU", "LYS", "MET", "PHE", "PRO", "SER", "THR", "TRP", "TYR", "VAL"]

    for line_number, line in enumerate(lines):
        n, mutant = line.strip().split()
        if not n.isnumeric():
            is_file_correct = False
            print(f"Line {line_number}: n {n} is not acceptable")
        if mutant.upper() not in amino_acids:
            is_file_correct = False
            print(f"Line {line_number}: mutant '{mutant}' is not acceptable.")
        
    if not is_file_correct:
        exit(-1)

# Open the file and read the lines
with open('mutations.txt', 'r') as f:
    lines = f.readlines()
    validate_mutations(lines)

#This is the raw code from mutation.py which i modified for this file
def raw_code(chain_id: str, output_file_path: str, get_min_strain: bool):
    # Loop over the lines
    for line in lines:
        # Split the line into residue number (n) and mutant
        n, mutant = line.strip().split()
        mutant = mutant.upper()

        # Use the values in your code
        cmd.wizard("mutagenesis")
        cmd.get_wizard().set_mode(mutant)
        cmd.get_wizard().do_select(f"chain {chain_id} and resid {n}")
        # To get minimum strain, comment the next line. Else, you ll get max %
        if not get_min_strain: cmd.frame(1)
        cmd.get_wizard().apply()
        # Close wiard
        cmd.wizard(None)

        #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")
        # cmd.save(fr"C:\Users\LENOVO\Downloads\gtm-{n}-{mutant}.pdb")
        cmd.save(output_file_path + f"/gtm-{n}-{mutant}.pdb")

#This function contains the actual code for this file
def execute_pymol(protein, num, chain_id: str, output_file_path: str, get_min_strain: bool):
    # Loop over the lines
    for line in lines:
        n, mutant = line.strip().split()
        mutant = mutant.upper()
        if num == int(n):
             # Use the values in your code
            cmd.fetch(protein)
            cmd.wizard("mutagenesis")
            cmd.get_wizard().set_mode(mutant)
            cmd.get_wizard().do_select(f"chain {chain_id} and resid {n}")
            # To get minimum strain, comment the next line. Else, you ll get max %
            if not get_min_strain: cmd.frame(1)
            cmd.get_wizard().apply()
            # Close wiard
            cmd.wizard(None)

            #Name the mutation
            old_name = protein
            new_name = protein + '2'
            cmd.set_name(old_name, new_name)

            #Fetch normal protein
            cmd.fetch(protein)

            # Align the structures
            cmd.align(old_name, new_name)

            # Generate the morph
            cmd.morph("morph", old_name, new_name)

            # Determine the number of states in the morph
            number_of_states = cmd.count_states("morph")

            # Save each state to a separate file
            for state in range(1, number_of_states + 1):
                filename = output_file_path + f"/{protein}/gtm-{n}-{mutant}/gtm-{n}-{mutant}-{state}.pdb"
                cmd.save(filename, "morph", state)
            

            #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")

#change the residue number here          
execute_pymol('7y6i', 475)
