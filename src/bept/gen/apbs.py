import bept.gen.interface as interface


def apbs_gen(input_file_path: str):
    """
    Interactive APBS input file generator.
    Args:
        input_file_path: The path to the input file
    """
    app = interface.InputApp(input_file_path)
    app.run()

    # TOML file paths
    input_toml_path = interface.input_file_name
    output_toml_path = interface.input_file_name[:-5] + "_bept.toml"
    return input_toml_path, output_toml_path
