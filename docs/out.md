# Output files (out)

The `out` command is meant for writing output files. Bept provides two default output files which are always outputted. These are `.bept` and a `{NAME}_bept.csv` file which consists of ALL the information about each atom present in the structure.

The `out` command inputs two files COMPULSARILY which are `.pqr` and `.dx` file of the protein structure which you can obtain with the help of other COMMANDS of bept.

You can run the `out` command by running the following command in the terminal -

```bash
bept out -d /path/to/pqr_file /path/to/dx_file
```

To see the help message, you can run `bept out --help` in your terminal.

## Format of `{protein}_bept.csv`

The data extracted from PQR file, apbs potential dx file is taken and mapped to each of the atom present in the PQR file. This data is now written to a `.csv` file making it easier for the user to use the data for the future. Here are the following columns present in the `.csv` file -

1. `Type` - Denoting ATOM, HETATM, etc.
2. `Num` - The serial number of atom from top as present in PQR file.
3. `Atom` - The name of the atom, based on nomenclature provided by PQR file.
4. `Resi` - The residue to which the atom belongs.
5. `Chain` - The chain to which the residue belongs.
6. `Cx` - The x-coordinate of the atom in the grid w.r.t origin.
7. `Cy` - The y-coordinate of the atom in the grid w.r.t origin.
8. `Cz` - The z-coordinate of the atom in the grid w.r.t origin.
9. `Q` - The estimated charge of the atom.
10. `R` - The radius of the atom.
11. `X` - The grid position of the atom in x-direction w.r.t (0,0,0). Always integer.
12. `Y` - The grid position of the atom in y-direction w.r.t (0,0,0). Always integer.
13. `Z` - The grid position of the atom in z-direction w.r.t (0,0,0). Always integer.
14. `Ex` - The electric field in x-direction at the atom.
15. `Ey` - The electric field in y-direction at the atom.
16. `Ez` - The electric field in z-direction at the atom.
17. `Potential` - The potential value of the atom.

You can use this data for further analysis or for plotting graphs.

## Format of `.bept`

The `.bept` file is a simple text file which contains a HEADER containing some metadata which are -

1. Protein Structure Name - Path of input PDB file.
2. The origin coordinates of the structure - Extracted from the PDB file.
3. Grid size(x, y, z) of structure - which encloses the protein structure.
4. Grid length of the box (cx, cy, cz) - The length of 1 unit along (x, y, z) respectively.
5. The paths of reference PQR and Potential DX file inputted.

The `.bept` file is simply a tabulated neat looking representation of the `.csv` file.

## Other output file types

Bept currently supports production of the following file types other than mentioned above -

1. `.xyz` - File containing the coordinates of the atoms in the structure.

You can interactively select which file types to generate by using the interactive or `-i` flag as follows -

```bash
bept out -d /path/to/pqr_file /path/to/dx_file -i
```

To generate all supported files, use the `-all | --all-types` flag for the same.

```bash
bept out -d /path/to/pqr_file /path/to/dx_file -a
```

You can also specify the output path of the files by using the `-o` flag as follows -

```bash
bept out -d /path/to/pqr_file /path/to/dx_file -o /path/to/output/directory
```

The output files will be generated in the specified directory, please do not provide a file name for output path.
