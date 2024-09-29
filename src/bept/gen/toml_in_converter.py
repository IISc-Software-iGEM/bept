import toml
import os


def in_toml(in_file_name: str):
    """
    Converts the .in file to .toml file
    Args:
        file_name: The name of the .in file
    """
    output_name = os.path.splitext(in_file_name)[0] + ".toml"
    # Loading and parsing the INPUT FILE
    with open(in_file_name, "r") as input_file:
        file = input_file.readlines()
        data = {}
        possible_calc_types = [
            "mg-auto",
            "mg-para",
            "mg-manual",
            "fe-manual",
            "mg-dummy",
        ]
        possible_pbe = ["lpbe", "npbe"]
        current_section = ""
        section_count = {}

        for line in file:
            line = line.strip()
            parts = line.split()

            if not line or line == "end" or line == "quit":
                current_section = None
                continue

            if (
                line.startswith("read")
                or line.startswith("elec")
                or line.startswith("print")
            ):
                section_name = line.split()[0]

                # Handle multiple blocks of the same type (e.g., "elec")
                if section_name in section_count:
                    section_count[section_name] += 1
                else:
                    section_count[section_name] = 1
                
                # Create a unique section name if there are multiple blocks
                unique_section_name = section_name
                if section_count[section_name] > 1:
                    unique_section_name = f"{section_name}_{section_count[section_name]}"

                current_section = unique_section_name
                data[current_section] = {}

                if len(line.split()) > 1:
                    first_key = line.split()[1]
                    data[current_section][first_key] = (
                        line.split()[2:] if len(line.split()) > 2 else None
                    )

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


def toml_in(toml_filepath: str):
    """
    Converts the .toml file to .in file
    Args:
        file_name: The name of the .toml file
    """
    lines = []
    # Converting the .toml file to .in file
    with open(toml_filepath, "r") as output_file:
        toml_content = toml.load(output_file)

        for section, values in toml_content.items():
            if section == "print":
                continue
            lines.append(section.split("_")[0])

            for key, value in values.items():
                if key == "calculation-type" or key == "pbe":
                    lines.append(f"    {value}")
                elif key == "write":
                    for i in value:
                        lines.append(f"    {key} {' '.join(i)}")
                elif isinstance(value, list):
                    # Join the list values for proper formatting
                    value_str = " ".join(map(str, value))
                    lines.append(f"    {key} {value_str}")
                else:
                    lines.append(f"    {key} {value}")

            lines.append("end")

        lines.append("print elecEnergy 1 end")
        lines.append("quit")

        with open(
            os.path.basename(toml_filepath).split(".")[0] + ".in", "w+"
        ) as output_file:
            output_file.write("\n".join(lines))
