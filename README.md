# Improvised CLI - BEPT

Bept - Beginner friendly Electrostatics for Protein analysis Tool

Bept is a beginner-friendly tool for analysis proteins which uses functionalities of `pdb2pqr` and `apbs` command line tools, but making them more beginner friendly, making it for you to learn their usages without undergoing the pain of reading the documentation. The tool is meant to target growing scientists interested in protein electrostatics but scared of using Terminal command line tool.

Bept is cross-platform and can be installed on MacOS, Linux and Windows. It is built using Python, managed by `uv` package manager.

## Features

- Interactively generate pdb2pqr command line and APBS `.in` input files without looking into deep documentation.
- Generate the PQR, Potential DX and BEPT special `.bept` file containing all the information you need for a protein.
- Automate the process of running PDB2PQR and APBS with optional interactive modes.
- Save your `.in` files in cache for future references.
- Save your PDB2PQR commands in history so you no need to generate it again.
- Read the docs of the tool directly from the CLI in an interactive way.
- Experience bept's extreme user-friendliness, color-coded outputs and error handling and make Electrostatics analysis a breeze!

## Preview

Here is series of examples of how to use the tool:

### Interactive mode for generating PDB2PQR and APBS input files

### Generating PQR, Potential DX and BEPT files

### Automating the process of running PDB2PQR and APBS

### View the docs of the tool

## Installation

Bept is a cross-platform tool and can be installed on MacOS, Linux and Windows through below-mentioned ways -

### Using pip

You can download bept from PyPI using pip. Run the below command to install -

```bash
pip install bept
```

If you want to use it once without installing, you can use the below command -

```bash
pipx bept --help
```

If you are using `uv`, you can use-

```bash
uvx bept --help
```

### Homebrew

You can download bept from Homebrew by running the below command -

```bash
brew install anirudhg07/anirudhg07/bept
```

### Building from source

`bept` has been made using `uv` python package manager. You can install `uv` and run the below commands to install `bept` -

```bash
git clone https://github.com/IISc-Software-iGEM/bept.git
cd bept
pip install .
```

Check if the tool is successfully installed by running `bept --help` and you are good to go!

### Using Docker

## APBS and PDB2PQR

`bept` focusses on the automation of the process of running PDB2PQR and APBS. `pdb2pqr` is installed along with `bept` so you need not worry. To install APBS, you can follow the below steps -

- MacOS

```bash
sudo port install apbs
```

- Linux

```bash
sudo apt-get install apbs
```

- Windows require manual installation. Please check APBS official website for detailed information.

## More info ...

## Our Team

The project was made by members of IISc-Software Team along with the upcoming iGemers among undergraduates from IISc Bengaluru.

- Anirudh Gupta - Maintainer and Project Leader
- Aditya Thakkar - APBS interactive generation
- Kishan Gowda - APBS interactive generation
- Akshita Sunsugu Palaniswami - PDB2PQR interactive generation
- G Hasini - Software Testing
- Deeptam Bhar - Interactive documentation
- Aditey Nandan - Biological Backend and Documentation
- Ritobroto Saha - Biological Backend and Documentation
- Shreyan Priyadarshi - Biological Backend and Documentation
- Soham Paul - Biological Backend and Documentation
