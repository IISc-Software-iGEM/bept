Interactively Generating PDB2PQR commands and APBS input files
==============================================================

Bept allows you to interactively generate PDB2PQR commands and APBS
input files. This feature makes bept unique and beginner-friendly. Let’s
understand how to interactively generate PDB2PQR commands and APBS input
files.

To see the interactive generation help menu, run ``bept gen --help``.

PDB2PQR
-------

``pdb2pqr --help`` provides a big range of options to choose from.
However, it can be overwhelming for beginners to understand what each
option does and how to use them. Bept simplifies this process by
providing an interactive way to generate PDB2PQR commands, powered by
`textual <https://github.com/Textualize/textual>`__ and
`beaupy <https://github.com/petereon/beaupy>`__. By default, we will use
the textual interface, but you can choose to use beaupy interface with
``-no-tui | -nu`` flag.

The inspiration for having an interactive mode for PDB2PQR came from the
amazing Web server of APBS. The command options provided here are
similar to the ones provided in the web server. The advantage of Bept
here is that you can run it as many times as you want, without any
delays, and you can save the commands for future references
automatically.

Say you have a protein PDB file called ``protein.pdb``. You can
interactively generate the PDB2PQR commands by running -

.. code:: bash

   bept gen -p protein.pdb

Bept has pre-configured default values in the textual interactive
interface where the default command generated without any changes is -

.. code:: bash

   pdb2pqr --ff=AMBER --whitespace --keep-chain --apbs-input=protein.in --titration-state-method=propka --with-ph=7.0 protein.pdb protein.pqr

These are recommended options for beginners to start with. You can
change the options as per your requirements. The output will be
``protein.pqr`` file along with ``protein.in`` file which is necessary
for running APBS.

APBS
----

APBS interactive apbs_input file developer is powered by
`Textual <https://github.com/textualise/textual>`__. The need for such a
terminal UI for input file generation is to simplify your life while
editing and changing the apbs_input file according to the parameters you
want to change.

TOML and INPUT file converter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before diving into details on how the main interface works, Bept
provides conversion between ``.in`` and ``.toml`` files. This is
especially helpful when you want to edit the apbs_input file in a more
user-friendly way, or extract the data from the input file to use in
your own scripts. The conversion is done by running the following
commands:

.. code:: bash

   # To convert .in file to .toml file
   bept gen -into input_file_path.in

   # To convert .toml file to .in file
   bept gen -toin input_file_path.toml

Now let’s understand how to interactively generate apbs_input files.

APBS is a command-line tool requires a ``.in`` input file to run. To
interactively generate the apbs_input file, you must have a dummy
``.in`` file for your protein created by PDB2PQR command.

To run the interactive APBS input file generator -

.. code:: bash

   bept gen -i input_file_path.in

-  The input file path can be relative to current working diretory or
   absolute path, the toml files will be generated in the same directory
   as the input file. However, the output .in file will be generated in
   the current working directory.
-  You can use the keyboard bindings in the footer to change between
   tabs(i for Input, m for Misc Options, o for Output
   Options)/widgets(<TAB> for next widget, <SHIFT+TAB> for previous
   widget).

Here is detailed information about the each option in the APBS
interactive mode has. You can also checkout official documentation for
apbs_input file
`here <https://ics.uci.edu/~dock/manuals/apbs/html/user-guide/x674.html>`__
for more information.

Interactive APBS input file generator. It runs the InputApp.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Args:
^^^^^

-  input_file_path: The path to the input file

GLOBALS in interface file
-------------------------

Vairables:
~~~~~~~~~~

data: dict
^^^^^^^^^^

-  The input data which is to be used as default in the interactive app.

input_file_name: str
^^^^^^^^^^^^^^^^^^^^

-  The name of the input toml file.

write_commands: list
^^^^^^^^^^^^^^^^^^^^

-  List containing all the things checked in the Output Settings.

calcenergy: str
^^^^^^^^^^^^^^^

-  Determines if the electrostatic energy is to be calculated for entire
   molecule, calculated for the entire molecule as well as energy
   components for each atom, or not to be calculated at all.

calcforce: str
^^^^^^^^^^^^^^

-  Determines if the electrostatic and apolar force is to be calculated
   for entire molecule, calculated for the entire molecule as well as
   energy components for each atom, or not to be calculated at all.

selected_input: str
^^^^^^^^^^^^^^^^^^^

-  The calculation type to be used. Possible values are ‘mg-auto’,
   ‘mg-para’, ‘mg-manual’, ‘fe-manual’, and ‘mg-dummy’.

form: str
^^^^^^^^^

