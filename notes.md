# layout of the tool.

## Flags

## Meta Options

- `--help` : Display help message
- `--version` : Display version of the tool

## Commands

### gen for Generate

Note the order of the below matters a lot

- -p : pdb2pqr, req args: input PDB FILE, output file name
- -a : apbs, req args: INPUT FILE
- -i : interactive, req args: None

### auto for Automation

- -p : pdb2pqr, req args: input PDB FILE, output file name
- -a : apbs, req args: INPUT FILE
- -c : command history load, that will be run, with file name, output name as mentioned in -p and -a flag.
- -f : file load, whith each line as file names. Outputs will be ran for each line.

### out for Output files

Here i would wanna produce all types files at once.
