import bept.gen.interface as interface
from bept.gen.pdb2pqr_textual import pdb2pqrApp


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


def pdb2pqr_gen(pdb_file_path: str):
    """
    Interactive PDB2PQR command generator.
    Args:
        pdb_file_path: The path to the PDB file
    """
    app = pdb2pqrApp(pdb_file_path)
    app.run()
    output_pdb2pqr_cmd = app.output
    return output_pdb2pqr_cmd


if __name__ == "__main__":
    pdb2pqr_gen("../../../protein_pdb/1l2y.pdb")
