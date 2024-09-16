from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer

MARKDOWN = ""


class MarkdownApp(App):
    def compose(self) -> ComposeResult:
        yield MarkdownViewer(MARKDOWN, show_table_of_contents=True)


if __name__ == "__main__":
    app = MarkdownApp()
    app.run()
