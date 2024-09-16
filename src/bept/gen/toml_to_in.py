import toml

# GLOBALS
lines = []
file_name = "7y6i_out.toml"

# Converting the .toml file to .in file
with open(file_name, "r") as output_file:
    toml_content = toml.load(output_file)
    
    for section, values in toml_content.items():
        if section == "print": continue
        lines.append(section)
        for key, value in values.items():
            if key == "calculation-type" or key == "pbe":
                lines.append(f"    {value}")
            elif isinstance(value, list):
                # Join the list values for proper formatting
                value_str = " ".join(map(str, value))
                lines.append(f"    {key} {value_str}")
            else:
                lines.append(f"    {key} {value}")
        lines.append("end")

    lines.append("print elecenergy1 end")
    lines.append("quit")

    with open(file_name.split(".")[0] + ".in", "w+") as output_file:
        output_file.write("\n".join(lines))
