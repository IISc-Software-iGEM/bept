# PDB Files

1. ATOM
    - atomic coordinate record containing the x,y,z orthogonal Angstrom coordinates for atoms in standard residues (amino acids and nucleic acids).

2. HETATM
    - atomic coordinate record containing the x,y,z orthogonal Angstrom coordinates for atoms in nonstandard residues. Nonstandard residues include inhibitors, cofactors, ions, and solvent. The only functional difference from ATOM records is that HETATM residues are by default not connected to other residues. Note that water residues should be in HETATM records.

3. TER
    - indicates the end of a chain of residues. For example, a hemoglobin molecule consists of four subunit chains which are not connected. TER indicates the end of a chain and prevents the display of a connection to the next chain.

4. SSBOND
    - defines disulfide bond linkages between cysteine residues.

5. HELIX
    - indicates the location and type (right-handed alpha, etc.) of helices. One record per helix.

6. SHEET
    - indicates the location, sense (anti-parallel, etc.) and registration with respect to the previous strand in the sheet (if any) of each strand in the model. One record per strand.

# PQR Files

Format:-
> Field_name Atom_number Atom_name Residue_name Chain_ID Residue_number X Y Z Charge Radius

1. Field_name
    - A string which specifies the type of PQR entry and should either be ATOM or HETATM in order to be parsed by APBS.

2. Atom_number
    - An integer which provides the atom index.

3. Atom_name
    - A string which provides the atom name.

4. Residue_name
    - A string which provides the residue name.

5. Chain_ID
    - An optional string which provides the chain ID of the atom. Note that chain ID support is a new feature of APBS 0.5.0 and later versions.

6. Residue_number
    - An integer which provides the residue index.

7. X Y Z
    - 3 floats which provide the atomic coordinates (in Å)

8. CHarge
    - A float which provides the atomic charge (in electrons).

9. Radius
    - A float which provides the atomic radius (in Å).

> Clearly, this format can deviate wildly from PDB due to the use of whitespaces rather than specific column widths and alignments. This deviation can be particularly significant when large coordinate values are used. However, in order to maintain compatibility with most molecular graphics programs, the PDB2PQR program and the utilities provided with APBS attempt to preserve the PDB format as much as possible.

# XYZ Files

1. The first line of a frame specifies the number of particles (N) in the frame. It is an integer number. No other text is allowed on this line.

2. The second line is a comment line. A comment may be placed here or the line may be left blank. This line is igored by the program.

3. There are then N lines, each of which describes the coordinates of a single particle. These lines consist of the identity of a particle followed by 3 spatial coordinates. No other text may be included in this line.

4. The identity of a particle is specified by a single letter or number. The coordinates are given as floating point numbers. Each of these elements is separated by either a single space or single tab-space.

5. If there are multiple timesteps then each timestep is appended directly after the last. It is not required that any quantities are conserved between timesteps (number of particles, particle identities etc.), each timestep is treated separately. It is not required to label or otherwise number frames although this is a good use of the comment line.

