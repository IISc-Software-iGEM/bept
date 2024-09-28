from functools import lru_cache

from bept.analysis.pot_extract import extract_dx_data


@lru_cache(maxsize=None)
def int_to_coord(x, y, z, filepath):
    """
    The function returns the coordinate of cx, cy, cz in the grid box.
    The formula should be (x*hx + xmin, y*hy + ymin, z*hz + zmin)
    """
    # Read the data
    data_dict = extract_dx_data(filepath, return_data=False)
    xmin, ymin, zmin = data_dict["origin"]
    hx, hy, hz = data_dict["grid spacing"]

    return x * hx + xmin, y * hy + ymin, z * hz + zmin


@lru_cache(maxsize=None)
def coord_to_int(cx: float, cy: float, cz: float, dx_filepath: str):
    """
    The function returns the coordinate of (x,y,z) in the grid box.
    Args:
        cx (float): Actual x coordinate
        cy (float): Actual y coordinate
        cz (float): Actual z coordinate
        dx_filepath (str): Path to the DX file
    """
    # Read the data
    data_dict = extract_dx_data(dx_filepath, return_data=False)
    xmin, ymin, zmin = data_dict["origin"]
    hx, hy, hz = data_dict["grid spacing"]
    hx, hy, hz = hx[0], hy[1], hz[2]
    # Calculate the integer coordinates
    # The below math will ensure the nearest grid point is selected
    x = round((float(cx) - xmin) / hx)
    y = round((float(cy) - ymin) / hy)
    z = round((float(cz) - zmin) / hz)

    return x, y, z
