## Template code Generate by BEPT
## For more information, visit: https://github.com/IISc-Software-iGEM/bept
## Please edit the code as required

from pymol import cmd


def show_bumps(selection="(all)", name="bump_check", quiet=1):
    """
    DESCRIPTION

        Visualize VDW clashes

    ARGUMENTS

        selection = string: atom selection {default: all}

        name = string: name of CGO object to create {default: bump_check}
    """
    # Delete the object if it already exists
    cmd.delete(name)

    # Create the object
    cmd.create(name, selection, zoom=0)

    # Set the sculpting parameters
    cmd.set("sculpt_vdw_vis_mode", 1, name)

    # Set the sculpting field mask
    cmd.set("sculpt_field_mask", 0x020)  # cSculptVDW

    # Set the sculpting state
    for state in range(1, 1 + cmd.count_states("%" + name)):
        cmd.sculpt_activate(name, state)
        strain = cmd.sculpt_iterate(name, state, cycles=0)

        # Print the strain
        if not int(quiet):
            print("VDW Strain in state %d: %f" % (state, strain))

    # Show the object
    cmd.show_as("cgo", name)


if __name__ == "__main__":
    cmd.extend("show_bumps", show_bumps)
