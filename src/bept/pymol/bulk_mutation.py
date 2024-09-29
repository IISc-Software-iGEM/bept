# This file is to be run in pymol, after directing into the directory where it is saved.
# This file lets you save all the morph states of the first rotamer in a mutation given the residue number and mutant 


from pymol import cmd

# Open the file and read the lines
with open('mutations.txt', 'r') as f:
    lines = f.readlines()

#This is the raw code from mutation.py which i modified for this file
def everything():
    # Loop over the lines
    for line in lines:
        # Split the line into residue number (n) and mutant
        n, mutant = line.strip().split()

        # Use the values in your code
        cmd.wizard("mutagenesis")
        cmd.get_wizard().set_mode(mutant)
        cmd.get_wizard().do_select(f"chain A and resid {n}")
        # To get minimum strain, comment the next line. Else, you ll get max %
        cmd.frame(1)
        cmd.get_wizard().apply()
        # Close wiard
        cmd.wizard(None)

        #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")
        cmd.save(fr"C:\Users\LENOVO\Downloads\gtm-{n}-{mutant}.pdb")

#This function contains the actual code for this file
def perMutant(protein, num):
    # Loop over the lines
    for line in lines:
        n, mutant = line.strip().split()
        if num == int(n):
             # Use the values in your code
            cmd.fetch(protein)
            cmd.wizard("mutagenesis")
            cmd.get_wizard().set_mode(mutant)
            cmd.get_wizard().do_select(f"chain A and resid {n}")
            # To get minimum strain, comment the next line. Else, you ll get max %
            cmd.frame(1)
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
                filename = fr"C:\Users\LENOVO\Code\forks\Ion-Channel-NCC\mutation_morphs\{protein}\gtm-{n}-{mutant}\gtm-{n}-{mutant}-{state}.pdb"
                cmd.save(filename, "morph", state)
            

            #cmd.save(f"/Volumes/Anirudh/IISc/IGEM/gtlmn-7yg0/gtm-{n}-{mutant}.pdb")

#change the residue number here          
perMutant('7y6i', 475)
