# APBS
> Command: `bept gen -a input_file_path`.
> The input file path can be relative to current working diretory or absolute path, the toml files will be generated in the same directory as the input file. However, the output .in file will be generated in the current working directory.
> Use the keyboard bindings in the footer to change between tabs(i for Input, m for Misc Options, o for Output Options)/widgets(\<TAB> for next widget, <SHIFT+TAB> for previous widget).

## apbs_gen
### Interactive APBS input file generator. It runs the TnputApp.
#### Args:
- input_file_path: The path to the input file

## GLOBALS in interface file
### Vairables:
#### data: dict
- The input data which is to be used as default in the interactive app.
#### input_file_name: str
- The name of the input toml file.
#### write_commands: list
- List containing all the things checked in the Output Settings.
#### calcenergy: str
- Determines if the electrostatic energy is to be calculated for entire molecule, calculated for the entire molecule as well as energy components for each atom, or not to be calculated at all.
#### calcforce: str
- Determines if the electrostatic and apolar force is to be calculated for entire molecule, calculated for the entire molecule as well as energy components for each atom, or not to be calculated at all.
#### selected_input: str
- The calculation type to be used. Possible values are 'mg-auto', 'mg-para', 'mg-manual', 'fe-manual', and 'mg-dummy'.
#### form: str
- The format to write the Output data.
#### TAB_NAMES: list
- The list containing all the tab names.
#### possible_inputs
- The list containing all the possible inputs for the calculation-type.
#### mg_auto_def: dict
- Intitialization variable for new_data

### Functions:
#### generate_toml_file
- Generates the input toml file from the given input file and loads it into the data variable.
- Args:
    - input_file: str
        - The input file path.

### Imported Functions:
#### in_toml
- Converts the .in file to .toml file
- Args:
    - file_name: The name of the .in file
#### toml_in
- Converts the .toml file to .in file
- Args:
    - file_name: str
        - The name of the .toml file

## InputApp
### The main interactive app.

### Args:
#### input_path: The path of the input file

### Attributes:
#### new_data: dict
- The dictionary which contains the data updated by the user.
#### cgcent: list
- The list containing the values for the center of the coarse grid.
#### fgcent: list
- The list containing the values for the center of the fine grid.
#### gcent: list
- The list containing the values for the center of the grid.
#### ion: list
- The list containing information about Charge, Concentration, and Radius of ions.
#### output_item: list
- The list containing all the output items.
#### activated_tab: str
- The current active tab. Possible values are 'Input', 'Misc-Options', and 'Output-Settings'
#### CSS: str
- The stylings used for the app.
#### BINDINGS: list
- List which contains the keys associated with different actions.

### Functions:
#### compose
- Yields the child widgets of the main app.
#### on_option_highligted
- Handles the change in OptionList Widget. Triggers when the OptionList widget is changed.
#### on_select_changed
- Handles the change in Select Widget. Triggers when the Select widget is changed.
#### on_radio_set_changed
- Handles the change in RadioSet Widget. Triggers when the RadioSet widget is changed.
#### on_checkbox_changed
- Handles the change in Checkbox Widget. Triggers when the Checkbox widget is changed.
#### on_input_submit
- Handles the change in Input Widget. Triggers when the Input widget is changed.
#### action_show_tab
- Handles the change in tabs. Triggers when a tab is changed.
#### action_quit
- Triggers when the App is quit. Finishing the output toml file and converting it back to \*.in file.
#### input_activated
- Triggers when Input tab is opened.
#### misc_activated
- Triggers when Misc-Options tab is opened.
#### output_activated
- Triggers when Output-Settings tab is opened.

## Mg_auto_options
### The widget for the mg-auto calculation type.

### Attributes:
#### dime : list
- Grid Points Per Processor
#### cglen : list
- Coarse Mesh Domain Lengths
#### fglen : list
- Fine Mesh Domain Lengths
#### cgcent : list
- Center Of The Coarse Grid
#### fgcent : list
- Center Of The Fine Grid
#### pbe : str
- Type Of PBE To Be Solved
#### bcfl : str
- Boundary Condition Definition
#### pdie : str
- Biomolecular Dielectric Constant
#### sdie : str
- Dielectric Constant Of The Solvent
#### srfm : str
- Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
#### chgm : str
- Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
#### sdens : str
- Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
#### srad : str
- Radius Of The Solvent Molecules
#### swin : str
- Size Of The Support For Spline-Based Surface Definitions
#### temp : str
- Temperature For PBE Calculation (in K)

