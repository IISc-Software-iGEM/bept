
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

#If PARSE is the forcefield
if forcefield == "PARSE":
    console.print("Options required for PARSE Forcefield")
    parse_options = {"Make the protein's N-terminus neutral" : "--neutraln",
            "Make the protein's C-terminus neutral" : "--neutralc",
            }

    # Choose multiple options from a list
    items1 = select_multiple(list(parse_options.keys()), tick_character='🎒', ticked_indices=[0], maximal_count=len(parse_options))

    for key, value in parse_options.items():
        if key in items1:
            result.append(value)

#Additional Options
console.print("Additional Options")

add_options = ["Ensure that new atoms are not rebuilt too close to existing atoms",
               "Optimize the hydrogen bonding network",
               "Assign charges to the ligand specified in a MOL2 file",
               "Enter the name for your APBS input file",
               "Add/keep chain IDs in the PQR file",
               "Insert whitespaces between atom name and residue name, between x and y, and between y and z",
               "Remove the waters from the output file"]

values = ["--nodebump",
          "--noopt",
          "",
          "",
          "--keep-chain",
          "--whitespace",
          "--drop-water"]

# Choose multiple options from a list
items2 = select_multiple(add_options, tick_character='🎒', ticked_indices=[0], maximal_count=len(add_options))

for i in range(len(add_options)):
    if i == 0 or i == 1:
        if add_options[i] not in items2:
            result.append(values[i])
    elif i == 2 or i == 3:
        #CODE TO GET INPUT FILES FROM USER
        pass
    else: 
        if add_options[i] in items2:
            result.append(values[i])


#pdb2pqr command generation
cl = " ".join(result)
print(cl)



