# AMBER Force Field
AMBER (Assisted Model Building with Energy Refinement) is the collected name for a number of programs which conducts molecular dynamics simulations.  
It can model many biomolecules like protein, nucleic acids, lipids, carbohydrates etc. 

### What AMBER Does:

A mathematical equation represents the form of AMBER, described below:

- Represents bond covalent bond energies.
- Energy due to position of electron orbitals.
- Accounts for torsional strain.
- Represents Van-der Waal and electrostatic energies.

### Representation of Atoms
It employs an all-atom model, that is, all atoms are explicitly represented. (Hydrogen not mentioned seperately)

### Parameter Sets:

To use AMBER, you need to provide various parameters like bond length, bond angles, charges, equilibrium bond length etc. Each parameter set is defined by an OFF or PREP file.

### Force Field:

- Bond stretching and angle bending are modelled as harmonic potential (1/2 * k (x - x<sub>o</sub>)<sup>2</sup>).
- Dihedral angles (torsional strain) is modelled by periodic potential (mathematical model contains potential energy, amplitude etc. as parameters)
- Electrostatic (Coulomb’s law) and Van der Waals (Lennard-Jones Potential)

### Recommended Force Fields

Don't randomly use any force field for modelling. There are certain force fields which work well for certain molecules/ions. Here is a list given below (Source: The Amber Project).  

| Molecule/Ion | Force Field |
| ------------ | ----------- |
| Protein      | ff19SB      |
| DNA          | OL21        |
| RNA          | OL3         |
| Carbohydrates| GLYCAM_06j  |
| Lipids       |lipids21     |



### References:
The Amber Project: https://ambermd.org/   
Journal of Computational Chemistry: https://onlinelibrary.wiley.com/doi/epdf/10.1002/jcc.540020311  
University of Oregon: https://www.uoxray.uoregon.edu/local/manuals/biosym/discovery/General/Forcefields/AMBER.html    
Cornell, W. D., et al. (1995). "A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules." Journal of the American Chemical Society, 117(19), 5179-5197.




