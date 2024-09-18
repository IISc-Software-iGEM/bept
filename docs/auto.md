# Automation in Bept (auto)

Bept provides a way to automate your commands and save them for future references. This is done through the `auto` command in Bept. The `auto` command has the following features.

## 1. Run one PDB2PQR and APBS at a time

Say you just want to run your given `pdb2pqr` or `apbs` command, you can run the following command to execute and save the command to history.

```bash
# For pdb2pqr
bept auto -p protein.pdb

# For apbs
bept auto -a apbs_input.in
```

## 2. Run series of PDB2PQR and APBS commands

Say you want to run a series of `pdb2pqr` and `apbs` commands, you can make a text file containing the commands and run the following command to execute and save the commands to history.

```bash
bept auto -f commands.txt
```

The format of the `commands.txt` file should be as follows:

- Each line should be in itself a command executable
- The file paths should be correct w.r.t the current working directory

You can interactively run each command one by one by adding the interactive flag `-i` to the command.

```bash
bept auto -f commands.txt -i
```

If you want to say halt the execution of the commands at any command specified, you can add ` :?` in between any command in the file, the execution will go into interactive mode just for that command.
Example - `apbs :? protein.in`.

Note that the ` :?` token is meant to be edited. It is not a command line flag in itself. However for `pdb2pqr` command, if you run `pdb2pqr --your-flags protein.pdb :?`, it will still work, since `pdb2pqr` will interpret it as the output path for `pqr` file.

## 3. Save the commands to history

All the commands will be saved to history and can be viewed using the `history` command. All the apbs_input files generated will be saved in the cache directory.
See `history` docs for more information.
