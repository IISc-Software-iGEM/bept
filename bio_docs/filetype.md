# A brief introduction to several file types

In computational biology, various files are used to represent data for biomolecules like proteins, lipids, DNA, etc. These files contain different types of information such as atomic coordinates, molecular structures, and other relevant data. Here are some common file types used in computational biology and bioinformatics -

## PDB Files

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

### Example

---

ATOM 1 N MET A 1 38.292 13.351 7.926 1.00 20.00 N

ATOM 2 CA MET A 1 37.905 12.048 8.510 1.00 20.00 C

Here, each line represents an atom, with columns specifying the atom number, atom type, residue name, chain identifier, and atomic coordinates.

---

## Advantages of PDB file

- **Standardised format:** PDB is a widely accepted and standardized file format, making it easy to share and exchange structural data.

- **Large Database:** The Protein Data Bank (PDB) contains over 175,000 experimentally determined 3D structures, providing a wealth of structural information.

- **Visualization Tools:** PDB files are compatible with numerous visualization and analysis tools, making it easy to explore protein structures.

## PQR Files

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

## XYZ Files

1. The first line of a frame specifies the number of particles (N) in the frame. It is an integer number. No other text is allowed on this line.

2. The second line is a comment line. A comment may be placed here or the line may be left blank. This line is igored by the program.

3. There are then N lines, each of which describes the coordinates of a single particle. These lines consist of the identity of a particle followed by 3 spatial coordinates. No other text may be included in this line.

4. The identity of a particle is specified by a single letter or number. The coordinates are given as floating point numbers. Each of these elements is separated by either a single space or single tab-space.

5. If there are multiple timesteps then each timestep is appended directly after the last. It is not required that any quantities are conserved between timesteps (number of particles, particle identities etc.), each timestep is treated separately. It is not required to label or otherwise number frames although this is a good use of the comment line.

## PDB vs PQR

PDB and PQR files both are important. However here are some key differences between them. Their functionalities make them suitable to different situations.

## PDB (Protein Data Bank) File

- **Purpose:** PDB files are used to store three-dimensional structures of biological molecules, like proteins, nucleic acids, and complex assemblies. These files are a standard format for representing molecular structures in the field.

- **Format:** A PDB file contains detailed information about the atoms in a molecule, including their coordinates, element types, and bonds. It also includes metadata such as the molecule's name, authors, and experimental conditions.

- **Usage:** These files are widely used in molecular visualization tools and software for analyzing and simulating biomolecules

## PQR File

- **Purpose:** PQR files are similar to PDB files but include additional information, specifically atomic charge and radius data. The "PQR" name comes from the combination of "PDB", "Q" for charge, and "R" for radius.

- **Format:** The format is almost identical to the PDB format, but with additional columns for partial charges and atomic radii.
- **Usage:** PQR files are often used in electrostatics calculations, particularly with software like APBS (Adaptive Poisson-Boltzmann Solver) to determine the electrostatic potential of biomolecules.

### Example

---

ATOM 1 N MET A 1 38.292 13.351 7.926 1.00 20.00 -0.3 1.85

ATOM 2 CA MET A 1 37.905 12.048 8.510 1.00 20.00 0.21 1.70

Here, the additional columns at the end represent the partial charge and atomic radius.

---

## Key Reasons Why PQR Files Are Useful for Electrostatic Calculations:

### 1. Inclusion of Partial Charges:

- **Electrostatic Interactions:** The electrostatic potential of a molecule depends on the distribution of charges across its atoms. PQR files include partial charges for each atom, which are necessary to calculate how the molecule interacts with electric fields, solvents, and other molecules.

- **Electrostatic Potential Maps:** Tools like APBS (Adaptive Poisson-Boltzmann Solver) use these partial charges to compute electrostatic potential maps, which are crucial for understanding molecular interactions, binding sites, and reactivity.

### 2. Atomic Radii:

- **Solvent Accessibility:** The atomic radii in PQR files are used to model how molecules interact with their environment, particularly with solvents. The radii help determine the solvent-accessible surface area, which influences the molecule's electrostatic properties.

- **Poisson-Boltzmann Equation:** When solving the Poisson-Boltzmann equation (a key equation in electrostatics), the atomic radii are used to define the dielectric boundary between the molecule and its surrounding environment. This boundary is crucial for accurate calculations of the electrostatic potential.
