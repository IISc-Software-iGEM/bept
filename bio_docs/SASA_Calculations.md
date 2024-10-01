## SASA Calculations

SASA (Solvent Accessible Surface Area) represents the surface area of a biomolecule (such as a protein) that is accessible to a solvent (typically water). It is generally used in protein analysis to understand how much of a protein is exposed to the solvent, and thus, potentially available for interactions with other molecules.

The Bio.PDB.SASA module uses the “rolling ball” algorithm developed by Shrake & Rupley algorithm, which uses a sphere (of equal radius to a solvent molecule) to probe the surface of the molecule.

It takes in a PDB structure (3-D coordinates of atoms) as input.

#### We initialize the class with three parameters:

- probe_radius (float) – Radius of the probe (roughly radius of water molecule), the default value is 1.40.
- n_points (int) – Resolution of the surface of each atom, the default is taken as 100. Larger the number of points more precise are the measurements, but the time taken to do the calculations is also more.
- radii_dict (dict) – User-provided dictionary of atomic radii to use in the calculation.

The points taken simulate the surface of the atom, this is done based on atomic radii. A spherical probe (represents the solvent) is rolled over its surface to determine which points are accessible to the solvent.
The algorithm calculates the accessible surface area (SASA) by counting the points that are not obscured by neighboring atoms.

### Applications

1. Protein Structure Analysis: To determine extent of exposure of each residue, potentially correlating it with stability.

2. Mutation Studies: Analyze how mutations affect the solvent accessibility of residues, which may affect the folding or functions of the protein.

3. Drug Design: Find regions of the protein that are exposed and could be targeted by small molecules or drugs.

4. Protein-Protein Interactions: Measure how much surface area of a protein becomes inaccessible or exposed when it interacts with another protein, aiding in the study of binding interfaces.

