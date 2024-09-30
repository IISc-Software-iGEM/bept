import os
from typing import Coroutine, Any
from textual.app import App, ComposeResult
from textual.widgets import (
    Footer,
    Label,
    Checkbox,
    RadioSet,
    RadioButton,
    TabbedContent,
    Input,
    TabPane,
    Select,
    Collapsible,
)
from textual import on

__about__ = """
This is an interactive pdb2pqr command generation with input pdb, making it easy to use & giving it a webserver feeling using textual library.
Args:
    input_pdb: The file path to the input pdb file.

Output:
    command to execute
"""


class pdb2pqrApp(App):
    def __init__(self, input_pdb):
        global input_file
        super().__init__()
        input_file = os.path.basename(input_pdb[:-4])

    options = ["--whitespace", "--keep-chain"]
    ph = ""
    nopka = False
    force_field = ""
    naming_scheme = ""
    output = ""
    user_field = ""
    usernames = ""
    apbs_file = ""
    # Bindings
    BINDINGS = [
        ("q", "quit", "Execute and Quit"),
    ]

    def compose(self) -> ComposeResult:
        # forcefield options
        forcefields = [
            "AMBER",
            "SCHARM",
            "PEOEPB",
            "PARSE",
            "SWANSON",
            "TYLO6",
            "User-defined Forcefield",
        ]
        # output naming scheme options
        naming_schemes = [
            "Internal naming scheme",
            "AMBER",
            "SCHARM",
            "PEOEPB",
            "PARSE",
            "SWANSON",
            "TYLO6",
        ]

        """Compose app with tabbed content."""
        yield Footer()
        with TabbedContent():
            with TabPane(title="PDB2PQR"):
                with RadioSet(
                    id="Propka",
                ):
                    yield RadioButton("No pKa calculation", id="nopka")
                    yield RadioButton(
                        "Use PROPKA to assign protonation states at provided pH",
                        value=True,
                        id="propka",
                    )
                with Collapsible(title="pH - Default: 7.0", id="pH", collapsed=False):
                    yield Input(value="7.0", type="number", id="pH")
                with Collapsible(title="Choose a Force-field to use", id="force"):
                    yield Select.from_values(forcefields, allow_blank=False, id="field")
                with Collapsible(title="Choose naming scheme", id="name"):
                    yield Select.from_values(
                        naming_schemes, allow_blank=False, id="name"
                    )
                with Collapsible(
                    title="Additional Inputs (** indicate recommended options to select.)"
                ):
                    yield Checkbox(
                        "Ensure that new atoms are not rebuilt too close to existing atoms",
                        id="--nodebump",
                    )
                    yield Checkbox(
                        "Optimize the hydrogen bonding network", id="--noopt"
                    )
                    yield Checkbox(
                        "Assign charges to the ligand specified in a MOL2 file",
                        id="ligand",
                    )
                    yield Checkbox(
                        "Create an APBS input file **", id="--apbs-input", value=True
                    )
                    yield Checkbox(
                        "Add/keep chain IDs in the PQR file **",
                        id="--keep-chain",
                        value=True,
                    )
                    yield Checkbox(
                        "Insert whitespaces between atom name and residue name, between x and y, and between y and z **",
                        id="--whitespace",
                        value=True,
                    )
                    yield Checkbox(
                        "Remove the waters from the output file", id="--drop-water"
                    )
                    yield Checkbox(
                        "Make the protein's N-terminus neutral(requires PARSE forcefield)",
                        id="--neutraln",
                    )
                    yield Checkbox(
                        "Make the protein's C-terminus neutral(requires PARSE forcefield)",
                        id="--neutralc",
                    )

    def action_quit(self) -> Coroutine[Any, Any, None]:
        if self.apbs_file == "":
            self.options.append(f"--apbs-input={input_file}.in")
        else:
            self.options.append(f"--apbs-input={self.apbs_file}.in")

        if self.nopka is False:
            self.options.append(self.ph)
        if self.force_field != "PARSE":
            if "--neutraln" in self.options:
                self.options.remove("--neutraln")
            if "--neutralc" in self.options:
                self.options.remove("--neutralc")
        self.options.append(input_file + ".pdb")
        self.options.append(input_file + ".pqr")

        if self.naming_scheme == "Internal naming scheme":
            if self.force_field == "User-defined Forcefield":
                self.output = (
                    "pdb2pqr "
                    + "--userff="
                    + self.user_field
                    + " "
                    + "--usernames="
                    + self.usernames
                    + " "
                    + " ".join(self.options)
                )
            else:
                self.output = (
                    "pdb2pqr "
                    + "--ff="
                    + self.force_field
                    + " "
                    + " ".join(self.options)
                )

        elif self.force_field == "User-defined Forcefield":
            self.output = (
                "pdb2pqr "
                + "--userff="
                + self.user_field
                + " "
                + "--usernames="
                + self.usernames
                + " "
                + "--ffout="
                + self.naming_scheme
                + " "
                + " ".join(self.options)
            )
        else:
            self.output = (
                "pdb2pqr "
                + "--ff="
                + self.force_field
                + " "
                + "--ffout="
                + self.naming_scheme
                + " "
                + " ".join(self.options)
            )
        return super().action_quit()

    @on(RadioSet.Changed)
    def on_radiobutton_changed(self, event: RadioSet.Changed):
        if event.pressed.id == "nopka":
            if event.pressed.value == True:
                self.nopka = True
        else:
            self.nopka = False

    @on(Select.Changed)
    def on_select_changed(self, event: Select.Changed):
        """Handles the change in Select Widget"""
        if event.value == "User-defined Forcefield":
            self.force_field = event.value
            self.mount(Label("Enter the path for Force-field File"))
            self.mount(Input(id="force-path"))
            self.mount(Label("Enter the path for names file"))
            self.mount(Input(id="names-path"))
        elif event.select.id == "field":
            self.force_field = event.value

        elif event.select.id == "name":
            self.naming_scheme = event.value

    @on(Input.Changed)
    def on_input_changed(self, event: Input.Changed):
        if event.input.id == "pH":
            self.ph = f"--titration-state-method=propka --with-ph={event.value}"
        elif event.input.id == "--ligand":
            for i in self.options:
                if "ligand" in i:
                    self.options.remove(i)
            self.options.append(f"--ligand={event.value}")
        elif event.input.id == "apbs":
            for i in self.options:
                if "apbs" in i:
                    self.options.remove(i)
            self.apbs_file = event.value
        elif event.input.id == "force-path":
            self.user_field = event.value
        elif event.input.id == "names-path":
            self.usernames = event.value

    @on(Checkbox.Changed)
    def on_checkbox_changed(self, event: Checkbox.Changed):
        if event.value is True:
            if event.checkbox.id == "--noopt":
                if "--noopt" in self.options:
                    self.options.remove(event.checkbox.id)
            elif event.checkbox.id == "ligand":
                self.mount(Label("Input the ligand File"))
                self.mount(Input(id="--ligand"))
            elif event.checkbox.id == "--apbs-input":
                self.mount(
                    Label(
                        f"Input apbs file name (without .in extension). Default: {input_file}.in"
                    )
                )
                self.mount(Input(id="apbs", placeholder=input_file + ".in"))
            else:
                self.options.append(event.checkbox.id)

        elif event.value is False:
            if event.checkbox.id == "--noopt":
                self.options.append(event.checkbox.id)
            else:
                if event.checkbox.id in self.options:
                    self.options.remove(event.checkbox.id)
