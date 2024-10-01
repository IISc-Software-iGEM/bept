# BEPT

Bept - Beginner friendly Electrostatics for Protein analysis Tool.

Bept is a beginner-friendly tool for analysis proteins which uses functionalities of `pdb2pqr` and `apbs` command line tools, but making them more beginner friendly, making it for you to learn their usages without undergoing the pain of reading the documentation. The tool is meant to target growing scientists interested in protein electrostatics but scared of using Terminal command line tool.

These documentations are meant to help you understand how to use the tool and a detailed & technical explanation how BEPT works.

## Features

- Interactively generate pdb2pqr command line and APBS `.in` input files without looking into deep documentation.
- Generate the PQR, Potential DX and BEPT special `.bept` file containing all the information you need for a protein.
- Automate the process of running PDB2PQR and APBS with optional interactive modes.
- Generate data on surface residues along with calculating SASA values.
- Bept provides PyMol python pre-made template codes for various functionalities.
- Save your `.in` files in cache for future references.
- Save your PDB2PQR commands in history so you no need to generate it again.
- If you feel understanding how to write the command itself, don't worry, Bept has a friendly UI for that too.
- Read the docs of the tool directly from the CLI in an interactive way.
- Experience bept's extreme user-friendliness, color-coded outputs and error handling and make Electrostatics analysis a breeze!

## Why use BEPT?

BEPT is meant for young scientists who are interested in protein electrostatics but don't know where to start, getting scared from reading the docs and understanding what options to choose from. If you are one of them, BEPT is for you!

- You can also use it as alternative to APBS web server, since the whole design is based on it. So you can use it for faster results, running as many times as you want.

## Usage of output files

Once you have used Bept to generate the PQR, Potential DX, CUBE files and BEPT files, etc. you can use them in the following ways -

1. **BEPT file** - This file contains all the information about the protein. You can use this file for your analysis in codes and visualisation of data in text format. It is recommended to use the generated `.csv` for your workflow.

2. **PQR file** - You can use this file to visualise the protein in PyMol or VMD. You can also use this file for further analysis in other tools. It is recommeneded to use these files for faster analysis instead of PDB's since it gives you the required information at hand.

3. **Potential DX file** - This file contains the potential values at each grid points. It may be hard to understand the textual content of the file, but you can use it in Pymol to visualise the potential maps.

4. **CUBE file** - This file contains data from the Potential DX and PQR files. You can use this file to visualise the protein and the potential maps in PyMol or VMD.

5. **Surface Residues file** - Bept generates surface residues data along with SASA values. You can use this data as pwe your requirements for deeper analysis.

## OS's Supported

BEPT is supported on MacOS, Linux and Windows. You can install it using `pip` or `pipx` or `uv` package manager. Check out the README in [bept](https://github.com/IISc-Software-iGEM/bept) official repository for more information.

## Credits and Acknowledgements

BEPT is made by Team IISc Software for iGEM 2024 competition.

It is under MIT License and you can use it for free. If you like the tool, please give us a star on [GitHub](https://github.com/IISc-Software-iGEM/bept) and share it with your friends.
