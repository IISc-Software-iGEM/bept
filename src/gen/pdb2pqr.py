
#easy way to get pdb2pqr on CLI
import time, os
from beaupy import confirm, prompt, select, select_multiple
#from beaupy.spinners import *
from rich.console import Console


def inter_pqr_gen(input_pdb:str):
    """
    This is an interactive pdb2pqr command generation with input pdb, making it easy to use & giving it a webserver feeling.
    Args:
        input_pdb: The file path to the input pdb file.

    Output:
        command to execute
    """
    console = Console()
    #making the cl prompt
    result = ['pdb2pqr']

    def get_file_path(attr=""):
        file_path = prompt(f'Enter the path to your {attr} file', target_type=str)  
        while not os.path.exists(file_path):
            console.print("The path you entered does not exist")
            file_path = prompt(f'Enter the path to your {attr} file', target_type=str)     
        return file_path
  
    #pKa Options
    if confirm("Would you like to use PROPKA to assign protonation states at provided pH?"):
        #get pH from user
        pH = prompt('Input pH value in float (Default value = 7.0):', target_type=float, validator=lambda count: count > 0 and count < 14)
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
        console.print("Input the Forcefield file")
        ff_path = get_file_path("force field")
        user_forcefield_str = f"--userff={ff_path}"
        result.append(user_forcefield_str)

        console.print("Input the Names file")
        n_path = get_file_path()
        user_names_str = f"--usernames={n_path}"
        result.append(user_names_str)
        
    
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
        parse_options = {
            "Make the protein's N-terminus neutral" : "--neutraln",
            "Make the protein's C-terminus neutral" : "--neutralc",
            "Skip, choose None" : "",
        }
    
        # Choose multiple options from a list
        items1 = select_multiple(list(parse_options.keys()), tick_character='*', ticked_indices=[0], maximal_count=len(parse_options))
    
        for key, value in parse_options.items():
            if key in items1:
                result.append(value)
    
    #Additional Options
    console.print("Additional Options. Recommended Options (**) ")
    
    add_options = ["Ensure that new atoms are not rebuilt too close to existing atoms",
                   "Optimize the hydrogen bonding network",
                   "Assign charges to the ligand specified in a MOL2 file",
                   "Create an APBS input file **",
                   "Add/keep chain IDs in the PQR file **",
                   "Insert whitespaces between atom name and residue name, between x and y, and between y and z **",
                   "Remove the waters from the output file"]
    
    values = ["--nodebump",
              "--noopt",
              "--ligand=",
              "--apbs-input=",
              "--keep-chain",
              "--whitespace",
              "--drop-water"]
    
    # Choose multiple options from a list
    items2 = select_multiple(add_options, tick_character='*', ticked_indices=[0], maximal_count=len(add_options))
    
    for i in range(len(add_options)):
        if i <= 1:
            if add_options[i] not in items2:
                result.append(values[i])

        elif i == 2:
            if add_options[i] in items2:
                console.print("Input the Ligand file")
                lig_path = get_file_path()
                ligand_str = f"--ligand={lig_path}"
                result.append(ligand_str)

        elif i == 3:
            if add_options[i] in items2:
                apbs_input_file = prompt('Enter the name for your APBS input file(without .in extension)', target_type=str)
                apbs_input_file_str = f"--apbs-input={apbs_input_file}" if apbs_input_file.endswith(".in") else f"--apbs-input={apbs_input_file}.in" 
                result.append(apbs_input_file_str)

        else: 
            if add_options[i] in items2:
                result.append(values[i])
                    
    #Adding input pdb file and the output pqr file to the cl prompt
    result.append(input_pdb)
    #Output pqr has the same name as input pdb
    output_pqr = input_pdb[:-3] + 'pqr'
    result.append(output_pqr)
    
    #pdb2pqr command generation
    final_cmd = " ".join(result)
    return final_cmd 