-  The format to write the Output data.

TAB_NAMES: list
^^^^^^^^^^^^^^^

-  The list containing all the tab names.

possible_inputs
^^^^^^^^^^^^^^^

-  The list containing all the possible inputs for the calculation-type.

mg_auto_def: dict
^^^^^^^^^^^^^^^^^

-  Intitialization variable for new_data

Functions:
~~~~~~~~~~

generate_toml_file
^^^^^^^^^^^^^^^^^^

-  Generates the input toml file from the given input file and loads it
   into the data variable.
-  Args:

   -  input_file: str

      -  The input file path.

Imported Functions:
~~~~~~~~~~~~~~~~~~~

in_toml
^^^^^^^

-  Converts the .in file to .toml file
-  Args:

   -  file_name: The name of the .in file

toml_in
^^^^^^^

-  Converts the .toml file to .in file
-  Args:

   -  file_name: str

      -  The name of the .toml file

InputApp
--------

The main interactive app.
~~~~~~~~~~~~~~~~~~~~~~~~~

.. _args-1:

Args:
~~~~~

input_path: The path of the input file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attributes:
~~~~~~~~~~~

new_data: dict
^^^^^^^^^^^^^^

-  The dictionary which contains the data updated by the user.

cgcent: list
^^^^^^^^^^^^

-  The list containing the values for the center of the coarse grid.

fgcent: list
^^^^^^^^^^^^

-  The list containing the values for the center of the fine grid.

gcent: list
^^^^^^^^^^^

-  The list containing the values for the center of the grid.

ion: list
^^^^^^^^^

-  The list containing information about Charge, Concentration, and
   Radius of ions.

output_item: list
^^^^^^^^^^^^^^^^^

-  The list containing all the output items.

activated_tab: str
^^^^^^^^^^^^^^^^^^

-  The current active tab. Possible values are ‘Input’, ‘Misc-Options’,
   and ‘Output-Settings’

CSS: str
^^^^^^^^

-  The stylings used for the app.

BINDINGS: list
^^^^^^^^^^^^^^

-  List which contains the keys associated with different actions.

.. _functions-1:

Functions:
~~~~~~~~~~

compose
^^^^^^^

-  Yields the child widgets of the main app.

on_option_highligted
^^^^^^^^^^^^^^^^^^^^

-  Handles the change in OptionList Widget. Triggers when the OptionList
   widget is changed.

on_select_changed
^^^^^^^^^^^^^^^^^

-  Handles the change in Select Widget. Triggers when the Select widget
   is changed.

on_radio_set_changed
^^^^^^^^^^^^^^^^^^^^

-  Handles the change in RadioSet Widget. Triggers when the RadioSet
   widget is changed.

on_checkbox_changed
^^^^^^^^^^^^^^^^^^^

-  Handles the change in Checkbox Widget. Triggers when the Checkbox
   widget is changed.

on_input_submit
^^^^^^^^^^^^^^^

-  Handles the change in Input Widget. Triggers when the Input widget is
   changed.

action_show_tab
^^^^^^^^^^^^^^^

-  Handles the change in tabs. Triggers when a tab is changed.

action_quit
^^^^^^^^^^^

-  Triggers when the App is quit. Finishing the output toml file and
   converting it back to \*.in file.

input_activated
^^^^^^^^^^^^^^^

-  Triggers when Input tab is opened.

misc_activated
^^^^^^^^^^^^^^

-  Triggers when Misc-Options tab is opened.

output_activated
^^^^^^^^^^^^^^^^

-  Triggers when Output-Settings tab is opened.

Mg_auto_options
---------------

The widget for the mg-auto calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-1:

Attributes:
~~~~~~~~~~~

dime : list
^^^^^^^^^^^

-  Grid Points Per Processor

cglen : list
^^^^^^^^^^^^

-  Coarse Mesh Domain Lengths

fglen : list
^^^^^^^^^^^^

-  Fine Mesh Domain Lengths

.. _cgcent-list-1:

cgcent : list
^^^^^^^^^^^^^

-  Center Of The Coarse Grid

.. _fgcent-list-1:

fgcent : list
^^^^^^^^^^^^^

-  Center Of The Fine Grid

pbe : str
^^^^^^^^^

-  Type Of PBE To Be Solved

bcfl : str
^^^^^^^^^^

-  Boundary Condition Definition

pdie : str
^^^^^^^^^^

-  Biomolecular Dielectric Constant

sdie : str
^^^^^^^^^^

-  Dielectric Constant Of The Solvent

srfm : str
^^^^^^^^^^

