Installation instructions
=========================

Bept is a cross-platform tool and can be installed on MacOS, Linux and
Windows through below-mentioned ways -

Installation
------------

Using pip
~~~~~~~~~

You can download bept from PyPI using pip. Run the below command to
install -

.. code:: bash

   pip install bept

If you want to use it once without installing, you can use the below
command -

.. code:: bash

   pipx bept --help

If you are using ``uv``, you can use-

.. code:: bash

   uvx bept --help

Homebrew
~~~~~~~~

You can download bept from Homebrew by running the below command -

.. code:: bash

   brew install anirudhg07/anirudhg07/bept

Building from source
~~~~~~~~~~~~~~~~~~~~

``bept`` has been made using ``uv`` python package manager. You can
install ``uv`` and run the below commands to install ``bept`` -

.. code:: bash

   git clone https://github.com/IISc-Software-iGEM/bept.git
   cd bept
   pip install .

Check if the tool is successfully installed by running ``bept --help``
and you are good to go!

Dependencies
------------

BEPT mainly uses ``pdb2pqr`` and ``apbs`` tool for running the
electrostatics analysis. You need to have these tools installed on your
system before running BEPT.

-  ``pdb2pqr`` is shipped with BEPT and you don’t need to install it
   separately. The latest version on Pypi will be installed
   automatically.
-  ``apbs`` is not shipped with BEPT and you need to install it
   separately. You can download it from
   `APBS <http://www.poissonboltzmann.org/>`__ official website, or as
   mentioned below.

If you are manually installing the tool, make sure the dependencies are
installed which are mentioned in the ``requirements.txt`` file by
running -

.. code:: bash

   pip install -r requirements.txt

If you downloading via Pypi or Homebrew, these dependencies will be
installed automatically.

APBS and PDB2PQR Installation
-----------------------------

``bept`` focusses on the automation of the process of running PDB2PQR
and APBS. ``pdb2pqr`` is installed along with ``bept`` so you need not
worry. To install APBS, you can follow the below steps -

-  MacOS

.. code:: bash

   sudo port install apbs

-  Linux

.. code:: bash

   sudo apt-get install apbs

-  For Windows, follow the instructions mentioned in the official APBS
   website
   `here <https://apbs.readthedocs.io/en/latest/getting/index.html>`__

Once all the dependencies are installed, you should be able to run
``bept --help`` and get the help message.
