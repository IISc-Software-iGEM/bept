import os
from bept.analysis.pot_extract import extract_dx_data
from bept.analysis.pqr_utils import atom_list_pqr
from rich.console import Console

CONSOLE = Console()


def cube_make(dx_filepath: str, pqr_path: str, output_dir: str = os.getcwd()):
    """Write a Cube-format data file.

    Cube file format is defined at
    <https://docs.chemaxon.com/display/Gaussian_Cube_format.html>.

    Args:
        dx_filepath (str): path to the DX file
        output_dir (str): path to the output directory

    // Code adapted from official PDB2PQR repository
    """
    err_cube = False
    destination_path = ""

    try:
        # Extract data from the DX file
        data_dict = extract_dx_data(dx_filepath, return_data=True)

        ## atom list
        atom_list = atom_list_pqr(pqr_path)
        if atom_list is None:
            atom_list = []

        ## Destination path set
        protein = os.path.splitext(os.path.basename(pqr_path))[0]
        destination_path = os.path.join(output_dir, protein + ".cube")

        cube_file = open(destination_path, "w")

        cube_file.write("CPMD CUBE FORMAT FILE" + "\n")
        cube_file.write("OUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n")
        origin = data_dict["origin"]
        cube_file.write(
            f"{len(atom_list):>4} {origin[0]:>11.6f} {origin[1]:>11.6f} "
            f"{origin[2]:>11.6f}\n"
        )
        num_points = data_dict["dimensions"]
        spacings = data_dict["grid spacing"]
        for i in range(3):
            cube_file.write(
                f"{num_points[i]:>4} "
                f"{spacings[i][0]:>11.6f} "
                f"{spacings[i][1]:>11.6f} "
                f"{spacings[i][2]:>11.6f}\n"
            )
        for atom in atom_list:
            cube_file.write(
                f"{atom.serial:>4} {atom.charge:>11.6f} {atom.cx:>11.6f} "
                f"{atom.cy:>11.6f} {atom.cz:>11.6f}\n"
            )
        stride = 6
        values = data_dict["potentials"]
        for i in range(0, len(values), 6):
            if i + stride < len(values):
                imax = i + 6
                words = [f"{val:< 13.5E}" for val in values[i:imax]]
                cube_file.write(" ".join(words) + "\n")
            else:
                words = [f"{val:< 13.5E}" for val in values[i:]]
                cube_file.write(" ".join(words))

        return destination_path, err_cube

    except FileNotFoundError as e:
        CONSOLE.print(f"Error: {e}. The file {e.filename} does not exist.", style="red")
    except Exception as e:
        CONSOLE.print(f"An unexpected error occurred: {e}", style="red")

    err_cube = True

    return destination_path, err_cube