-  Model To Use To Construct The Dielectric Ion-Accessibility
   Coefficients

chgm : str
^^^^^^^^^^

-  Method By Which The Biomolecular Point Charges Are Mapped Onto The
   Grid

sdens : str
^^^^^^^^^^^

-  Number Of Grid Points Per Square-Angstrom To Use In Surface
   Constructions

srad : str
^^^^^^^^^^

-  Radius Of The Solvent Molecules

swin : str
^^^^^^^^^^

-  Size Of The Support For Spline-Based Surface Definitions

temp : str
^^^^^^^^^^

-  Temperature For PBE Calculation (in K)

.. _functions-2:

Functions:
~~~~~~~~~~

.. _compose-1:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Mg_para_options
---------------

The widget for the mg-para calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-2:

Attributes:
~~~~~~~~~~~

.. _dime-list-1:

dime : list
^^^^^^^^^^^

-  Grid Points Per Processor

pdime : list
^^^^^^^^^^^^

-  Processors In Parallel

ofrac : str
^^^^^^^^^^^

-  Amount Of Overlap To Include Between The Individual Processors’
   Meshes

.. _cglen-list-1:

cglen : list
^^^^^^^^^^^^

-  Coarse Mesh Domain Lengths

.. _fglen-list-1:

fglen : list
^^^^^^^^^^^^

-  Fine Mesh Domain Lengths

.. _cgcent-list-2:

cgcent : list
^^^^^^^^^^^^^

-  Center Of The Coarse Grid

.. _fgcent-list-2:

fgcent : list
^^^^^^^^^^^^^

-  Center Of The Fine Grid

.. _pbe-str-1:

pbe : str
^^^^^^^^^

-  Type Of PBE To Be Solved

.. _bcfl-str-1:

bcfl : str
^^^^^^^^^^

-  Boundary Condition Definition

.. _pdie-str-1:

pdie : str
^^^^^^^^^^

-  Biomolecular Dielectric Constant

.. _sdie-str-1:

sdie : str
^^^^^^^^^^

-  Dielectric Constant Of The Solvent

.. _srfm-str-1:

srfm : str
^^^^^^^^^^

-  Model To Use To Construct The Dielectric Ion-Accessibility
   Coefficients

.. _chgm-str-1:

chgm : str
^^^^^^^^^^

-  Method By Which The Biomolecular Point Charges Are Mapped Onto The
   Grid

.. _sdens-str-1:

sdens : str
^^^^^^^^^^^

-  Number Of Grid Points Per Square-Angstrom To Use In Surface
   Constructions

.. _srad-str-1:

srad : str
^^^^^^^^^^

-  Radius Of The Solvent Molecules

.. _swin-str-1:

swin : str
^^^^^^^^^^

-  Size Of The Support For Spline-Based Surface Definitions

.. _temp-str-1:

temp : str
^^^^^^^^^^

-  Temperature For PBE Calculation (in K)

.. _functions-3:

Functions:
~~~~~~~~~~

.. _compose-2:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Mg_manual_options
-----------------

The widget for the mg-manual calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-3:

Attributes:
~~~~~~~~~~~

.. _dime-list-2:

dime : list
^^^^^^^^^^^

-  Grid Points Per Processor

glen : list
^^^^^^^^^^^

-  Mesh Domain Lengths

.. _gcent-list-1:

gcent : list
^^^^^^^^^^^^

-  Center Of The Grid

.. _pbe-str-2:

pbe : str
^^^^^^^^^

-  Type Of PBE To Be Solved

.. _bcfl-str-2:

bcfl : str
^^^^^^^^^^

-  Boundary Condition Definition

.. _pdie-str-2:

pdie : str
^^^^^^^^^^

-  Biomolecular Dielectric Constant

.. _sdie-str-2:

sdie : str
^^^^^^^^^^

-  Dielectric Constant Of The Solvent

.. _srfm-str-2:

srfm : str
^^^^^^^^^^

-  Model To Use To Construct The Dielectric Ion-Accessibility
   Coefficients

.. _chgm-str-2:

chgm : str
^^^^^^^^^^

-  Method By Which The Biomolecular Point Charges Are Mapped Onto The
   Grid

.. _sdens-str-2:

sdens : str
^^^^^^^^^^^

-  Number Of Grid Points Per Square-Angstrom To Use In Surface
   Constructions

.. _srad-str-2:

srad : str
^^^^^^^^^^

-  Radius Of The Solvent Molecules

.. _swin-str-2:

swin : str
^^^^^^^^^^

-  Size Of The Support For Spline-Based Surface Definitions

.. _temp-str-2:

