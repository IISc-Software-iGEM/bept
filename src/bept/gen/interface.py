import warnings
from copy import deepcopy
from typing import Any, Coroutine

import toml
from textual import on
from textual.app import App
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import (Checkbox, Collapsible, Footer, Input, Label,
                             OptionList, RadioButton, RadioSet, Select, Static,
                             TabbedContent, TabPane)
from textual.widgets.option_list import Option

from bept.gen.toml_in_converter import in_toml, toml_in

# GLOBALS
TAB_NAMES = ["Input", "Misc-Options", "Output-Settings"]
possible_inputs = ["mg-auto", "mg-para", "mg-manual", "fe-manual", "mg-dummy"]
mg_auto_def = {
    "read": {"mol": ["pqr", ""]},
    "elec": {
        "calculation-type": "",
        "dime": ["", "", ""],
        "cglen": ["", "", ""],
        "fglen": ["", "", ""],
        "cgcent": ["", ""],
        "fgcent": ["", ""],
        "mol": "1",
        "pbe": "",
        "bcfl": "",
        "pdie": "",
        "sdie": "",
        "srfm": "",
        "chgm": "",
        "sdens": "",
        "srad": "",
        "swin": "",
        "temp": "",
        "calcenergy": "",
        "calcforce": "",
        "write": [],
    },
    "print": {"elecEnergy": ["1", "end"]},
}
data = dict()


def generate_toml_file(input_file):
    global data, input_file_name, write_commands, calcenergy, calcforce, selected_input, form

    in_toml(input_file)
    toml_input_file_name = input_file_name = input_file[:-3] + ".toml"

    # Loading the toml file
    with open(toml_input_file_name, "r") as input_file:
        data = toml.load(input_file)

    write_commands = []
    for i in list(data["elec"].keys()):
        if "write" in i:
            write_commands.append([i.split("-")[1]])
    calcenergy = data["elec"]["calcenergy"]
    calcforce = data["elec"]["calcforce"]
    selected_input = data["elec"]["calculation-type"]
    form = data["elec"]["write-pot"][0]


