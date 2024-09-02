# PDB vs PQR
## PDB (Protein Data Bank) File

* **Purpose:**  PDB files are used to store three-dimensional structures of biological molecules, like proteins, nucleic acids, and complex assemblies. These files are a standard format for representing molecular structures in the field.

* **Format:** A PDB file contains detailed information about the atoms in a molecule, including their coordinates, element types, and bonds. It also includes metadata such as the molecule's name, authors, and experimental conditions.

* **Usage:** These files are widely used in molecular visualization tools and software for analyzing and simulating biomolecules

### Example
____
ATOM      1  N   MET A   1      38.292  13.351   7.926  1.00 20.00           N

ATOM      2  CA  MET A   1      37.905  12.048   8.510  1.00 20.00           C

Here, each line represents an atom, with columns specifying the atom number, atom type, residue name, chain identifier, and atomic coordinates.
___

## Advantages of PDB file
* **Standardised format:** PDB is a widely accepted and standardized file format, making it easy to share and exchange structural data.

* **Large Database:** The Protein Data Bank (PDB) contains over 175,000 experimentally determined 3D structures, providing a wealth of structural information.

* V**isualization Tools:** PDB files are compatible with numerous visualization and analysis tools, making it easy to explore protein structures.

## PQR File
* **Purpose:** PQR files are similar to PDB files but include additional information, specifically atomic charge and radius data. The "PQR" name comes from the combination of "PDB", "Q" for charge, and "R" for radius.

* **Format:** The format is almost identical to the PDB format, but with additional columns for partial charges and atomic radii.
* **Usage:** PQR files are often used in electrostatics calculations, particularly with software like APBS (Adaptive Poisson-Boltzmann Solver) to determine the electrostatic potential of biomolecules.

### Example
___
ATOM      1  N   MET A   1      38.292  13.351   7.926  1.00 20.00      -0.3    1.85

ATOM      2  CA  MET A   1      37.905  12.048   8.510  1.00 20.00      0.21    1.70

Here, the additional columns at the end represent the partial charge and atomic radius.
___________



## Key Reasons Why PQR Files Are Useful for Electrostatic Calculations:

### 1. Inclusion of Partial Charges:
* **Electrostatic Interactions:** The electrostatic potential of a molecule depends on the distribution of charges across its atoms. PQR files include partial charges for each atom, which are necessary to calculate how the molecule interacts with electric fields, solvents, and other molecules. 

* **Electrostatic Potential Maps:** Tools like APBS (Adaptive Poisson-Boltzmann Solver) use these partial charges to compute electrostatic potential maps, which are crucial for understanding molecular interactions, binding sites, and reactivity.

### 2. Atomic Radii:
* **Solvent Accessibility:** The atomic radii in PQR files are used to model how molecules interact with their environment, particularly with solvents. The radii help determine the solvent-accessible surface area, which influences the molecule's electrostatic properties.

* **Poisson-Boltzmann Equation:** When solving the Poisson-Boltzmann equation (a key equation in electrostatics), the atomic radii are used to define the dielectric boundary between the molecule and its surrounding environment. This boundary is crucial for accurate calculations of the electrostatic potential.
