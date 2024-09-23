from bept.analysis.coord_conv import coord_to_int
from bept.analysis.pot_extract import extract_dx_data

# Cache for storing file data
file_cache = {}


def val_potential(cx, cy, cz, filepath):
    """
    This file will extract the potential value at cx, cy, cz.
    The convert it to x,y,z and extract the potential value.
    """

    # Check if data for this file is already in cache
    if filepath not in file_cache:
        # If not, read it and store it in cache
        file_cache[filepath] = extract_dx_data(filepath, return_data=True)

    _, ny, nz = file_cache[filepath]["dimensions"]  # Extract nx, ny, nz
    data = file_cache[filepath]["potentials"]  # Extract the potential data
    x, y, z = coord_to_int(cx, cy, cz, filepath)

    # Extract the potential data
    # Formula for which line to target
    total_z = x * ny * nz + y * nz + z
    # # Calculate the line number and the position within the line
    line_number = total_z // 3
    position = total_z % 3
    # Extract the potential from the data
    potential = data[line_number].split()[position]

    return float(potential)
