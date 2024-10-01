Automation in Bept (auto)
=========================

Bept provides a way to automate your commands and save them for future
references. This is done through the ``auto`` command in Bept. The
``auto`` command has the following features.

1. Run one PDB2PQR and APBS at a time
-------------------------------------

Say you just want to run your given ``pdb2pqr`` or ``apbs`` command, you
can run the following command to execute and save the command to
history.

.. code:: bash

   # For pdb2pqr
   bept auto -p protein.pdb

   # For apbs
   bept auto -a apbs_input.in

You can provide the ``--interactive | -i`` flag to run the command
interactively.

2. Run series of PDB2PQR and APBS commands
------------------------------------------

Say you want to run a series of ``pdb2pqr`` and ``apbs`` commands, you
can make a text file containing the commands and run the following
command to execute and save the commands to history, using
``--file-load`` or ``-f`` flag. Here is example -

.. code:: bash

   bept auto -f commands.txt

The format of the ``commands.txt`` file should be as follows:

-  Each line should be in itself a command executable
-  The file paths should be correct w.r.t the current working directory

..

   [!Tip] We have given an example of the ``commands.txt`` file at the
   bottom of this page.

You can interactively run each command one by one by adding the
interactive flag ``-i`` to the command.

.. code:: bash

   bept auto -f commands.txt -i

If you want to say halt the execution of the commands at any command
specified, you can add ``:?`` in between any command in the file, the
execution will go into interactive mode just for that command. Example -
``apbs :? protein.in``.

Note that the ``:?`` token is meant to be edited. It is not a command
line flag in itself. However for ``pdb2pqr`` command, if you run
``pdb2pqr --your-flags protein.pdb :?``, it will still work, since
``pdb2pqr`` will interpret it as the output path for ``pqr`` file.

3. Save the commands to history
-------------------------------

All the commands will be saved to history and can be viewed using the
``history`` command. All the apbs_input files generated will be saved in
the cache directory. See ``history`` docs for more information.

Example for ``commands.txt`` file.
--------------------------------

This file should be a simple ``.txt`` or non executable file. Here is an
example containing various examples for you to run.

.. code:: text

   # This is an example of a simple pdb2pqr command. This line is commented out.
   pdb2pqr --ff=AMBER --apbs-input=2gmo.in --keep-chain --whitespace --drop-water --titration-state-method=propka --with-ph=7 2gmo.pdb 2gmo.pqr

   # Above is an empty line, which is allowed.
   apbs 2gmo.in
   # To halt the command in between automation, you can add :? in between the command. Please edit `:?` else it will be considered as a part of the command.
   pdb2pqr --ff=AMBER --apbs-input=7y6i.in --keep-chain --whitespace 7y6i.pdb 7y6i.pqr :?
   apbs 7y6i.in

**Important Note:**

1. You can have an empty line in between the commands.
2. To write commands in the file, you can use the ``#`` symbol in the
   beginning of the line.

If you have any other issues, feel free to raise an issue on the
repository.
