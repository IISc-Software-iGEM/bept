import os
from bept.analysis.pot_extract import extract_dx_data


def write_cube(dx_filepath: str, output_dir: str = os.getcwd()):
    """Write a Cube-format data file.

    Cube file format is defined at
    <https://docs.chemaxon.com/display/Gaussian_Cube_format.html>.

    Args:


    """
    # Extract data from the DX file
    data_dict = extract_dx_data(dx_filepath, return_data=True)
    num_atoms = data_dict["atom count"]

    ## Destination path set
    protein = os.path.splitext(os.path.basename(dx_filepath))[0]
    destination_path = os.path.join(output_dir, protein + ".cube")

    cube_file = open(destination_path, "w")

    cube_file.write("CPMD CUBE FORMAT FILE - BEPT" + "\n")
    cube_file.write("OUTER LOOP: X, MIDDLE LOOP: Y, INNER LOOP: Z\n")
    origin = data_dict["origin"]
    cube_file.write(
        f"{num_atoms:>4} {origin[0]:>11.6f} {origin[1]:>11.6f} " f"{origin[2]:>11.6f}\n"
    )
    num_points = data_dict["dimensions"]
    spacings = data_dict["grid spacing"]
    for i in range(3):
        cube_file.write(
            f"{-num_points[i]:>4} "
            f"{spacings[i][0]:>11.6f} "
            f"{spacings[i][1]:>11.6f} "
            f"{spacings[i][2]:>11.6f}\n"
        )
    for atom in atom_list:
        cube_file.write(
            f"{atom.serial:>4} {atom.charge:>11.6f} {atom.x:>11.6f} "
            f"{atom.y:>11.6f} {atom.z:>11.6f}\n"
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
