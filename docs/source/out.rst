Output files (out)
==================

The ``out`` command is meant for writing output files. Bept provides two
default output files which is always outputted. These are ``.bept`` and
a ``{NAME}_bept.csv`` file which consists of ALL the information about
each atom present in the structure.

The ``out`` command inputs two files COMPULSARILY which are ``.pqr`` and
``.dx`` file of the protein structure which you can obtain with the help
of other COMMANDS of bept.

You can run the ``out`` command by running the following command in the
terminal -

.. code:: bash

   bept out -q /path/to/pqr_file -d /path/to/dx_file

To see the help message, you can run ``bept out --help`` in your
terminal.

Calculation of the Gradients
----------------------------

We calculate the gradients of the electric field at each atom in the
structure. The gradient is calculated using the algorithms used by
``numpy.gradient`` function. To know more about how we implement the
gradient calculation, check out the `Gradient
Calculation <https://github.com/IISc-Software-iGEM/bept/blob/main/bio_docs/electrostatic_gradient.md>`__
documentation on our repository.

Format of ``{protein}_bept.csv``
--------------------------------

The data extracted from PQR file, apbs potential dx file is taken and
mapped to each of the atom present in the PQR file. This data is now
written to a ``.csv`` file making it easier for the user to use the data
for the future. Here are the following columns present in the ``.csv``
file -

1.  ``Type`` - Denoting ATOM, HETATM, etc.
2.  ``Num`` - The serial number of atom from top as present in PQR file.
3.  ``Atom`` - The name of the atom, based on nomenclature provided by
    PQR file.
4.  ``Resi`` - The residue to which the atom belongs.
5.  ``Chain`` - The chain to which the residue belongs.
6.  ``Resi_Seq`` - The sequence number of the residue.
7.  ``Cx`` - The x-coordinate of the atom in the grid w.r.t origin.
8.  ``Cy`` - The y-coordinate of the atom in the grid w.r.t origin.
9.  ``Cz`` - The z-coordinate of the atom in the grid w.r.t origin.
10. ``Q`` - The estimated charge of the atom.
11. ``R`` - The radius of the atom.
12. ``X`` - The grid position of the atom in x-direction w.r.t (0,0,0).
    Always integer.
13. ``Y`` - The grid position of the atom in y-direction w.r.t (0,0,0).
    Always integer.
14. ``Z`` - The grid position of the atom in z-direction w.r.t (0,0,0).
    Always integer.
15. ``Ex`` - The electric field in x-direction at the atom.
16. ``Ey`` - The electric field in y-direction at the atom.
17. ``Ez`` - The electric field in z-direction at the atom.
18. ``Potential`` - The potential value of the atom.

You can use this data for further analysis or for plotting graphs.

   [!Important] This file is generated in the ``.bept`` directory
   present in your current working directory.

Format of ``.bept``
-------------------

The ``.bept`` file is a simple text file which contains a HEADER
containing some metadata which are -

1. Protein Structure Name - Path of input PDB file.
2. The origin coordinates of the structure - Extracted from the PDB
   file.
3. Grid size(x, y, z) of structure - which encloses the protein
   structure.
4. Grid length of the box (hx, hy, hz) - The length of 1 unit along (x,
   y, z) respectively.
5. The paths of reference PQR and Potential DX file inputted.

The ``.bept`` file is simply a tabulated neat looking representation of
the ``.csv`` file.

   [!Important] This file will be generated in your current working
   directory.

Further analysis and generation of other files
----------------------------------------------

Bept currently supports production of the following file types other
than mentioned above -

1. ``.xyz`` - File containing the coordinates of the atoms in the
   structure.

..

   The XYZ File format followed is -
   https://docs.chemaxon.com/display/docs/formats_xyz-format.md

2. ``.cube`` - File containing the potential values of the atoms in the
   structure.

..

   The Gaussian Cube File format followed is -
   https://docs.chemaxon.com/display/docs/formats_gaussian-cube-format.md

You can interactively select which file types to generate by using the
interactive or ``-i`` flag as follows -

3. Surface Residues data with their potential values.

Bept provides a list of surface residues in the protein along with their
Potential value, using ``biopython`` library. The potential value used
here is extracted from the ``bept.csv`` file generated.

.. code:: txt

   V = Sum of potential of atoms on residue / Number of atoms in residue

..

   [!Important] The data is written in a ``.csv`` file stored in the
   ``.bept`` directory as well as a well tabulated
   ``protein_surface_data.txt`` file too.

4. SASA - Solvent Accessible Surface Area for protein.

Bept calculates the SASA value for the protein structure and prints to
the terminal. To know more into how SASA values is calculated, check out
the `SASA
Calculation <https://github.com/IISc-Software-iGEM/bept/blob/main/bio_docs/SASA_Calculations.md>`__
documentation on our repository.

   [!Note] For generation 3 and 4, PDB file paths is necessary.

Usage
-----

The ``out`` command has ``-d`` and ``-q`` as required flags for
providing potential ``.dx`` and ``.pqr`` file respectively. Optionally
(and recommended) is to add ``-p`` path for providing the ``.pdb`` file.

.. code:: bash

   bept out -q /path/to/pqr_file -d /path/to/dx_file -i

To generate all supported files, use the ``-all | --all-types`` flag for
the same.

.. code:: bash

   bept out -q /path/to/pqr_file -d /path/to/dx_file -p /path/to/pdb_file -all

You can also specify the output path of the files by using the ``-o``
flag as follows -

.. code:: bash

   bept out -q /path/to/pqr_file -d /path/to/dx_file -o /path/to/output/directory

The output files will be generated in the specified directory, please do
not provide a file name for output path.
