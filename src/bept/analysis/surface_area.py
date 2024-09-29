from Bio.PDB import PDBParser
from Bio.PDB.SASA import ShrakeRupley

def get_residues_and_sasa(protein_file):
    """
    Parameters
    ----------
    protein_file : str
        The pdb file path(without the .pdb)
    
    Returns
    -------
    SASA : int
        The solvent accessible surface area
    """
    p = PDBParser(QUIET=1)
    struct = p.get_structure(protein_file, protein_file + ".pdb")

    sr = ShrakeRupley()
    sr.compute(struct, level="S")

    with open(protein_file + "_surface_resi.txt", "w+") as f:
        for i in struct.get_residues():
            f.write(i.get_resname(), i.id[1])

    return round(struct.sasa, 6)
