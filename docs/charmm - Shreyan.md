# CHARMM - Chemistry at HARvard Macromolecular Mechanics

- similar to amber but provides more parameters.
- treats all the atoms separately to find potential energy.
- Also provides parameters to include polarized charges (an advantage over amber)
- target molecules are - proteins, nucleic acids and membranes.

## Atomic representation
- Each atom is a point charge
- For practical purposes, Hydrogen atoms are combined with nearby atoms to give an extended atomic repr.

## Empirical Energy Function
- Uses some formulae to calculate potential energy of the system.
- Accounts for bond potential, bond angle potential, torsion angle potential, van der Walls forces, and electrostatic potential.


## Generation of data structure - to calculate potential
- Sophisticated shit

## Mechanics and Energetics
- The system tends to achieve a state of low energy. 
- Thus, it is desirable to calculate minima of energy, and adjust the coordinates of the system.
- Along with this, there is also a trajectory - due to initial velocity of the atoms.
- Due to computational complexity, it becomes impossible to calculate global minima, and we will have to suffice w/ a local minima. 

## Further reading
[CHARMM: A Program for Macromolecular Energy, Minimization and Dynamics Calculations](https://onlinelibrary.wiley.com/doi/epdf/10.1002/jcc.540040211)


