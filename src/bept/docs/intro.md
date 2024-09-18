# BEPT

Bept - Beginner friendly Electrostatics for Protein analysis Tool.

Bept is a beginner-friendly tool for analysis proteins which uses functionalities of `pdb2pqr` and `apbs` command line tools, but making them more beginner friendly, making it for you to learn their usages without undergoing the pain of reading the documentation. The tool is meant to target growing scientists interested in protein electrostatics but scared of using Terminal command line tool.

These documentations are meant to help you understand how to use the tool and a detailed & technical explanation how BEPT works.

## Features

- Interactively generate pdb2pqr command line and APBS `.in` input files without looking into deep documentation.
- Generate the PQR, Potential DX and BEPT special `.bept` file containing all the information you need for a protein.
- Automate the process of running PDB2PQR and APBS with optional interactive modes.
- Save your `.in` files in cache for future references.
- Save your PDB2PQR commands in history so you no need to generate it again.
- Read the docs of the tool directly from the CLI in an interactive way.
- Experience bept's extreme user-friendliness, color-coded outputs and error handling and make Electrostatics analysis a breeze!

## OS's Supported

BEPT is supported on MacOS, Linux and Windows. You can install it using `pip` or `pipx` or `uv` package manager. Check out the README in [bept](https://github.com/IISc-Software-iGEM/bept) official repository for more information.

## Why use BEPT?

BEPT is meant for young scientists who are interested in protein electrostatics but don't know where to start, getting scared from reading the docs and understanding what options to choose from. If you are one of them, BEPT is for you!

- You can also use it as alternative to APBS web server, since the whole design is based on it. So you can use it for faster results, running as many times as you want.

## Credits and Acknowledgements

BEPT is made by Team IISc Software for iGEM 2024 competition.

It is under MIT License and you can use it for free. If you like the tool, please give us a star on [GitHub](https://github.com/IISc-Software-iGEM/bept) and share it with your friends.
