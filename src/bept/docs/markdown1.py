import os
from textual.app import App, ComposeResult
from textual.widgets import Footer, Markdown, TabbedContent, TabPane

class TabbedApp(App):
    """An example of tabbed content."""

    def __init__(self, file_paths):
        super().__init__()
        self.file_paths = file_paths
        self.content = []

    def compose(self) -> ComposeResult:
        """Compose app with tabbed content."""
        
        # Read file contents into self.content
        for file_name in self.file_paths:
            try:
                with open(file_name, "r") as file:
                    self.content.append((os.path.basename(file_name), file.read()))  # Only use the base file name
            except Exception as e:
                self.content.append((os.path.basename(file_name), f"Error reading file: {e}"))
        
        yield Footer()

        # Add the TabbedContent widget
        with TabbedContent():
            for base_file_name, file_content in self.content:
                with TabPane(base_file_name[:-3]):  # Use base file name for tab title
                    yield Markdown(file_content)

    def action_show_tab(self, tab: str) -> None:
        """Switch to a new tab."""
        self.get_child_by_type(TabbedContent).active = tab

if __name__ == "__main__":
    # Specify your file paths here
    file_list = [
        r"C:\Users\dbhar\Downloads\PDB vs PQR.md", r"C:\Users\dbhar\Downloads\PBEQTools.md.md",r"C:\Users\dbhar\Downloads\filetype.md"
        # Add more file paths as needed
    ]
    app = TabbedApp(file_list)
    app.run()
