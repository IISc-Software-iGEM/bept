import toml

# INPUT AND OUTPUT FILE NAMES
file_name = "7y6i.in"
output_name = file_name[:-3] + ".toml"

# Loading and parsing the INPUT FILE
with open(file_name, "r") as input_file:
    file = input_file.readlines()
    data = {}
    possible_calc_types = ["mg-auto", "mg-para", "mg-manual", "fe-manual", "mg-dummy"]
    possible_pbe = ["lpbe", "npbe"]

    for line in file:
        line = line.strip()
        parts = line.split()

        if not line or line == "end" or line == "quit":
            current_section = None
            continue
        
        if line.startswith("read") or line.startswith("elec") or line.startswith("print"):
            section_name = line.split()[0]
            current_section = section_name
            data[current_section] = {}
            if len(line.split()) > 1:
                first_key = line.split()[1]
                data[current_section][first_key] = line.split()[2:] if len(line.split()) > 2 else None
        elif line in possible_calc_types:
            data[current_section]["calculation-type"] = line
        elif line in possible_pbe:
            data[current_section]["pbe"] = line
        elif "write" == parts[0]:
            data[current_section][parts[0] + "-" + parts[1]] = parts[2:]
        elif current_section:
            key = parts[0]
            value = parts[1:] if len(parts) > 1 else []
            data[current_section][key] = value if len(value) > 1 else value[0]

with open(output_name, "w") as output_file:
    output_file.write(toml.dumps(data))