temp : str
^^^^^^^^^^

-  Temperature For PBE Calculation (in K)

.. _functions-4:

Functions:
~~~~~~~~~~

.. _compose-3:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Fe_manual_options
-----------------

The widget for the fe-manual calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-4:

Attributes:
~~~~~~~~~~~

.. _pbe-str-3:

pbe : str
^^^^^^^^^

-  Type Of PBE To Be Solved

.. _bcfl-str-3:

bcfl : str
^^^^^^^^^^

-  Boundary Condition Definition

.. _pdie-str-3:

pdie : str
^^^^^^^^^^

-  Biomolecular Dielectric Constant

.. _sdie-str-3:

sdie : str
^^^^^^^^^^

-  Dielectric Constant Of The Solvent

.. _srfm-str-3:

srfm : str
^^^^^^^^^^

-  Model To Use To Construct The Dielectric Ion-Accessibility
   Coefficients

.. _chgm-str-3:

chgm : str
^^^^^^^^^^

-  Method By Which The Biomolecular Point Charges Are Mapped Onto The
   Grid

.. _sdens-str-3:

sdens : str
^^^^^^^^^^^

-  Number Of Grid Points Per Square-Angstrom To Use In Surface
   Constructions

.. _srad-str-3:

srad : str
^^^^^^^^^^

-  Radius Of The Solvent Molecules

.. _swin-str-3:

swin : str
^^^^^^^^^^

-  Size Of The Support For Spline-Based Surface Definitions

.. _temp-str-3:

temp : str
^^^^^^^^^^

-  Temperature For PBE Calculation (in K)

.. _functions-5:

Functions:
~~~~~~~~~~

.. _compose-4:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Mg_dummy_options
----------------

The widget for the mg-dummy calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-5:

Attributes:
~~~~~~~~~~~

.. _dime-list-3:

dime : list
^^^^^^^^^^^

-  Grid Points Per Processor

.. _cglen-list-2:

cglen : list
^^^^^^^^^^^^

-  Coarse Mesh Domain Lengths

.. _cgcent-list-3:

cgcent : list
^^^^^^^^^^^^^

-  Center Of The Coarse Grid

.. _pbe-str-4:

pbe : str
^^^^^^^^^

-  Type Of PBE To Be Solved

.. _bcfl-str-4:

bcfl : str
^^^^^^^^^^

-  Boundary Condition Definition

.. _pdie-str-4:

pdie : str
^^^^^^^^^^

-  Biomolecular Dielectric Constant

.. _sdie-str-4:

sdie : str
^^^^^^^^^^

-  Dielectric Constant Of The Solvent

.. _srfm-str-4:

srfm : str
^^^^^^^^^^

-  Model To Use To Construct The Dielectric Ion-Accessibility
   Coefficients

.. _chgm-str-4:

chgm : str
^^^^^^^^^^

-  Method By Which The Biomolecular Point Charges Are Mapped Onto The
   Grid

.. _sdens-str-4:

sdens : str
^^^^^^^^^^^

-  Number Of Grid Points Per Square-Angstrom To Use In Surface
   Constructions

.. _srad-str-4:

srad : str
^^^^^^^^^^

-  Radius Of The Solvent Molecules

.. _swin-str-4:

swin : str
^^^^^^^^^^

-  Size Of The Support For Spline-Based Surface Definitions

.. _temp-str-4:

temp : str
^^^^^^^^^^

-  Temperature For PBE Calculation (in K)

.. _functions-6:

Functions:
~~~~~~~~~~

.. _compose-5:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Misc_options
------------

.. _the-widget-for-the-mg-dummy-calculation-type.-1:

The widget for the mg-dummy calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _attributes-6:

Attributes:
~~~~~~~~~~~

.. _calcenergy-str-1:

calcenergy : str
^^^^^^^^^^^^^^^^

-  Calculation Of Electrostatic Energy From A PBE Calculation

.. _calcforce-str-1:

calcforce : str
^^^^^^^^^^^^^^^

-  Calculation Of Electrostatic And Apolar Force Outputs From A PBE
   Calculation

.. _functions-7:

Functions:
~~~~~~~~~~

.. _compose-6:

compose
^^^^^^^

-  Yields the child widgets of the main app.

Output_options
--------------

.. _the-widget-for-the-mg-dummy-calculation-type.-2:

The widget for the mg-dummy calculation type.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _functions-8:

Functions:
~~~~~~~~~~

.. _compose-7:

compose
^^^^^^^

-  Yields the child widgets of the main app. > Command:
   ``bept gen -a input_file_path``.
