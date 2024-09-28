from functools import lru_cache


@lru_cache(maxsize=None)
def extract_dx_data(dx_filepath: str, return_data: bool = False):
    """
    # Data from APBS 3.4.1
    #
    # POTENTIAL (kT/e)
    #
    object 1 class gridpositions counts 353 193 257
    origin 6.617750e+01 9.325490e+01 7.383950e+01
    delta 4.895710e-01 0.000000e+00 0.000000e+00
    delta 0.000000e+00 4.995792e-01 0.000000e+00
    delta 0.000000e+00 0.000000e+00 4.786953e-01
    object 2 class gridconnections counts 353 193 257
    object 3 class array type double rank 0 items 17509153         data follows
    8.841046e-01 8.803156e-01 8.765030e-01
    8.726683e-01 8.688033e-01 8.649116e-01
    8.610003e-01 8.570672e-01 8.531058e-01
    8.491277e-01 8.451333e-01 8.411144e-01
    ...
    This is the general format, where first potential is of the format
    U(0,0,0) U(0,0,1) U(0,0,2)
    U(0,0,3) U(0,0,4) U(0,0,5)
    ...

        The function reads the file and extracts the potential data at (i,j,k)

    // Code adapted from official PDB2PQR repository

    Args:
        filepath (str): path to the file
        return_data (bool): if True, returns the potential data as well
    """
    # Read the data
    with open(dx_filepath) as f:
        data = f.readlines()

    # Define dictionary
    dx_dict = {
        "grid spacing": [],  # hx, hy, hz
        "potentials": [],  # U(i,j,k)
        "dimensions": None,  # nx, ny, nz
        "origin": None,  # xmin, ymin, zmin
    }
    for line in data:
        words = [w.strip() for w in line.split()]
        if words[0] in ["#", "attribute", "component"]:
            pass
        elif words[0] == "object":
            if words[1] == "1":
                dx_dict["dimensions"] = (
                    int(words[5]),
                    int(words[6]),
                    int(words[7]),
                )
        elif words[0] == "origin":
            dx_dict["origin"] = [
                float(words[1]),
                float(words[2]),
                float(words[3]),
            ]
        elif words[0] == "delta":
            spacing = [float(words[1]), float(words[2]), float(words[3])]
            dx_dict["grid spacing"].append(spacing)
        else:
            if return_data:
                for word in words:
                    dx_dict["potentials"].append(float(word))
    return dx_dict
