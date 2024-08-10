
#easy way to get pdb2pqr on CLI
import time
from beaupy import confirm, prompt, select, select_multiple
#from beaupy.spinners import *
from rich.console import Console

console = Console()
#making the cl prompt
result = ['pdb2pqr']


#pKa Options
if confirm("Would you like to use PROPKA to assign protonation states at provided pH?"):
    #get pH from user
    pH = prompt('pH value?', target_type=float, validator=lambda count: count > 0 and count < 14)
    #making the cl prompt
    pH_str = f"--titration-state-method=propka --with-ph={pH}"
    result.append(pH_str)


#forcefield options
forcefields = [
        "AMBER",
        "SCHARM",
        "PEOEPB",
        "PARSE",
        "SWANSON",
        "TYLO6",
        "[red]User-defined Forcefield[/red]"
    ]
console.print("Please choose a forcefield to use:")
# Choose one item from a list
forcefield = select(forcefields, cursor="🢧", cursor_style="cyan")
#making the cl prompt
if forcefield != "[red]User-defined Forcefield[/red]":
    forcefield_str = f"--ff={forcefield}"
    result.append(forcefield_str)
    
else:
    pass #still have to do something



#output naming scheme options
naming_schemes = [
        "AMBER",
        "SCHARM",
        "PEOEPB",
        "PARSE",
        "SWANSON",
        "TYLO6",
        "[red]Internal naming scheme[/red]"
    ]
console.print("Please choose an output naming scheme to use:")
# Choose one item from a list
naming_scheme = select(naming_schemes, cursor="🢧", cursor_style="cyan")
#making the cl prompt
if naming_scheme != "[red]Internal naming scheme[/red]":
    naming_scheme_str = f"--ffout={naming_scheme}"
    result.append(naming_scheme_str)

    
#Additional Options
if not confirm("Ensure that new atoms are not rebuilt too close to existing atoms"):
    #making the cl prompt
    result.append(f"--nodebump")

if not confirm("Optimize the hydrogen bonding network"):
    #making the cl prompt
    result.append(f"--noopt")

if confirm("Assign charges to the ligand specified in a MOL2 file"):
    #Need to somehow get the ligand file from user
    ligand_file = None
    #making the cl prompt
    result.append(f"--ligand={ligand_file}")

if confirm("Create an APBS input file"):
    apbs_input_filename = prompt('Enter the name for your APBS input file:', target_type=str, validator=lambda string: len(string) < 20 )
    #making the cl prompt
    result.append(f"--ligand={apbs_input_filename}")

if confirm("Add/keep chain IDs in the PQR file"):
    #making the cl prompt
    result.append(f"--keep-chain")

if confirm("Insert whitespaces between atom name and residue name, between x and y, and between y and z"):
    #making the cl prompt
    result.append(f"--whitespace")

if forcefield == 'PARSE':
    if confirm("Make the protein's N-terminus neutral"):
        #making the cl prompt
        result.append(f"--neutraln")

    if confirm("Make the protein's C-terminus neutral"):
        #making the cl prompt
        result.append(f"--neutralc")

if confirm("Remove the waters from the output file"):
        #making the cl prompt
        result.append(f"--drop-water")

#pdb2pqr command generation
cl = " ".join(result)
print(cl)