### Functions:
#### compose
- Yields the child widgets of the main app.

## Mg_para_options
### The widget for the mg-para calculation type.

### Attributes:
#### dime : list
- Grid Points Per Processor
#### pdime : list
- Processors In Parallel
#### ofrac : str
- Amount Of Overlap To Include Between The Individual Processors' Meshes
#### cglen : list
- Coarse Mesh Domain Lengths
#### fglen : list
- Fine Mesh Domain Lengths
#### cgcent : list
- Center Of The Coarse Grid
#### fgcent : list
- Center Of The Fine Grid
#### pbe : str
- Type Of PBE To Be Solved
#### bcfl : str
- Boundary Condition Definition
#### pdie : str
- Biomolecular Dielectric Constant
#### sdie : str
- Dielectric Constant Of The Solvent
#### srfm : str
- Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
#### chgm : str
- Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
#### sdens : str
- Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
#### srad : str
- Radius Of The Solvent Molecules
#### swin : str
- Size Of The Support For Spline-Based Surface Definitions
#### temp : str
- Temperature For PBE Calculation (in K)

### Functions:
#### compose
- Yields the child widgets of the main app.

## Mg_manual_options
### The widget for the mg-manual calculation type.

### Attributes:
#### dime : list
- Grid Points Per Processor
#### glen : list
- Mesh Domain Lengths
#### gcent : list
- Center Of The Grid
#### pbe : str
- Type Of PBE To Be Solved
#### bcfl : str
- Boundary Condition Definition
#### pdie : str
- Biomolecular Dielectric Constant
#### sdie : str
- Dielectric Constant Of The Solvent
#### srfm : str
- Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
#### chgm : str
- Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
#### sdens : str
- Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
#### srad : str
- Radius Of The Solvent Molecules
#### swin : str
- Size Of The Support For Spline-Based Surface Definitions
#### temp : str
- Temperature For PBE Calculation (in K)

### Functions:
#### compose
- Yields the child widgets of the main app.

## Fe_manual_options
### The widget for the fe-manual calculation type.

### Attributes:
#### pbe : str
- Type Of PBE To Be Solved
#### bcfl : str
- Boundary Condition Definition
#### pdie : str
- Biomolecular Dielectric Constant
#### sdie : str
- Dielectric Constant Of The Solvent
#### srfm : str
- Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
#### chgm : str
- Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
#### sdens : str
- Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
#### srad : str
- Radius Of The Solvent Molecules
#### swin : str
- Size Of The Support For Spline-Based Surface Definitions
#### temp : str
- Temperature For PBE Calculation (in K)

### Functions:
#### compose
- Yields the child widgets of the main app.

## Mg_dummy_options
### The widget for the mg-dummy calculation type.

### Attributes:
#### dime : list
- Grid Points Per Processor
#### cglen : list
- Coarse Mesh Domain Lengths
#### cgcent : list
- Center Of The Coarse Grid
#### pbe : str
- Type Of PBE To Be Solved
#### bcfl : str
- Boundary Condition Definition
#### pdie : str
- Biomolecular Dielectric Constant
#### sdie : str
- Dielectric Constant Of The Solvent
#### srfm : str
- Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
#### chgm : str
- Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
#### sdens : str
- Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
#### srad : str
- Radius Of The Solvent Molecules
#### swin : str
- Size Of The Support For Spline-Based Surface Definitions
#### temp : str
- Temperature For PBE Calculation (in K)

### Functions:
#### compose
- Yields the child widgets of the main app.

## Misc_options
### The widget for the mg-dummy calculation type.

### Attributes:
#### calcenergy : str
- Calculation Of Electrostatic Energy From A PBE Calculation
#### calcforce : str
- Calculation Of Electrostatic And Apolar Force Outputs From A PBE Calculation

### Functions:
#### compose
- Yields the child widgets of the main app.

## Output_options
### The widget for the mg-dummy calculation type.

### Functions:
#### compose
- Yields the child widgets of the main app.
