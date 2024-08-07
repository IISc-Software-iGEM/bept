from dx_pot_extract import extract
from dx_pot_val import val_potential
from dx_coord import coord_to_int
from dx_elec import elec

def filemaker(protein, pqr_file, pot_dx_file, destination_file):
    """
    This will make our custom potential file.
    We want the coordinate, and the potential at that coordinate. 
    also each line will have x, y, z in integer.
    INFO x y z cx cy cz potential ex ey ez
    The INFO should be pqr file's data
    ATOM   N  Residue A Resi_num    x y z cx cy cz q r potential ex ey ez

    Also some pre data, which tells origin and grid length, etc.
    """
    with open(pqr_file, "r") as f:
        pqr_data= f.readlines()

    xmin, ymin, zmin, hx, hy, hz, nx, ny, nz= extract(pot_dx_file)
    with open(destination_file, "w") as p:
        p.write("Protein structure: " + protein + "\n")
        p.write("Origin(xmin, ymin, zmin): " + str(xmin) + " " + str(ymin) + " " + str(zmin) + "\n")   
        p.write("Grid Box Size(x y z): " + str(nx) + " " + str(ny) + " " + str(nz) + "\n")
        p.write("Grid length(cx cy cz): " + str(hx) + " " + str(hy) + " " + str(hz) + "\n")
        p.write("Reference pqr file: " + pqr_file + "\n")
        p.write("Reference dx potential file: " + pot_dx_file + "\n\n")
        print("Written Header Files.")

        for line in pqr_data:
            line = line.split()
            cx, cy, cz, q, r = line[-5], line[-4], line[-3], line[-2], line[-1]
            x,y,z = coord_to_int(cx, cy, cz, pot_dx_file)
            ex, ey, ez, potential = 0, 0, 0, 0
            typ, num, atom, resi, chain, c = line[0], line[1], line[2], line[3], "", 4
            if isinstance(line[5], str):
                chain = line[5]
                c = 5

            gap = 5
            extra_gap = 25
            # For demonstration, I'm assuming `typ`, `num`, etc., are defined somewhere above this code block
            fields = [str(typ), str(num), str(atom), str(resi), str(chain) if c == 5 else "", str(x), str(y), str(z), str(cx), str(cy), str(cz), str(q), str(r), str(potential), str(ex), str(ey), str(ez)]
            widths = [max(len(field) + (extra_gap if i >= len(fields) - 3 else gap), 10) for i, field in enumerate(fields)]

            # Create a format string based on the calculated widths
            format_str = ''.join(f"{{:<{width}}}" for width in widths) + "\n"
            try:
                potential = val_potential(cx, cy, cz, pot_dx_file)
                ex, ey, ez = elec(x, y, z, pot_dx_file)
                # Use the format string in the write method
                if c == 5:
                    p.write(format_str.format(typ, num, atom, resi, chain, x, y, z, cx, cy, cz, q, r, potential, ex, ey, ez))
                else:
                    # Exclude 'chain' for the else case
                    p.write(format_str.format(typ, num, atom, resi, x, y, z, cx, cy, cz, q, r, potential, ex, ey, ez))
                    
            except FileNotFoundError:
                print("\033[91m\033[1mWARNING: \033[93mPotential and Gradient could not be calculated for coordinate:", cx, cy, cz, "\033[0m")
                print("\033[93mAssuming potential and gradient to be 0. \033[0m")
                # Use the format string in the write method
                if c == 5:
                    p.write(format_str.format(typ, num, atom, resi, chain, x, y, z, cx, cy, cz, q, 0,0,0,0))
                else:
                    # Exclude 'chain' for the else case
                    p.write(format_str.format(typ, num, atom, resi, x, y, z, cx, cy, cz, q, r, 0,0,0,0))
            except Exception as e:
                print("\033[91m\033[1mERROR: \033[93mAn error occured while writing the file: ", e, "\033[0m")
    return

print("Starting. . .")
try:
    filemaker("7yg0", "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0.pqr", "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/7yg0_pot.dx", "/Volumes/Anirudh/IISc/IGEM/Ion-Channel-NCC/codes/potential_analyse/potential.txt")
    print("Your file is generated successfully.")
except Exception as e:
    print("An error occured: ", e)
    print("Process failed. Retry. . .")