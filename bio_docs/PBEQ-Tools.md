# Some more tools to look into for protein analysis

Computational Biology is a vast field with a plethora of tools available for various tasks. Here are some more tools that can be used for protein analysis and visualization.

## [PEP-Patch](https://github.com/liedllab/surface_analyses)

A tool to visualize and quantify the electrostatic potential on the protein surface in terms of surface patches, denoting separated areas of the surface with a common physical property. The tool's main uses are to generate a molecular surface, map a potential to this surface, and define patches, i.e. connected areas on the surface with all positive or all negative potential values.

---

## [MD-DaVis](https://github.com/djmaity/md-davis/tree/master)

MD DaVis is a tool for comparative analysis of molecular dynamics simulations of proteins. It provides a range of features for visualizing, analyzing, and interpreting the results of MD (Molecular Dynamics) simulations.

Some key features of the tool:

- Free Energy Landscape: Graphical representation of the potential energy of a system as a function of its configurations. It provides insights into the stability and dynamics of molecular systems.

- Residue Properties Plot: Information about various properties of individual residues within a protein or other biomolecule.

- Surface Electrostatics: Mapping the electrostatic potential on surface of molecule (uses colour coded maps for positive and negative charges).
- H-bond/Contact Matrix: Tool for analyzing hydrogen bonds and other types of contacts within a biomolecule.

---

## [DelPhi](http://compbio.clemson.edu/sapp/delphi_webserver/)

DelPhi webserver is a Poisson-Boltzmann solver for calculating electrostatic energies and potential in biological macromolecules. It was originally developed in Dr. Barry Honig's lab and currently being maintained by Delphi Development team. It utilizes a finite difference method to solve the Poisson-Boltzmann equation for biomolecules and objects within a given system.

Key Points:

- Electrostatic Potential Calculation: Calculates the electrostatic potential of a biomolecular system.

- Solvent Accessibility: It can compute the electrostatic potential on the surface of the molecule. This helps in visualizing how the charge distribution affects molecular interactions.

- Support for Multiple Types of Biomolecules: It can represent proteins, nucleic acids, peptides, complexes, etc making it versatile tool.
- Interactive Visualization: This helps in understanding the distribution of electrostatic potential.

---

## [PDB2PQR](https://pdb2pqr.readthedocs.io/en/latest/)

This software automates many of the common tasks of preparing structures for continuum solvation calculations as well as many other types of biomolecular structure modeling, analysis, and simulation. PDB2PQR helps to bridge the gap between protein structure data and electrostatic modeling, making it easier to analyze the electrostatic interactions and properties of proteins. These tasks include:

- Charge and Radii Addition

- Formation of PQR files
- Handling Protonation States
- Interface with Electrostatics Tools

This softwares is intended to broaden the accessibility of biomolecular solvation and electrostatics analyses to the biomedical community.

---

## [APBS](https://www.poissonboltzmann.org/)

Adaptive Poisson-Boltzmann Solver solves the equations of continuum electrostatics for large biomolecular assemblages. This software was designed from the ground up using modern design principles.

It adapts its search strategy on basis of previous events and dynamically adjuts its process. It can be tailored to different problems and constraints making it a very versatile tool.

APBS code is accompanied by extensive documentation for both users and programmers and its open-source license ensures its accessibility to the entire biomedical community.

The pdb2pqr tool was developed by the same team to automate many of the tasks associated with continuum solvation calculations. Our code uses APBS and pdb2pqr internally for doing electrostatic calculations.

---

## [PBEQ-Solver](https://charmm-gui.org/?doc=input/pbeqsolver)

The PBEQ-Solver like other tools helps solve Poisson-Boltzmann Equation (PBE), which models electrostatic interactions of biomolecules in ionic solutions.

Key Features:

- Electrostatic Potential Calculation: The main objective of PBEQ-Solver is to determine the electrostatic potential surrounding biomolecules in an ionic solution.

- Molecular Surface Mapping: This technique measures the electrostatic potential of a molecule's surface to help in the analysis of various interactions such as hydrophobic effects, ionic interactions, and hydrogen bonding.

- Addressing Irregular Geometries: The surfaces of biological molecules are complex and irregular. These geometries are well handled by the tool, enabling accurate electrostatic calculations even in complex biomolecular structures.

- Use in Biomolecular Simulations: The tool integrates well with molecular dynamics simulations. It computes the electrostatic component of molecular interactions.

---

## [Bluues](http://protein.bio.unipd.it/bluues/)

It is part of the broader GROMACS molecular dynamics suite and enables highly accurate predictions of electrostatic interactions in biomolecules.

Features:

- Born Radii Calculations: Represents the effective size of an atom or a group of atoms in a solvent. They are computed to help describe how each atom in a molecule interacts in the solvent.

- Solvation Electrostatic Free Energy Calculations: The energy change associated with transferring a biomolecule from a vacuum into a solvent.

- Electrostatic Forces Calculation: The tool computes the electrostatic forces acting on atoms within a biomolecule by deriving them from the electrostatic potential.

---

## [AESOP](https://aesop.readthedocs.io/en/latest/)

No, it isn't the ancient Greek storyteller who is famous for his collection of fables but rather is a python library to investigate electrostatics in protein interactions.

It is developed and maintained by members of the Biomolecular Modeling and Design Lab at the University of California, Riverside

It uses multiple tools like APBS, PDB2PQR, ProDy, and Modeller. AESOP is the only platform focused on protein electrostatics and offers multiple computational methods for both family-based and single-structure based analyses.

The three computational methods it supports are:

- Alascan
- DirectedMutagenesis
- ElecSimilarity.

It has various features like alanine scan, directed mutagenesis, electrostatic similarity, cross-platform, parallelized implementation, mutant generation etc.

It has great flexibility and ease in integration with other python libraries. It provides a simple interface for quantitative comparisons of electrostatic potentials generated by proteins

---

## Sources

- https://charmm-gui.org/?doc=input/pbeqsolver
- http://protein.bio.unipd.it/bluues/
- https://www.sciencedirect.com/science/article/pii/S2001037020303184#s0040
- https://www.sciencedirect.com/science/article/pii/S0006349517303922
- https://aesop.readthedocs.io/en/latest/
- https://github.com/Electrostatics/electrostatics.github.io
- https://pdb2pqr.readthedocs.io/en/latest/
- http://compbio.clemson.edu/sapp/delphi_webserver/
- https://github.com/djmaity/md-davis/tree/master
- https://github.com/liedllab/surface_analyses
