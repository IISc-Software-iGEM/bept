from collections import namedtuple

# Define the Atom named tuple
Atom = namedtuple(
    "Atom",
    [
        "type",
        "serial",
        "name",
        "res_name",
        "chain_id",
        "res_seq",
        "ins_code",
        "cx",
        "cy",
        "cz",
        "charge",
        "radius",
    ],
)


def pqr_line_parser(pqr_line: str):
    """
    Parse a PQR line and return an Atom object.
    Args:
        pqr_line (str): a line from a PQR file

    // Code adapted from official PDB2PQR repository
    """
    words = [w.strip() for w in pqr_line.split()]
    token = words.pop(0)
    if token in [
        "REMARK",
        "TER",
        "END",
        "HEADER",
        "TITLE",
        "COMPND",
        "SOURCE",
        "KEYWDS",
        "EXPDTA",
        "AUTHOR",
        "REVDAT",
        "JRNL",
    ]:
        return None
    if token in ["ATOM", "HETATM"]:
        atom_type = token
    elif token[:4] == "ATOM":
        atom_type = "ATOM"
        words = [token[4:]] + words
    elif token[:6] == "HETATM":
        atom_type = "HETATM"
        words = [token[6:]] + words
    else:
        err = f"Unable to parse line: {pqr_line}"
        raise ValueError(err)

    # Parse the line
    serial = int(words.pop(0))
    name = words.pop(0)
    res_name = words.pop(0)
    token = words.pop(0)

    try:
        res_seq = int(token)
        chain_id = None
    except ValueError:
        chain_id = token
        res_seq = int(words.pop(0))

    token = words.pop(0)

    # set x based on token
    try:
        cx = float(token)
        ins_code = None
    except ValueError:
        ins_code = token
        cx = float(words.pop(0))

    # set y, z, charge, and radius
    cy = float(words.pop(0))
    cz = float(words.pop(0))
    charge = float(words.pop(0))
    radius = float(words.pop(0))

    return Atom(
        type=atom_type,
        serial=serial,
        name=name,
        res_name=res_name,
        chain_id=chain_id,
        res_seq=res_seq,
        ins_code=ins_code,
        cx=cx,
        cy=cy,
        cz=cz,
        charge=charge,
        radius=radius,
    )


def atom_list_pqr(pqr_file: str) -> list:
    """
    Parse a PQR file and return a list of Atom objects.
    Args:
        pqr_file (str): path to a PQR file
    """
    atoms = []
    with open(pqr_file, "r") as pf:
        pqr_data = pf.readlines()
    for line in pqr_data:
        atom = pqr_line_parser(line)
        if atom is not None:
            atoms.append(atom)
    return atoms