class Mg_auto_options(Static):
    """
    The mg-auto Options dropdown.

    ...

    Attributes
    ----------
    dime : list
        Grid Points Per Processor
    cglen : list
        Coarse Mesh Domain Lengths
    fglen : list
        Fine Mesh Domain Lengths
    cgcent : list
        Center Of The Coarse Grid
    fgcent : list
        Center Of The Fine Grid
    pbe : str
        Type Of PBE To Be Solved
    bcfl : str
        Boundary Condition Definition
    pdie : str
        Biomolecular Dielectric Constant
    sdie : str
        Dielectric Constant Of The Solvent
    srfm : str
        Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
    chgm : str
        Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
    sdens : str
        Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
    srad : str
        Radius Of The Solvent Molecules
    swin : str
        Size Of The Support For Spline-Based Surface Definitions
    temp : str
        Temperature For PBE Calculation (in K)
    """

    def compose(self):
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        if "dime" in data["elec"]:
            self.dime = data["elec"]["dime"]
        else:
            self.dime = ["193", "225", "225"]

        if "cglen" in data["elec"]:
            self.cglen = data["elec"]["cglen"]
        else:
            self.cglen = ["", "", ""]

        if "fglen" in data["elec"]:
            self.fglen = data["elec"]["fglen"]
        else:
            self.fglen = ["", "", ""]

        if "cgcent" in data["elec"]:
            self.cgcent = data["elec"]["cgcent"]
        else:
            self.cgcent = ["mol", "1"]

        if "fgcent" in data["elec"]:
            self.fgcent = data["elec"]["fgcent"]
        else:
            self.fgcent = ["mol", "1"]

        self.pbe = data["elec"]["pbe"]
        self.bcfl = data["elec"]["bcfl"]
        self.pdie = data["elec"]["pdie"]
        self.sdie = data["elec"]["sdie"]
        self.srfm = data["elec"]["srfm"]
        self.chgm = data["elec"]["chgm"]
        self.sdens = data["elec"]["sdens"]
        self.srad = data["elec"]["srad"]
        self.swin = data["elec"]["swin"]
        self.temp = data["elec"]["temp"]

        # Dropdown starts here
        with Collapsible(title="mg-auto-options", id="mg-auto-options"):
            # GRID POINTS AND DOMAIN LENGHTS"
            with Collapsible(title="GRID POINTS AND DOMAIN LENGHTS", id="gpdlen"):
                yield Horizontal(
                    # Grid Points Per Processor
                    Vertical(
                        Label("Grid Points Per Processor"),
                        Input(value=self.dime[0], id="dime_0", type="number"),
                        Input(value=self.dime[1], id="dime_1", type="number"),
                        Input(value=self.dime[2], id="dime_2", type="number"),
                        id="dime",
                        classes="input-boxes",
                    ),
                    # Coarse Mesh Domain Lengths
                    Vertical(
                        Label("Coarse Mesh Domain Lengths"),
                        Input(value=self.cglen[0], id="cglen_0", type="number"),
                        Input(value=self.cglen[1], id="cglen_1", type="number"),
                        Input(value=self.cglen[2], id="cglen_2", type="number"),
                        id="cglen",
                        classes="input-boxes",
                    ),
                    # Fine Mesh Domain Lengths
                    Vertical(
                        Label("Fine Mesh Domain Lengths"),
                        Input(value=self.fglen[0], id="fglen_0", type="number"),
                        Input(value=self.fglen[1], id="fglen_1", type="number"),
                        Input(value=self.fglen[2], id="fglen_2", type="number"),
                        id="gflen",
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )

            # CENTER OF THE COARSE GRID
            with Collapsible(title="CENTER OF THE COARSE GRID", id="cgcent"):
                with TabbedContent(
                    initial="cgcenter" if self.cgcent[0] == "mol" else "cgmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="cgcenter"):
                        if len(self.cgcent) == 2:
                            cgcent_val = self.cgcent[1]
                        else:
                            cgcent_val = 1
                        yield Input(value=cgcent_val, type="number", id="cgcent")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="cgmanual"
                    ):
                        if len(self.cgcent) == 3:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = self.cgcent
                        else:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=cgcent_val_x,
                            type="number",
                            id="cgcent_0",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=cgcent_val_y,
                            type="number",
                            id="cgcent_1",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=cgcent_val_z,
                            type="number",
                            id="cgcent_2",
                        )

            # CENTER OF THE FINE GRID
            with Collapsible(title="CENTER OF THE FINE GRID", id="fgcent"):
                with TabbedContent(
                    initial="fgcenter" if self.fgcent[0] == "mol" else "fgmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="fgcenter"):
                        if len(self.fgcent) == 2:
                            fgcent_val = self.cgcent[1]
                        else:
                            fgcent_val = 1
                        yield Input(value=fgcent_val, type="number", id="fgcent")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="fgmanual"
                    ):
                        if len(self.fgcent) == 3:
                            fgcent_val_x, fgcent_val_y, fgcent_val_z = self.fgcent
                        else:
                            fgcent_val_x, fgcent_val_y, fgcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=fgcent_val_x,
                            type="number",
                            id="fgcent_0",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=fgcent_val_y,
                            type="number",
                            id="fgcent_1",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=fgcent_val_z,
                            type="number",
                            id="fgcent_2",
                        )

            # TYPE OF PBE TO BE SOLVED
            with Collapsible(title="TYPE OF PBE TO BE SOLVED", id="pbe"):
                pbe_options = OptionList(
                    Option("Linearised", id="pbe lpbe"),
                    Option("Non-Linearised", id="pbe npbe"),
                )
                pbe_options.highlighted = ["lpbe", "npbe"].index(self.pbe)
                yield pbe_options

            # BOUNDARY CONDITION DEFINITION
            with Collapsible(title="BOUNDARY CONDITION DEFINITION", id="bcfl"):
                bcfl_options = OptionList(
                    Option("Zero", id="bcfl zero"),
                    Option("Single Debye-Hückel", id="bcfl sdh"),
                    Option("Multiple Debye-Hückel", id="bcfl mdh"),
                    Option("Focusing", id="bcfl focus"),
                )
                bcfl_options.highlighted = ["zero", "sdh", "mdh", "focus"].index(
                    self.bcfl
                )
                yield bcfl_options

            # MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)
            with Collapsible(title="MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)"):
                yield Horizontal(
                    Vertical(
                        Label("Charge (Ec)"),
                        Input(placeholder="Ion 1", id="ion_0_0"),
                        Input(placeholder="Ion 2", id="ion_1_0"),
                        Input(placeholder="Ion 3", id="ion_2_0"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Concentration (M)"),
                        Input(placeholder="Ion 1", id="ion_0_1"),
                        Input(placeholder="Ion 2", id="ion_1_1"),
                        Input(placeholder="Ion 3", id="ion_2_1"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Radius A"),
                        Input(placeholder="Ion 1", id="ion_0_2"),
                        Input(placeholder="Ion 2", id="ion_1_2"),
                        Input(placeholder="Ion 3", id="ion_2_2"),
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )
            # BIOMOLECULAR DIELECTRIC CONSTANT
            with Collapsible(title="BIOMOLECULAR DIELECTRIC CONSTANT", id="pdie"):
                yield Input(value=self.pdie, type="number", id="pdie")

            # DIELECTRIC CONSTANT OF SOLVENT
            with Collapsible(title="DIELECTRIC CONSTANT OF SOLVENT", id="sdie"):
                yield Input(value=self.sdie, id="sdie", type="number")

            # METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID
            with Collapsible(
                title="METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID",
                id="chgm",
            ):
                chgm_options = OptionList(
                    Option("Traditional trilinear interpolation ", id="chgm spl0"),
                    Option("Cubic B-spline discretization", id="chgm spl2"),
                    Option("Quintic B-spline discretization", id="chgm spl4"),
                )
                chgm_options.highlighted = ["spl0", "spl2", "spl4"].index(self.chgm)
                yield chgm_options

            # NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS
            with Collapsible(
                title="NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS",
                id="sdens",
            ):
                yield Input(value=self.sdens, type="number", id="sdens")

            # MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS
            with Collapsible(
                title="MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS",
                id="srfm",
            ):
                srfm_options = OptionList(
                    Option("Molecular surface definition ", id="srfm mol"),
                    Option("9-point harmonic averaging", id="srfm smol"),
                    Option("Cubic-Spline Surface", id="srfm spl2"),
                    Option("7th order polynomial", id="srfm spl4"),
                )
                srfm_options.highlighted = ["mol", "smol", "spl2", "spl4"].index(
                    self.srfm
                )
                yield srfm_options

            # RADIUS OF THE SOLVENT MOLECULES
            with Collapsible(title="RADIUS OF THE SOLVENT MOLECULES", id="srad"):
                yield Input(value=self.srad, type="number", id="srad")

            # SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS
            with Collapsible(
                title="SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS",
                id="swin",
            ):
                yield Input(value=self.swin, type="number", id="swin")

            # TEMPERATURE FOR PBE CALCULATION (IN K)
            with Collapsible(title="TEMPERATURE FOR PBE CALCULATION (IN K)", id="temp"):
                yield Input(value=self.temp, type="number", id="temp")


class Mg_para_options(Static):
    """
    The mg-para Options dropdown.

    ...

    Attributes
    ----------
    dime : list
        Grid Points Per Processor
    pdime : list
        Processors In Parallel
    ofrac : str
        Amount Of Overlap To Include Between The Individual Processors' Meshes
    cglen : list
        Coarse Mesh Domain Lengths
    fglen : list
        Fine Mesh Domain Lengths
    cgcent : list
        Center Of The Coarse Grid
    fgcent : list
        Center Of The Fine Grid
    pbe : str
        Type Of PBE To Be Solved
    bcfl : str
        Boundary Condition Definition
    pdie : str
        Biomolecular Dielectric Constant
    sdie : str
        Dielectric Constant Of The Solvent
    srfm : str
        Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
    chgm : str
        Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
    sdens : str
        Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
    srad : str
        Radius Of The Solvent Molecules
    swin : str
        Size Of The Support For Spline-Based Surface Definitions
    temp : str
        Temperature For PBE Calculation (in K)
    """

    def compose(self):
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        if "dime" in data["elec"]:
            self.dime = data["elec"]["dime"]
        else:
            self.dime = ["193", "225", "225"]

        if "pdime" in data["elec"]:
            self.pdime = data["elec"]["pdime"]
        else:
            self.pdime = ["1.0", "1.0", "1.0"]

        if "ofrac" in data["elec"]:
            self.ofrac = data["elec"]["pfrac"]
        else:
            self.ofrac = "0.1"

        if "cglen" in data["elec"]:
            self.cglen = data["elec"]["cglen"]
        else:
            self.cglen = ["", "", ""]

        if "fglen" in data["elec"]:
            self.fglen = data["elec"]["fglen"]
        else:
            self.fglen = ["", "", ""]

        if "cgcent" in data["elec"]:
            self.cgcent = data["elec"]["cgcent"]
        else:
            self.cgcent = ["mol", "1"]

        if "fgcent" in data["elec"]:
            self.fgcent = data["elec"]["fgcent"]
        else:
            self.fgcent = ["mol", "1"]

        self.pbe = data["elec"]["pbe"]
        self.bcfl = data["elec"]["bcfl"]
        self.pdie = data["elec"]["pdie"]
        self.sdie = data["elec"]["sdie"]
        self.srfm = data["elec"]["srfm"]
        self.chgm = data["elec"]["chgm"]
        self.sdens = data["elec"]["sdens"]
        self.srad = data["elec"]["srad"]
        self.swin = data["elec"]["swin"]
        self.temp = data["elec"]["temp"]

        # Dropdown starts here
        with Collapsible(title="mg-para-options", id="mg-para-options"):
            # GRID POINTS AND DOMAIN LENGHTS"
            with Collapsible(title="GRID POINTS AND DOMAIN LENGHTS", id="gpdlen"):
                yield Horizontal(
                    # Grid Points Per Processor
                    Vertical(
                        Label("Grid Points Per Processor"),
                        Input(value=self.dime[0], id="dime_0", type="number"),
                        Input(value=self.dime[1], id="dime_1", type="number"),
                        Input(value=self.dime[2], id="dime_2", type="number"),
                        id="dime",
                        classes="input-boxes",
                    ),
                    # Coarse Mesh Domain Lengths
                    Vertical(
                        Label("Coarse Mesh Domain Lengths"),
                        Input(value=self.cglen[0], id="cglen_0", type="number"),
                        Input(value=self.cglen[1], id="cglen_1", type="number"),
                        Input(value=self.cglen[2], id="cglen_2", type="number"),
                        id="cglen",
                        classes="input-boxes",
                    ),
                    # Fine Mesh Domain Lengths
                    Vertical(
                        Label("Fine Mesh Domain Lengths"),
                        Input(value=self.fglen[0], id="fglen_0", type="number"),
                        Input(value=self.fglen[1], id="fglen_1", type="number"),
                        Input(value=self.fglen[2], id="fglen_2", type="number"),
                        id="gflen",
                        classes="input-boxes",
                    ),
                    # Number of Processors in Parallel
                    Vertical(
                        Label("# Processors in Parallel"),
                        Input(value=self.pdime[0], id="pdime_0", type="number"),
                        Input(value=self.pdime[1], id="pdime_1", type="number"),
                        Input(value=self.pdime[2], id="pdime_2", type="number"),
                        id="pdime",
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )

            # AMOUNT OF OVERLAP TO INCLUDE BETWEEN THE INDIVIDUAL PROCESSORS' MESHES
            with Collapsible(
                title="AMOUNT OF OVERLAP TO INCLUDE BETWEEN THE INDIVIDUAL PROCESSORS' MESHES",
                id="ofrac",
            ):
                yield Input(value=self.ofrac, id="ofrac")

            # CENTER OF THE COARSE GRID
            with Collapsible(title="CENTER OF THE COARSE GRID", id="cgcent"):
                with TabbedContent(
                    initial="cgcenter" if self.cgcent[0] == "mol" else "cgmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="cgcenter"):
                        if len(self.cgcent) == 2:
                            cgcent_val = self.cgcent[1]
                        else:
                            cgcent_val = 1
                        yield Input(value=cgcent_val, type="number", id="cgcent")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="cgmanual"
                    ):
                        if len(self.cgcent) == 3:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = self.cgcent
                        else:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=cgcent_val_x,
                            type="number",
                            id="cgcent_0",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=cgcent_val_y,
                            type="number",
                            id="cgcent_1",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=cgcent_val_z,
                            type="number",
                            id="cgcent_2",
                        )

            # CENTER OF THE FINE GRID
            with Collapsible(title="CENTER OF THE FINE GRID", id="fgcent"):
                with TabbedContent(
                    initial="fgcenter" if self.fgcent[0] == "mol" else "fgmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="fgcenter"):
                        if len(self.fgcent) == 2:
                            fgcent_val = self.cgcent[1]
                        else:
                            fgcent_val = 1
                        yield Input(value=fgcent_val, type="number", id="fgcent")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="fgmanual"
                    ):
                        if len(self.fgcent) == 3:
                            fgcent_val_x, fgcent_val_y, fgcent_val_z = self.fgcent
                        else:
                            fgcent_val_x, fgcent_val_y, fgcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=fgcent_val_x,
                            type="number",
                            id="fgcent_0",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=fgcent_val_y,
                            type="number",
                            id="fgcent_1",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=fgcent_val_z,
                            type="number",
                            id="fgcent_2",
                        )

            # TYPE OF PBE TO BE SOLVED
            with Collapsible(title="TYPE OF PBE TO BE SOLVED", id="pbe"):
                pbe_options = OptionList(
                    Option("Linearised", id="pbe lpbe"),
                    Option("Non-Linearised", id="pbe npbe"),
                )
                pbe_options.highlighted = ["lpbe", "npbe"].index(self.pbe)
                yield pbe_options

            # BOUNDARY CONDITION DEFINITION
            with Collapsible(title="BOUNDARY CONDITION DEFINITION", id="bcfl"):
                bcfl_options = OptionList(
                    Option("Zero", id="bcfl zero"),
                    Option("Single Debye-Hückel", id="bcfl sdh"),
                    Option("Multiple Debye-Hückel", id="bcfl mdh"),
                    Option("Focusing", id="bcfl focus"),
                )
                bcfl_options.highlighted = ["zero", "sdh", "mdh", "focus"].index(
                    self.bcfl
                )
                yield bcfl_options

            # MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)
            with Collapsible(title="MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)"):
                yield Horizontal(
                    Vertical(
                        Label("Charge (Ec)"),
                        Input(placeholder="Ion 1", id="ion_0_0"),
                        Input(placeholder="Ion 2", id="ion_1_0"),
                        Input(placeholder="Ion 3", id="ion_2_0"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Concentration (M)"),
                        Input(placeholder="Ion 1", id="ion_0_1"),
                        Input(placeholder="Ion 2", id="ion_1_1"),
                        Input(placeholder="Ion 3", id="ion_2_1"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Radius A"),
                        Input(placeholder="Ion 1", id="ion_0_2"),
                        Input(placeholder="Ion 2", id="ion_1_2"),
                        Input(placeholder="Ion 3", id="ion_2_2"),
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )
            # BIOMOLECULAR DIELECTRIC CONSTANT
            with Collapsible(title="BIOMOLECULAR DIELECTRIC CONSTANT", id="pdie"):
                yield Input(value=self.pdie, type="number", id="pdie")

            # DIELECTRIC CONSTANT OF SOLVENT
            with Collapsible(title="DIELECTRIC CONSTANT OF SOLVENT", id="sdie"):
                yield Input(value=self.sdie, id="sdie", type="number")

            # METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID
            with Collapsible(
                title="METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID",
                id="chgm",
            ):
                chgm_options = OptionList(
                    Option("Traditional trilinear interpolation ", id="chgm spl0"),
                    Option("Cubic B-spline discretization", id="chgm spl2"),
                    Option("Quintic B-spline discretization", id="chgm spl4"),
                )
                chgm_options.highlighted = ["spl0", "spl2", "spl4"].index(self.chgm)
                yield chgm_options

            # NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS
            with Collapsible(
                title="NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS",
                id="sdens",
            ):
                yield Input(value=self.sdens, type="number", id="sdens")

            # MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS
            with Collapsible(
                title="MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS",
                id="srfm",
            ):
                srfm_options = OptionList(
                    Option("Molecular surface definition ", id="srfm mol"),
                    Option("9-point harmonic averaging", id="srfm smol"),
                    Option("Cubic-Spline Surface", id="srfm spl2"),
                    Option("7th order polynomial", id="srfm spl4"),
                )
                srfm_options.highlighted = ["mol", "smol", "spl2", "spl4"].index(
                    self.srfm
                )
                yield srfm_options

            # RADIUS OF THE SOLVENT MOLECULES
            with Collapsible(title="RADIUS OF THE SOLVENT MOLECULES", id="srad"):
                yield Input(value=self.srad, type="number", id="srad")

            # SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS
            with Collapsible(
                title="SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS",
                id="swin",
            ):
                yield Input(value=self.swin, type="number", id="swin")

            # TEMPERATURE FOR PBE CALCULATION (IN K)
            with Collapsible(title="TEMPERATURE FOR PBE CALCULATION (IN K)", id="temp"):
                yield Input(value=self.temp, type="number", id="temp")


class Mg_manual_options(Static):
    """
    The mg-manual Options dropdown.

    ...

    Attributes
    ----------
    dime : list
        Grid Points Per Processor
    glen : list
        Mesh Domain Lengths
    gcent : list
        Center Of The Grid
    pbe : str
        Type Of PBE To Be Solved
    bcfl : str
        Boundary Condition Definition
    pdie : str
        Biomolecular Dielectric Constant
    sdie : str
        Dielectric Constant Of The Solvent
    srfm : str
        Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
    chgm : str
        Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
    sdens : str
        Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
    srad : str
        Radius Of The Solvent Molecules
    swin : str
        Size Of The Support For Spline-Based Surface Definitions
    temp : str
        Temperature For PBE Calculation (in K)
    """

    def compose(self):
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        if "dime" in data["elec"]:
            self.dime = data["elec"]["dime"]
        else:
            self.dime = ["193", "225", "225"]

        if "glen" in data["elec"]:
            self.glen = data["elec"]["glen"]
        elif "cglen" in data["elec"]:
            self.glen = data["elec"]["cglen"]
        else:
            self.glen = ["", "", ""]

        if "gcent" in data["elec"]:
            self.gcent = data["elec"]["gcent"]
        else:
            self.gcent = ["mol", "1"]

        self.pbe = data["elec"]["pbe"]
        self.bcfl = data["elec"]["bcfl"]
        self.pdie = data["elec"]["pdie"]
        self.sdie = data["elec"]["sdie"]
        self.srfm = data["elec"]["srfm"]
        self.chgm = data["elec"]["chgm"]
        self.sdens = data["elec"]["sdens"]
        self.srad = data["elec"]["srad"]
        self.swin = data["elec"]["swin"]
        self.temp = data["elec"]["temp"]

        # Dropdown starts here
        with Collapsible(title="mg-manual-options", id="mg-manual-options"):
            # GRID POINTS AND DOMAIN LENGHTS"
            with Collapsible(title="GRID POINTS AND DOMAIN LENGHTS", id="gpdlen"):
                yield Horizontal(
                    # Grid Points Per Processor
                    Vertical(
                        Label("Grid Points Per Processor"),
                        Input(value=self.dime[0], id="dime_0", type="number"),
                        Input(value=self.dime[1], id="dime_1", type="number"),
                        Input(value=self.dime[2], id="dime_2", type="number"),
                        id="dime",
                        classes="input-boxes",
                    ),
                    # Mesh Domain Lengths
                    Vertical(
                        Label("Mesh Domain Lengths"),
                        Input(value=self.glen[0], id="glen_0", type="number"),
                        Input(value=self.glen[1], id="glen_1", type="number"),
                        Input(value=self.glen[2], id="glen_2", type="number"),
                        id="glen",
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )

            # DEPTH OF THE MULTILEVEL HIERARCHY USED IN THE MULTIGRID SOLVER
            with Collapsible(
                title="DEPTH OF THE MULTILEVEL HIERARCHY USED IN THE MULTIGRID SOLVER"
            ):
                yield Input(value="4", id="nlev", type="number")

            # CENTER OF THE GRID
            with Collapsible(title="CENTER OF THE GRID", id="gcent"):
                with TabbedContent(
                    initial="gcenter" if self.gcent[0] == "mol" else "gmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="gcenter"):
                        if len(self.gcent) == 2:
                            gcent_val = self.gcent[1]
                        else:
                            gcent_val = 1
                        yield Input(value=gcent_val, id="gcent", type="number")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="gmanual"
                    ):
                        if len(self.gcent) == 3:
                            gcent_val_x, gcent_val_y, gcent_val_z = self.gcent
                        else:
                            gcent_val_x, gcent_val_y, gcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=gcent_val_x,
                            id="gcent_0",
                            type="number",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=gcent_val_y,
                            id="gcent_1",
                            type="number",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=gcent_val_z,
                            id="gcent_2",
                            type="number",
                        )

            # TYPE OF PBE TO BE SOLVED
            with Collapsible(title="TYPE OF PBE TO BE SOLVED", id="pbe"):
                pbe_options = OptionList(
                    Option("Linearised", id="pbe lpbe"),
                    Option("Non-Linearised", id="pbe npbe"),
                )
                pbe_options.highlighted = ["lpbe", "npbe"].index(self.pbe)
                yield pbe_options

            # BOUNDARY CONDITION DEFINITION
            with Collapsible(title="BOUNDARY CONDITION DEFINITION", id="bcfl"):
                bcfl_options = OptionList(
                    Option("Zero", id="bcfl zero"),
                    Option("Single Debye-Hückel", id="bcfl sdh"),
                    Option("Multiple Debye-Hückel", id="bcfl mdh"),
                    Option("Focusing", id="bcfl focus"),
                )
                bcfl_options.highlighted = ["zero", "sdh", "mdh", "focus"].index(
                    self.bcfl
                )
                yield bcfl_options

            # MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)
            with Collapsible(title="MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)"):
                yield Horizontal(
                    Vertical(
                        Label("Charge (Ec)"),
                        Input(placeholder="Ion 1", id="ion_0_0"),
                        Input(placeholder="Ion 2", id="ion_1_0"),
                        Input(placeholder="Ion 3", id="ion_2_0"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Concentration (M)"),
                        Input(placeholder="Ion 1", id="ion_0_1"),
                        Input(placeholder="Ion 2", id="ion_1_1"),
                        Input(placeholder="Ion 3", id="ion_2_1"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Radius A"),
                        Input(placeholder="Ion 1", id="ion_0_2"),
                        Input(placeholder="Ion 2", id="ion_1_2"),
                        Input(placeholder="Ion 3", id="ion_2_2"),
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )
            # BIOMOLECULAR DIELECTRIC CONSTANT
            with Collapsible(title="BIOMOLECULAR DIELECTRIC CONSTANT", id="pdie"):
                yield Input(value=self.pdie, type="number", id="pdie")

            # DIELECTRIC CONSTANT OF SOLVENT
            with Collapsible(title="DIELECTRIC CONSTANT OF SOLVENT", id="sdie"):
                yield Input(value=self.sdie, id="sdie", type="number")

            # METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID
            with Collapsible(
                title="METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID",
                id="chgm",
            ):
                chgm_options = OptionList(
                    Option("Traditional trilinear interpolation ", id="chgm spl0"),
                    Option("Cubic B-spline discretization", id="chgm spl2"),
                    Option("Quintic B-spline discretization", id="chgm spl4"),
                )
                chgm_options.highlighted = ["spl0", "spl2", "spl4"].index(self.chgm)
                yield chgm_options

            # NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS
            with Collapsible(
                title="NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS",
                id="sdens",
            ):
                yield Input(value=self.sdens, type="number", id="sdens")

            # MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS
            with Collapsible(
                title="MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS",
                id="srfm",
            ):
                srfm_options = OptionList(
                    Option("Molecular surface definition ", id="srfm mol"),
                    Option("9-point harmonic averaging", id="srfm smol"),
                    Option("Cubic-Spline Surface", id="srfm spl2"),
                    Option("7th order polynomial", id="srfm spl4"),
                )
                srfm_options.highlighted = ["mol", "smol", "spl2", "spl4"].index(
                    self.srfm
                )
                yield srfm_options

            # RADIUS OF THE SOLVENT MOLECULES
            with Collapsible(title="RADIUS OF THE SOLVENT MOLECULES", id="srad"):
                yield Input(value=self.srad, type="number", id="srad")

            # SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS
            with Collapsible(
                title="SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS",
                id="swin",
            ):
                yield Input(value=self.swin, type="number", id="swin")

            # TEMPERATURE FOR PBE CALCULATION (IN K)
            with Collapsible(title="TEMPERATURE FOR PBE CALCULATION (IN K)", id="temp"):
                yield Input(value=self.temp, type="number", id="temp")


class Fe_manual_options(Static):
    """
    The fe-manual Options dropdown.

    ...

    Attributes
    ----------
    pbe : str
        Type Of PBE To Be Solved
    bcfl : str
        Boundary Condition Definition
    pdie : str
        Biomolecular Dielectric Constant
    sdie : str
        Dielectric Constant Of The Solvent
    srfm : str
        Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
    chgm : str
        Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
    sdens : str
        Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
    srad : str
        Radius Of The Solvent Molecules
    swin : str
        Size Of The Support For Spline-Based Surface Definitions
    temp : str
        Temperature For PBE Calculation (in K)
    """

    def compose(self):
        # Loading the required things
        self.pbe = data["elec"]["pbe"]
        self.bcfl = data["elec"]["bcfl"]
        self.pdie = data["elec"]["pdie"]
        self.sdie = data["elec"]["sdie"]
        self.srfm = data["elec"]["srfm"]
        self.chgm = data["elec"]["chgm"]
        self.sdens = data["elec"]["sdens"]
        self.srad = data["elec"]["srad"]
        self.swin = data["elec"]["swin"]
        self.temp = data["elec"]["temp"]

        # Dropdown begins here
        with Collapsible(title="fe-manual-options", id="fe-manual-options"):
            # TYPE OF PBE TO BE SOLVED
            with Collapsible(title="TYPE OF PBE TO BE SOLVED", id="pbe"):
                pbe_options = OptionList(
                    Option("Linearised", id="pbe lpbe"),
                    Option("Non-Linearised", id="pbe npbe"),
                )
                pbe_options.highlighted = ["lpbe", "npbe"].index(self.pbe)
                yield pbe_options

            # BOUNDARY CONDITION DEFINITION
            with Collapsible(title="BOUNDARY CONDITION DEFINITION", id="bcfl"):
                bcfl_options = OptionList(
                    Option("Zero", id="bcfl zero"),
                    Option("Single Debye-Hückel", id="bcfl sdh"),
                    Option("Multiple Debye-Hückel", id="bcfl mdh"),
                    Option("Focusing", id="bcfl focus"),
                )
                bcfl_options.highlighted = ["zero", "sdh", "mdh", "focus"].index(
                    self.bcfl
                )
                yield bcfl_options

            # MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)
            with Collapsible(title="MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)"):
                yield Horizontal(
                    Vertical(
                        Label("Charge (Ec)"),
                        Input(placeholder="Ion 1", id="ion_0_0"),
                        Input(placeholder="Ion 2", id="ion_1_0"),
                        Input(placeholder="Ion 3", id="ion_2_0"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Concentration (M)"),
                        Input(placeholder="Ion 1", id="ion_0_1"),
                        Input(placeholder="Ion 2", id="ion_1_1"),
                        Input(placeholder="Ion 3", id="ion_2_1"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Radius A"),
                        Input(placeholder="Ion 1", id="ion_0_2"),
                        Input(placeholder="Ion 2", id="ion_1_2"),
                        Input(placeholder="Ion 3", id="ion_2_2"),
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )
            # BIOMOLECULAR DIELECTRIC CONSTANT
            with Collapsible(title="BIOMOLECULAR DIELECTRIC CONSTANT", id="pdie"):
                yield Input(value=self.pdie, type="number", id="pdie")

            # DIELECTRIC CONSTANT OF SOLVENT
            with Collapsible(title="DIELECTRIC CONSTANT OF SOLVENT", id="sdie"):
                yield Input(value=self.sdie, id="sdie", type="number")

            # METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID
            with Collapsible(
                title="METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID",
                id="chgm",
            ):
                chgm_options = OptionList(
                    Option("Traditional trilinear interpolation ", id="chgm spl0"),
                    Option("Cubic B-spline discretization", id="chgm spl2"),
                    Option("Quintic B-spline discretization", id="chgm spl4"),
                )
                chgm_options.highlighted = ["spl0", "spl2", "spl4"].index(self.chgm)
                yield chgm_options

            # NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS
            with Collapsible(
                title="NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS",
                id="sdens",
            ):
                yield Input(value=self.sdens, type="number", id="sdens")

            # MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS
            with Collapsible(
                title="MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS",
                id="srfm",
            ):
                srfm_options = OptionList(
                    Option("Molecular surface definition ", id="srfm mol"),
                    Option("9-point harmonic averaging", id="srfm smol"),
                    Option("Cubic-Spline Surface", id="srfm spl2"),
                    Option("7th order polynomial", id="srfm spl4"),
                )
                srfm_options.highlighted = ["mol", "smol", "spl2", "spl4"].index(
                    self.srfm
                )
                yield srfm_options

            # RADIUS OF THE SOLVENT MOLECULES
            with Collapsible(title="RADIUS OF THE SOLVENT MOLECULES", id="srad"):
                yield Input(value=self.srad, type="number", id="srad")

            # SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS
            with Collapsible(
                title="SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS",
                id="swin",
            ):
                yield Input(value=self.swin, type="number", id="swin")

            # TEMPERATURE FOR PBE CALCULATION (IN K)
            with Collapsible(title="TEMPERATURE FOR PBE CALCULATION (IN K)", id="temp"):
                yield Input(value=self.temp, type="number", id="temp")


class Mg_dummy_options(Static):
    """
    The mg-auto Options dropdown.

    ...

    Attributes
    ----------
    dime : list
        Grid Points Per Processor
    cglen : list
        Coarse Mesh Domain Lengths
    cgcent : list
        Center Of The Coarse Grid
    pbe : str
        Type Of PBE To Be Solved
    bcfl : str
        Boundary Condition Definition
    pdie : str
        Biomolecular Dielectric Constant
    sdie : str
        Dielectric Constant Of The Solvent
    srfm : str
        Model To Use To Construct The Dielectric Ion-Accessibility Coefficients
    chgm : str
        Method By Which The Biomolecular Point Charges Are Mapped Onto The Grid
    sdens : str
        Number Of Grid Points Per Square-Angstrom To Use In Surface Constructions
    srad : str
        Radius Of The Solvent Molecules
    swin : str
        Size Of The Support For Spline-Based Surface Definitions
    temp : str
        Temperature For PBE Calculation (in K)
    """

    def compose(self):
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        if "dime" in data["elec"]:
            self.dime = data["elec"]["dime"]
        else:
            self.dime = ["193", "225", "225"]

        if "cglen" in data["elec"]:
            self.cglen = data["elec"]["cglen"]
        else:
            self.cglen = ["", "", ""]

        if "cgcent" in data["elec"]:
            self.cgcent = data["elec"]["cgcent"]
        else:
            self.cgcent = ["mol", "1"]

        self.pbe = data["elec"]["pbe"]
        self.bcfl = data["elec"]["bcfl"]
        self.pdie = data["elec"]["pdie"]
        self.sdie = data["elec"]["sdie"]
        self.srfm = data["elec"]["srfm"]
        self.chgm = data["elec"]["chgm"]
        self.sdens = data["elec"]["sdens"]
        self.srad = data["elec"]["srad"]
        self.swin = data["elec"]["swin"]
        self.temp = data["elec"]["temp"]

        # Dropdown begins here
        with Collapsible(title="mg-dummy-options", id="mg-dummy-options"):
            # GRID POINTS AND DOMAIN LENGHTS"
            with Collapsible(title="GRID POINTS AND DOMAIN LENGHTS", id="gpdlen"):
                yield Horizontal(
                    # Grid Points Per Processor
                    Vertical(
                        Label("Grid Points Per Processor"),
                        Input(value=self.dime[0], id="dime_0", type="number"),
                        Input(value=self.dime[1], id="dime_1", type="number"),
                        Input(value=self.dime[2], id="dime_2", type="number"),
                        id="dime",
                        classes="input-boxes",
                    ),
                    # Coarse Mesh Domain Lengths
                    Vertical(
                        Label("Coarse Mesh Domain Lengths"),
                        Input(value=self.cglen[0], id="cglen_0", type="number"),
                        Input(value=self.cglen[1], id="cglen_1", type="number"),
                        Input(value=self.cglen[2], id="cglen_2", type="number"),
                        id="cglen",
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )

            # CENTER OF THE COARSE GRID
            with Collapsible(title="CENTER OF THE COARSE GRID", id="cgcent"):
                with TabbedContent(
                    initial="cgcenter" if self.cgcent[0] == "mol" else "cgmanual"
                ):
                    # TAB: Center grid on a molecule
                    with TabPane("Center grid on a molecule", id="cgcenter"):
                        if len(self.cgcent) == 2:
                            cgcent_val = self.cgcent[1]
                        else:
                            cgcent_val = 1
                        yield Input(value=cgcent_val, type="number", id="cgcent")
                    # TAB: Manually enter coordinates for center of grid
                    with TabPane(
                        "Manually enter coordinates for center of grid", id="cgmanual"
                    ):
                        if len(self.cgcent) == 3:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = self.cgcent
                        else:
                            cgcent_val_x, cgcent_val_y, cgcent_val_z = "", "", ""

                        yield Input(
                            placeholder="x-coordinate",
                            value=cgcent_val_x,
                            type="number",
                            id="cgcent_0",
                        )
                        yield Input(
                            placeholder="y-coordinate",
                            value=cgcent_val_y,
                            type="number",
                            id="cgcent_1",
                        )
                        yield Input(
                            placeholder="z-coordinate",
                            value=cgcent_val_z,
                            type="number",
                            id="cgcent_2",
                        )

            # TYPE OF PBE TO BE SOLVED
            with Collapsible(title="TYPE OF PBE TO BE SOLVED", id="pbe"):
                pbe_options = OptionList(
                    Option("Linearised", id="pbe lpbe"),
                    Option("Non-Linearised", id="pbe npbe"),
                )
                pbe_options.highlighted = ["lpbe", "npbe"].index(self.pbe)
                yield pbe_options

            # BOUNDARY CONDITION DEFINITION
            with Collapsible(title="BOUNDARY CONDITION DEFINITION", id="bcfl"):
                bcfl_options = OptionList(
                    Option("Zero", id="bcfl zero"),
                    Option("Single Debye-Hückel", id="bcfl sdh"),
                    Option("Multiple Debye-Hückel", id="bcfl mdh"),
                    Option("Focusing", id="bcfl focus"),
                )
                bcfl_options.highlighted = ["zero", "sdh", "mdh", "focus"].index(
                    self.bcfl
                )
                yield bcfl_options

            # MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)
            with Collapsible(title="MOBILE ION SPECIES PRESENT IN SYSTEM (OPTIONAL)"):
                yield Horizontal(
                    Vertical(
                        Label("Charge (Ec)"),
                        Input(placeholder="Ion 1", id="ion_0_0"),
                        Input(placeholder="Ion 2", id="ion_1_0"),
                        Input(placeholder="Ion 3", id="ion_2_0"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Concentration (M)"),
                        Input(placeholder="Ion 1", id="ion_0_1"),
                        Input(placeholder="Ion 2", id="ion_1_1"),
                        Input(placeholder="Ion 3", id="ion_2_1"),
                        classes="input-boxes",
                    ),
                    Vertical(
                        Label("Radius A"),
                        Input(placeholder="Ion 1", id="ion_0_2"),
                        Input(placeholder="Ion 2", id="ion_1_2"),
                        Input(placeholder="Ion 3", id="ion_2_2"),
                        classes="input-boxes",
                    ),
                    classes="input-container",
                )
            # BIOMOLECULAR DIELECTRIC CONSTANT
            with Collapsible(title="BIOMOLECULAR DIELECTRIC CONSTANT", id="pdie"):
                yield Input(value=self.pdie, type="number", id="pdie")

            # DIELECTRIC CONSTANT OF SOLVENT
            with Collapsible(title="DIELECTRIC CONSTANT OF SOLVENT", id="sdie"):
                yield Input(value=self.sdie, id="sdie", type="number")

            # METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID
            with Collapsible(
                title="METHOD BY WHICH THE BIOMOLECULAR POINT CHARGES ARE MAPPED ONTO THE GRID",
                id="chgm",
            ):
                chgm_options = OptionList(
                    Option("Traditional trilinear interpolation ", id="chgm spl0"),
                    Option("Cubic B-spline discretization", id="chgm spl2"),
                    Option("Quintic B-spline discretization", id="chgm spl4"),
                )
                chgm_options.highlighted = ["spl0", "spl2", "spl4"].index(self.chgm)
                yield chgm_options

            # NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS
            with Collapsible(
                title="NUMBER OF GRID POINTS PER SQUARE-ANGSTROM TO USE IN SURFACE CONSTRUCTIONS",
                id="sdens",
            ):
                yield Input(value=self.sdens, type="number", id="sdens")

            # MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS
            with Collapsible(
                title="MODEL TO USE TO CONSTRUCT THE DIELECTRIC ION-ACCESSIBILITY COEFFICIENTS",
                id="srfm",
            ):
                srfm_options = OptionList(
                    Option("Molecular surface definition ", id="srfm mol"),
                    Option("9-point harmonic averaging", id="srfm smol"),
                    Option("Cubic-Spline Surface", id="srfm spl2"),
                    Option("7th order polynomial", id="srfm spl4"),
                )
                srfm_options.highlighted = ["mol", "smol", "spl2", "spl4"].index(
                    self.srfm
                )
                yield srfm_options

            # RADIUS OF THE SOLVENT MOLECULES
            with Collapsible(title="RADIUS OF THE SOLVENT MOLECULES", id="srad"):
                yield Input(value=self.srad, type="number", id="srad")

            # SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS
            with Collapsible(
                title="SIZE OF THE SUPPORT FOR SPLINE-BASED SURFACE DEFINITIONS",
                id="swin",
            ):
                yield Input(value=self.swin, type="number", id="swin")

            # TEMPERATURE FOR PBE CALCULATION (IN K)
            with Collapsible(title="TEMPERATURE FOR PBE CALCULATION (IN K)", id="temp"):
                yield Input(value=self.temp, type="number", id="temp")


class Misc_options(Static):
    """
    The Misc Options Tab.

    ...

    Attributes
    ----------
    calcenergy : str
        Calculation Of Electrostatic Energy From A PBE Calculation
    calcforce : str
        Calculation Of Electrostatic And Apolar Force Outputs From A PBE Calculation
    """

    def compose(self):
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        if "calcenergy" in data["elec"]:
            self.calcenergy = data["elec"]["calcenergy"]
        else:
            self.calcenergy = "no"

        if "calcforce" in data["elec"]:
            self.calcforce = data["elec"]["calcforce"]
        else:
            self.calcforce = "no"

        # Misc-Options begin here
        with VerticalScroll():
            # Remove water from calculations and visualization
            yield Checkbox("Remove water from calculations and visualization")

            # Energy Calculations
            yield Label("Energy Calculations")
            with Collapsible(
                title="CALCULATION OF ELECTROSTATIC ENERGY FROM A PBE CALCULATION:",
                id="calcenergy",
            ):
                with RadioSet(id="energy"):
                    yield RadioButton(
                        "Don't calculate any energies",
                        id="no",
                        value=(self.calcforce == "no"),
                    )
                    yield RadioButton(
                        "Calculate and return total electrostatic energy for the entire molecule ",
                        id="total",
                        value=(self.calcforce == "total"),
                    )
                    yield RadioButton(
                        "Calculate and return total electrostatic energy for the entire molecule as well as energy components for each atom ",
                        id="comps",
                        value=(self.calcforce == "comps"),
                    )

            # Force Calculations
            yield Label("Force Calculations")
            with Collapsible(
                title="CALCULATION OF ELECTROSTATIC AND APOLAR FORCE OUTPUTS FROM A PBE CALCULATION:",
                id="calcforce",
            ):
                with RadioSet(id="force"):
                    yield RadioButton(
                        "Don't calculate any forces",
                        id="no",
                        value=(self.calcenergy == "no"),
                    )
                    yield RadioButton(
                        "Calculate and return total electrostatic and apolar forces for the entire molecule",
                        id="total",
                        value=(self.calcenergy == "total"),
                    )
                    yield RadioButton(
                        "Calculate and return total electrostatic and apolar forces for the entire molecule as well as force components for each atom",
                        id="comps",
                        value=(self.calcenergy == "comps"),
                    )


class Output_options(Static):
    """
    The Output Options Tab.
    """

    def compose(self):
        global selected_input
        # Checking if the follwing is present in the .in file and setting the values to default ones if absent
        self.format = "dx"
        for i in data["elec"].items():
            if "write" in i:
                self.format = i[0]

        # Output-Options begin here
        with VerticalScroll():
            # Scalar Data Output
            yield Label("Scalar Data Output")
            with Collapsible(
                title="OUTPUT OF SCALAR DATA CALCULATED DURING THE PB RUN:"
            ):
                yield Checkbox(
                    "Write out the biomolecular charge distribution in units of ec (multigrid only)",
                    id="charge",
                    value=("write-charge" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the electrostatic potential in units of kbT/ec (multigrid and finite element)",
                    id="pot",
                    value=("write-pot" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the solvent accessibility defined by the molecular surface definition",
                    id="smol",
                    value=("write-smol" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the spline-based solvent accessibility",
                    id="sspl",
                    value=("write-sspl" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the van der Waals-based solvent accessibility",
                    id="vdw",
                    value=("write-vdw" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the inflated van der Waals-based ion accessibility",
                    id="ivdw",
                    value=("write-ivdw" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the Laplacian of the potential in units of kBT/ec/A2 (multigrid only)",
                    id="lap",
                    value=("write-lap" in data["elec"]),
                )
                yield Checkbox(
                    'Write out the "energy density" in units of kBT/ec/A2 (multigrid only)',
                    id="edens",
                    value=("write-edens" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the mobile ion number density for m ion species in units of M (multigrid only)",
                    id="ndens",
                    value=("write-ndens" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the mobile charge density for m ion species in units of eₜᶜ M (multigrid only)",
                    id="qdens",
                    value=("write-qdens" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the dielectric map shifted by 1/2 grid spacing in the x-direction",
                    id="dielx",
                    value=("write-dielx" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the dielectric map shifted by 1/2 grid spacing in the y-direction",
                    id="diely",
                    value=("write-diely" in data["elec"]),
                )
                yield Checkbox(
                    "Write out the dielectric map shifted by 1/2 grid spacing in the z-direction",
                    id="dielz",
                    value=("write-dielz" in data["elec"]),
                )
                # yield Checkbox("Write out the ion-accessibility kappa map")

            # Output Format
            yield Label("Output")
            with Collapsible(title="FORMAT TO WRITE DATA:"):
                with RadioSet(id="format"):
                    yield RadioButton("OpenDX", id="dx", value=(self.format[0] == "dx"))
                    yield RadioButton(
                        "AVS UCD",
                        id="avs",
                        disabled=(selected_input != "fe-manual"),
                        value=(self.format[0] == "avs"),
                    )
                    yield RadioButton(
                        "UBHD",
                        id="uhbd",
                        disabled=(selected_input == "fe-manual"),
                        value=(self.format[0] == "uhbd"),
                    )


class InputApp(App):
    def __init__(self, input_path):
        super().__init__()
        self.input_path = input_path

    # Initializations
    global data, input_file_name, write_commands, calcenergy, calcforce, selected_input, form
    new_data = mg_auto_def
    cgcent = ["", "", ""]
    fgcent = ["", "", ""]
    gcent = ["", "", ""]
    ion = [["", "", ""], ["", "", ""], ["", "", ""]]
    output_item = list(new_data["elec"].items())
    activated_tab = ""

    # CSS
    CSS = """
    .hidden {
        display: none;
    }
    .input-container{
        height: auto;
    }
    .input-boxes {
        align-vertical: middle;
        height: auto;
    }
    #empty-container {
        display: none;
    }
    #Misc-Options {
        dock: top;
        visibility: hidden;
    }
    #Output-Settings {
        dock: top;
        visibility: hidden;
    }
    ToggleButton > .toggle--button {
        background: black;
    }
    ToggleButton.-on > .toggle--button {
        color: red;
    }
    ToggleButton:disabled {
        color: grey;
    }
    ToggleButton:disabled > .toggle--button {
        background: grey;
    }
    OptionList > .option-list--option-highlighted {
        color: red !important;
        text-style: bold;
    }
    VerticalScroll {
        height: auto;
    }
    """

    # Bindings
    BINDINGS = [
        ("i", "show_tab('Input')", "Input"),
        ("m", "show_tab('Misc-Options')", "Misc Options"),
        ("o", "show_tab('Output-Settings')", "Output Settings"),
        ("q", "quit", "Save & Quit"),
        ("<TAB>", "tab", "Move Next"),
        ("<SHIFT+TAB>", "shift_tab", "Move Previous"),
    ]

    def compose(self):
        generate_toml_file(self.input_path)

        # Footer
        yield Footer()

        # TABS
        with TabbedContent(initial="Input"):
            for tab in TAB_NAMES:
                with TabPane(tab, id=tab):
                    if tab == "Input":
                        yield Select(
                            [(inp, inp) for inp in possible_inputs],
                            allow_blank=False,
                            value=selected_input,
                        ).focus()
                    else:
                        yield Vertical(id="empty-container")

    @on(OptionList.OptionHighlighted)
    def on_option_highligted(self, event: OptionList.OptionHighlighted):
        """Handles the change in OptionList Widget"""
        self.new_data["elec"][event.option.id.split()[0]] = event.option.id.split()[1]

    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed):
        """Handles the change in Select Widget"""
        selected_input = event.value
        self.new_data["elec"]["calculation-type"] = selected_input

        # Adding the mg-auto options list
        if selected_input == "mg-auto":
            self.query(Collapsible).remove()
            self.mount(Mg_auto_options())
            self.new_data = deepcopy(mg_auto_def)
            self.new_data["elec"]["calculation-type"] = selected_input

        # Adding the mg-para options list
        elif selected_input == "mg-para":
            self.query(Collapsible).remove()
            self.mount(Mg_para_options())
            self.new_data = deepcopy(mg_auto_def)
            item = list(mg_auto_def["elec"].items())
            item.insert(2, ("pdime", ["", "", ""]))
            item.insert(3, ("ofrac", ""))
            self.new_data["elec"] = dict(item)
            self.new_data["elec"]["calculation-type"] = selected_input

        # Adding the fe-manual options list
        elif selected_input == "fe-manual":
            self.query(Collapsible).remove()
            self.mount(Fe_manual_options())
            self.new_data = deepcopy(mg_auto_def)
            item = list(mg_auto_def["elec"].items())
            for i in item.copy():
                if i[0] in ["dime", "cglen", "cgcent", "fglen", "fgcent"]:
                    item.remove(i)
            self.new_data["elec"] = dict(item)
            self.new_data["elec"]["calculation-type"] = selected_input

        # Adding the mg-manual options list
        elif selected_input == "mg-manual":
            self.query(Collapsible).remove()
            self.mount(Mg_manual_options())
            self.new_data = deepcopy(mg_auto_def)
            item = list(mg_auto_def["elec"].items())
            for i in item.copy():
                if i[0] in ["cglen", "cgcent", "fglen", "fgcent"]:
                    item.remove(i)
            item.insert(
                2,
                (
                    "glen",
                    [
                        "",
                        "",
                        "",
                    ],
                ),
            )
            item.insert(3, ("nlev", ""))
            item.insert(4, ("gcent", ["", ""]))
            self.new_data["elec"] = dict(item)
            self.new_data["elec"]["calculation-type"] = selected_input

        # Adding the mg-dummy options list
        elif selected_input == "mg-dummy":
            self.query(Collapsible).remove()
            self.mount(Mg_dummy_options())
            self.new_data = deepcopy(mg_auto_def)
            item = list(mg_auto_def["elec"].items())
            for i in item.copy():
                if i[0] in ["fglen", "fgcent"]:
                    item.remove(i)
            self.new_data["elec"] = dict(item)
            self.new_data["elec"]["calculation-type"] = selected_input

    @on(RadioSet.Changed)
    def on_radio_set_changed(self, event: RadioSet.Changed):
        """Triggers when the RadioSet widget is changed"""
        if str(event.radio_set.id) == "energy":
            calcenergy = event.pressed.id
        elif str(event.radio_set.id) == "force":
            calcforce = event.pressed.id
        elif str(event.radio_set.id) == "format":
            form = event.pressed.id

    @on(Checkbox.Changed)
    def on_checkbox_changed(self, event: Checkbox.Changed):
        """Triggers when the Checkbox widget is changed"""
        if event.value == True:
            write_commands.append([event.checkbox.id])

    @on(Input.Changed)
    def on_input_submit(self, event: Input.Changed):
        """Triggers when the Input widget is changed"""
        if "gcent" in event.input.id:
            if "_" in event.input.id:
                if event.input.id.startswith("c"):
                    self.cgcent[int(event.input.id.split("_")[1])] = event.value
                elif event.input.id.startswith("f"):
                    self.fgcent[int(event.input.id.split("_")[1])] = event.value
                else:
                    self.gcent[int(event.input.id.split("_")[1])] = event.value
                if "" not in self.cgcent:
                    self.new_data["elec"]["cgcent"] = self.cgcent
                if "" not in self.fgcent:
                    self.new_data["elec"]["fgcent"] = self.fgcent
                if "" not in self.gcent:
                    self.new_data["elec"]["gcent"] = self.gcent
            else:
                self.new_data["elec"][event.input.id.split("_")[0]][0] = "mol"
                self.new_data["elec"][event.input.id.split("_")[0]][1] = event.value
        elif "ion" in event.input.id:
            self.ion[int(event.input.id.split("_")[1])][
                int(event.input.id.split("_")[2])
            ] = event.value
            if "" not in self.ion[int(event.input.id.split("_")[1])]:
                item = list(self.new_data["elec"].items())
                n = int(list(self.new_data["elec"].keys()).index("mol"))
                if "ion" in list(self.new_data["elec"].keys()):
                    item[n - 1][1].append(self.ion[int(event.input.id.split("_")[1])])
                else:
                    item.insert(
                        n, ("ion", [self.ion[int(event.input.id.split("_")[1])]])
                    )
                self.new_data["elec"] = dict(item)
        elif "_" in event.input.id:
            self.new_data["elec"][event.input.id.split("_")[0]][
                int(event.input.id.split("_")[1])
            ] = event.value
        else:
            self.new_data["elec"][event.input.id] = event.value

    def action_show_tab(self, tab: str) -> None:
        """Handles the change in tabs"""
        self.get_child_by_type(TabbedContent).active = tab

    def action_quit(self) -> Coroutine[Any, Any, None]:
        """Triggers when the App is quit"""
        self.new_data["read"]["mol"] = [
            "pqr",
            data["read"]["mol"][1].split(".")[0] + ".pqr",
        ]
        self.new_data["elec"]["calcforce"] = calcforce
        self.new_data["elec"]["calcenergy"] = calcenergy
        for i in range(len(write_commands)):
            write_commands[i].append(form)
            write_commands[i].append(data["read"]["mol"][1].split(".")[0] + ".pqr")
        self.new_data["elec"]["write"] = write_commands

        output_file = open(self.input_path[:-3] + "_bept.toml", "w+")
        toml.dump(self.new_data, output_file)
        output_file.close()
        toml_in(self.input_path[:-3] + "_bept.toml")
        return super().action_quit()

    @on(TabbedContent.TabActivated, pane="#Input")
    def input_activated(self):
        """Triggers when Input tab is opened"""
        self.query_one("#Input").disabled = False
        self.query_one("#Misc-Options").disabled = True
        self.query_one("#Output-Settings").disabled = True
        self.query(Collapsible).remove_class("hidden")
        self.query(Misc_options).remove()
        self.query(Output_options).remove()

    @on(TabbedContent.TabActivated, pane="#Misc-Options")
    def misc_activated(self):
        """Triggers when Misc-Options tab is opened"""
        self.query_one("#Misc-Options").disabled = False
        self.query_one("#Input").disabled = True
        self.query_one("#Output-Settings").disabled = True
        self.query(Collapsible).add_class("hidden")
        self.mount(Misc_options())
        self.query(Output_options).remove()

    @on(TabbedContent.TabActivated, pane="#Output-Settings")
    def output_activated(self):
        """Triggers when Output-Settings tab is opened"""
        self.query_one("#Output-Settings").disabled = False
        self.query_one("#Misc-Options").disabled = True
        self.query_one("#Input").disabled = True
        self.query(Collapsible).add_class("hidden")
        self.query(Misc_options).remove()
        self.mount(Output_options())


for i in InputApp.ion:
    if i.count("") == 2 or i.count("") == 1:
        warnings.warn(
            "All the parameters for ion"
            + str(InputApp.ion.index(i) + 1)
            + " are not provided, and it will be ignored in the calculation"
        )
