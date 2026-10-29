from pathlib import Path
import runpy
import os
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / 'tui-deps'))
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import Button, Footer, Header, Label, Static, TextArea

ROOT = Path(os.environ.get('FLOW_EXPLORER_ROOT', HERE.parent)).resolve()
STEPS = runpy.run_path(str(HERE / 'map-flow-tui.py'))['STEPS']
FLOW = [
    'resort: str -> formatted report: str',
    'resort: str -> WeatherReport',
    'resort: str -> snowfall_cm: int',
    'resort: str -> snowfall_cm: int',
]

class FlowEditor(App):
    TITLE = 'DOMAIN LENS / FLOW AND CODE'
    CSS = '''
    Screen { background: #202a25; color: #e6eae4; }
    #main { height: 1fr; }
    #flow { width: 42%; padding: 1 2; background: #202a25; }
    #editor { width: 58%; padding: 1 2; background: #202a25; }
    .step { width: 100%; min-height: 3; margin-bottom: 0; border: round #526b5a; background: #27372e; color: #e6eae4; text-align: left; }
    .step:focus { border: round #8ac69e; background: #2d4939; }
    .edge { color: #e1b97b; padding-left: 2; height: auto; }
    #title { color: #8ac69e; text-style: bold; height: auto; }
    #detail { height: auto; color: #c7d4cb; margin-bottom: 1; }
    #status { height: 2; color: #e1b97b; }
    TextArea { height: 1fr; border: round #526b5a; }
    '''
    BINDINGS = [Binding('ctrl+s', 'save_file', 'Save', priority=True), Binding('ctrl+q', 'quit_safely', 'Quit', priority=True)]

    def __init__(self):
        super().__init__()
        self.path = None
        self.original_bytes = None
        self.baseline = ''
        self.newline = '\n'
        self.has_bom = False

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal(id='main'):
            with VerticalScroll(id='flow'):
                yield Label('REQUEST / RESPONSE FLOW', id='title')
                for i, (name, _, _) in enumerate(STEPS):
                    if i == 5:
                        yield Label('SUPPORT / SETUP', classes='edge')
                    yield Button(name, id=f'step-{i}', classes='step')
                    if i < 4:
                        yield Label('  |  ' + FLOW[i], classes='edge')
            with Vertical(id='editor'):
                yield Label('Choose a component', id='title')
                yield Static('Click a component to read and edit its source.', id='detail')
                yield TextArea.code_editor('', id='code', read_only=True, show_line_numbers=True)
                yield Static('Ctrl+S saves | Ctrl+Q quits', id='status')
        yield Footer()

    def status(self, message):
        self.query_one('#status', Static).update(message)

    def dirty(self):
        return self.path is not None and self.query_one('#code', TextArea).text != self.baseline

    def on_button_pressed(self, event: Button.Pressed):
        if self.dirty():
            self.status('Unsaved edits: Ctrl+S to save, or Ctrl+Z to undo before switching.')
            return
        index = int(event.button.id.split('-')[1])
        name, detail, relative = STEPS[index]
        editor = self.query_one('#code', TextArea)
        self.query_one('#editor #title', Label).update(name)
        self.query_one('#detail', Static).update(detail)
        self.path = ROOT / relative if relative else None
        if self.path is None:
            self.original_bytes = None
            self.baseline = 'A visitor asks for a fictional ski resort snow report.'
            editor.read_only = True
            editor.load_text(self.baseline)
            self.status('No local source for this component.')
            return
        try:
            self.original_bytes = self.path.read_bytes()
            self.has_bom = self.original_bytes.startswith(b'\xef\xbb\xbf')
            text = self.original_bytes.decode('utf-8-sig')
            self.newline = '\r\n' if '\r\n' in text else '\n'
            self.baseline = text.replace('\r\n', '\n')
            editor.read_only = False
            editor.load_text(self.baseline)
            self.status(f'{relative} | Ctrl+S saves | Ctrl+Q quits')
        except (OSError, UnicodeError) as error:
            self.path = None
            editor.read_only = True
            self.status(f'Could not open file: {error}')

    def action_save_file(self):
        if self.path is None:
            self.status('No editable file selected.')
            return
        try:
            if self.path.read_bytes() != self.original_bytes:
                self.status('File changed on disk; save blocked. Reopen after resolving the conflict.')
                return
            text = self.query_one('#code', TextArea).text
            data = text.replace('\n', self.newline).encode('utf-8')
            if self.has_bom:
                data = b'\xef\xbb\xbf' + data
            self.path.write_bytes(data)
            self.original_bytes = data
            self.baseline = text
            self.status(f'Saved {self.path.relative_to(ROOT)}')
        except OSError as error:
            self.status(f'Could not save: {error}')

    def action_quit_safely(self):
        if self.dirty():
            self.status('Unsaved edits: Ctrl+S to save, or Ctrl+Z to undo before quitting.')
        else:
            self.exit()

if __name__ == '__main__':
    FlowEditor().run()
