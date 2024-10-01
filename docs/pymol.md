# Pymol and BEPT

PyMol is a powerful tool for visualizing proteins and their electrostatics. PyMol provides Python API's to allow automation of its functions through simple python scripts. These maybe confusing and hard to use in the beginning. Hence, BEPT provides PyMol python pre-made template codes for various functionalities as mentioned in the next section. You can use these templates to automate your work in PyMol.

## PyMol Templates

Here is wide list of operations you can perform in PyMol using BEPT provided templates -

1. Morphing Two Proteins - This function morphs two proteins. The code template file name is "morphing_two_proteins.py".
2. Aligning Two Proteins - This function aligns two proteins. The code template file name is "aligning_two_proteins.py".
3. Superimposing Two Proteins - This function superimposes two proteins. The code template file name is "superimpose_two_proteins.py".
4. Mutagenesis - This function performs point mutagenesis. The code template file name is "point_mutagenesis.py".
5. Bulk Mutagenesis - This function performs bulk mutagenesis. The code template file name is "bulk_mutagenesis.py".
6. Selecting Residues in a Radius Around Atom - This function selects residues in a radius around an atom. The code template file name is "radius_selection.py".
7. Show Bumps - This function shows bumps in the protein structure. The code template file name is "show_bumps.py".
8. Cartoon Representation of Protein - This function creates a cartoon representation of the protein. The code template file name is "cartoon_representation.py".
9. Create and Color a Surface - This function creates and colors a surface. The code template file name is "create_color_surface.py".
10. Distance Between Two Atoms - This function calculates the distance between two atoms. The code template file name is "dist_bw_atoms.py".
11. Calculate SASA - This function calculates the solvent-accessible surface area (SASA). The code template file name is "calc_sasa.py".

## How to use the templates

These templates have a very simple structure to them. To use them, you can simply edit the option mentioned below in the code and everything will be automatically taken care of by the code. Note that we have provided comments for each line of code and if you would like to comment out any line, feel free to do so.

Here is an example of how to use the "morphing_two_proteins.py" template -

```python
# Input the following values and run the code.
## To fetch the pdb file, set fetch = True/False
fetch = True

## If fetch is False, set the path to the pdb file, else simply set PDB ID
protein1 = "protein1_PDB_ID/path_to_pdb_file"
protein2 = "protein2_PDB_ID/path_to_pdb_file"

## Output path to write the aligned protein to
output_path = os.path.join(os.getcwd(), "aligned_protein.pdb")  # Default
```

You will see the above code snippet at the bottom which can you can edit according to the comments.

## Running codes in PyMol

PyMol has it's own command line interface which can be used to run the python scripts. Traverse to the directory where the code is saved and run the below command -

```bash
run bept_template.py
```

This will run the code and perform the operation as mentioned in the template.

For any issues, feel free to raise an issue in the [GitHub repository](https://github.com/IISc-Software-iGEM/bept).
