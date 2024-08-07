from dx_pot_extract import extract

def int_to_coord(x,y,z,filepath):
    """
    The function returns the coordinate of cx, cy, cz in the grid box.
    The formula should be (x*hx + xmin, y*hy + ymin, z*hz + zmin)
    """
    # Read the data
    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz = extract(filepath)

    return x*hx + xmin, y*hy + ymin, z*hz + zmin

def coord_to_int(cx,cy,cz,filepath): 
    """
    The function returns the coordinate of (x,y,z) in the grid box.
    The formula should be 
    """
    # Read the data
    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz= extract(filepath)
    # Calculate the integer coordinates
    # The below math will ensure the nearest grid point is selected
    x = round((float(cx) - xmin) / hx)
    y = round((float(cy) - ymin) / hy)
    z = round((float(cz) - zmin) / hz)

    return x,y,z