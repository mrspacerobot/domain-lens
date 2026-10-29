from pathlib import Path
import os
import shutil
import sys
import textwrap

ROOT = Path(os.environ.get('FLOW_EXPLORER_ROOT', Path(__file__).resolve().parent.parent)).resolve()
EXAMPLE = 'examples/ski_flow.py'
STEPS = [
    ('Browser', 'A visitor asks for a resort snow report.', None),
    ('RequestHandler', 'Accepts a resort name and formats the report.', EXAMPLE),
    ('SnowService', 'Builds a weather report for the resort.', EXAMPLE),
    ('WeatherGateway', 'Fetches snowfall data from the weather source.', EXAMPLE),
    ('MockWeatherAPI', 'Returns fictional snowfall values.', EXAMPLE),
]

def fit(text, width):
    text = text.expandtabs(4)
    return text[:width].ljust(width)

def panel(title, lines, width, height):
    width = max(width, 5)
    if '--ascii' in sys.argv:
        tl, tr, bl, br, horizontal, vertical = '+', '+', '+', '+', '-', '|'
    else:
        tl, tr, bl, br, horizontal, vertical = '\u256d', '\u256e', '\u2570', '\u256f', '\u2500', '\u2502'
    title = ' ' + title + ' '
    top = tl + title[:width - 2].ljust(width - 2, horizontal) + tr
    body = [vertical + ' ' + fit(line, width - 4) + ' ' + vertical for line in lines[:height]]
    body += [vertical + ' ' + ' ' * (width - 4) + ' ' + vertical] * (height - len(body))
    return [top, *body, bl + horizontal * (width - 2) + br]

HITBOXES = []
FLOW_COLUMN = None
CODE_START = 0
FLOW = [
    ('resort: str', 'formatted report: str'),
    ('report(resort: str)', 'WeatherReport'),
    ('fetch(resort: str)', 'snowfall_cm: int'),
    ('snowfall(resort: str)', 'snowfall_cm: int'),
]
PORTS = [
    ('IN visitor request', 'OUT resort: str'),
    ('IN resort: str', 'OUT formatted report: str'),
    ('IN resort: str', 'OUT WeatherReport'),
    ('IN resort: str', 'OUT snowfall_cm: int'),
    ('IN resort: str', 'OUT snowfall_cm: int'),
]


def screen(selected, offset, width, height):
    """Lay out both text and the exact clickable rectangles in console cells."""
    global HITBOXES, FLOW_COLUMN, CODE_START
    HITBOXES = []
    width, height = max(40, width - 1), max(12, height - 1)
    label, detail, path = STEPS[selected]
    wide = width >= 112 and height >= 39
    flowwidth = min(59, width // 2) if wide else width
    down, up = ('v', '^') if '--ascii' in sys.argv else ('\u2193', '\u2191')
    left = [f'REQUEST {down}  |  RESPONSE {up}  |  example flow', '']
    for index in range(5):
        y = len(left) + 3
        name = STEPS[index][0]
        title = ('> ' if selected == index else '  ') + str(index + 1) + '  ' + name
        left.extend(panel(title, PORTS[index], flowwidth, 2))
        HITBOXES.append((0, y, flowwidth, y + 4, index))
        if index < 4:
            left.append(f'  {down} SEND   ' + FLOW[index][0])
            left.append(f'  {up} RETURN ' + FLOW[index][1])
    left.append('')
    for start in range(5, len(STEPS), 2):
        row = ''
        for index in range(start, min(start + 2, len(STEPS))):
            cell = flowwidth // 2
            x = (index - start) * cell
            title = ('>' if selected == index else ' ') + f'[{index + 1:02}] ' + STEPS[index][0]
            row += fit(title, cell)
            HITBOXES.append((x, len(left) + 3, x + cell, len(left) + 4, index))
        left.append(row)
    # A short terminal uses a compact graph so the code stays visible.
    if not wide:
        left = [f'REQUEST {down} / RESPONSE {up}  |  example flow']
        HITBOXES = []
        for index in range(5):
            y = len(left) + 3
            left.append(('> ' if selected == index else '  ') + f'[{index + 1:02}] ' + STEPS[index][0])
            HITBOXES.append((0, y, width, y + 1, index))
            if index < 4:
                left.append(f'  {down} SEND   ' + FLOW[index][0])
                left.append(f'  {up} RETURN ' + FLOW[index][1])
        for start in range(5, len(STEPS), 2):
            row = ''
            for index in range(start, min(start + 2, len(STEPS))):
                cell = width // 2
                x = (index - start) * cell
                text = ('>' if selected == index else ' ') + f'[{index + 1:02}] ' + STEPS[index][0]
                row += fit(text, cell)
                HITBOXES.append((x, len(left) + 3, x + cell, len(left) + 4, index))
            left.append(row)
    try:
        code = (ROOT / path).read_text(encoding='utf-8').splitlines() if path else [
            'A visitor asks about snowfall at a ski resort.',
            'Input: resort name.',
            'Output: a formatted weather report.',
            '', 'Browser source is outside this repository.']
    except OSError as error:
        code = ['Cannot read source: ' + str(error)]
    rightwidth = width - flowwidth - 3 if wide else width
    available = height - 3 if wide else max(7, height - len(left) - 4)
    description = textwrap.wrap(detail, rightwidth - 4)
    metadata = [label, *description, '', 'FILE ' + (Path(path).name if path else '(external browser)'), '']
    page = max(1, available - len(metadata) - 1)
    offset = max(0, min(offset, max(0, len(code) - page)))
    right = metadata + [f'SOURCE {offset + 1}-{min(len(code), offset + page)} / {len(code)}'] + [
        f'{i + 1:4}  {code[i]}' for i in range(offset, min(len(code), offset + page))]
    FLOW_COLUMN = flowwidth if wide else None
    CODE_START = 3 + len(metadata) + 1 if wide else 3 + len(left) + 1 + len(metadata) + 1
    rows = [' DOMAIN LENS / SKI WEATHER EXAMPLE',
            ' Click component | Left/Right select | Up/Down / wheel scroll | PgUp/PgDn | Q quit', '']
    if wide:
        for i in range(max(len(left), len(right))):
            rows.append(fit(left[i] if i < len(left) else '', flowwidth) + '   ' +
                        (right[i] if i < len(right) else ''))
    else:
        rows.extend(left + [''] + right)
    return '\n'.join(fit(row, width) for row in rows[:height]), len(code), page


def colored(display, selected):
    """Forest Night colors are applied after layout, preserving click positions."""
    base = '38;2;230;234;228;48;2;32;42;37'
    muted = '38;2;146;165;154;48;2;32;42;37'
    mint = '38;2;138;198;158;48;2;32;42;37'
    orange = '38;2;225;185;123;48;2;32;42;37'
    selected_style = '1;38;2;230;234;228;48;2;45;73;57'
    rows = []
    for number, full_line in enumerate(display.split('\n')):
        if FLOW_COLUMN is not None and number >= 3:
            line, source = full_line[:FLOW_COLUMN], full_line[FLOW_COLUMN:]
        elif FLOW_COLUMN is None and number >= CODE_START:
            line, source = '', full_line
        else:
            line, source = full_line, ''
        if number == 0:
            style = mint
        elif number == 1:
            style = muted
        elif ' SEND ' in line or line.startswith('REQUEST'):
            style = orange
        elif ' RETURN ' in line:
            style = mint
        elif 'SOURCE ' in line or 'SUPPORT / SETUP' in line:
            style = mint
        else:
            style = base
        marker = ('> ' + str(selected + 1) + '  ' + STEPS[selected][0]) if selected < 5 else ('>[' + f'{selected + 1:02}' + '] ' + STEPS[selected][0])
        if marker in line:
            before, after = line.split(marker, 1)
            rendered = ('\x1b[' + style + 'm' + before + '\x1b[' + selected_style + 'm' + marker +
                        '\x1b[' + style + 'm' + after)
        else:
            rendered = '\x1b[' + style + 'm' + line
        rows.append(rendered + '\x1b[' + base + 'm' + source + '\x1b[0m')
    return '\n'.join(rows)

def main():
    if '--snapshot' in sys.argv:
        print(screen(2, 0, 144, 44)[0])
        return
    if os.name != 'nt':
        print('This prototype currently requires a Windows terminal.')
        return
    import ctypes
    from ctypes import wintypes
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')

    class Coord(ctypes.Structure):
        _fields_ = [('X', ctypes.c_short), ('Y', ctypes.c_short)]
    class KeyEvent(ctypes.Structure):
        _fields_ = [('down', wintypes.BOOL), ('repeat', wintypes.WORD), ('key', wintypes.WORD),
                    ('scan', wintypes.WORD), ('char', wintypes.WCHAR), ('control', wintypes.DWORD)]
    class MouseEvent(ctypes.Structure):
        _fields_ = [('pos', Coord), ('buttons', wintypes.DWORD), ('control', wintypes.DWORD), ('flags', wintypes.DWORD)]
    class Event(ctypes.Union):
        _fields_ = [('key', KeyEvent), ('mouse', MouseEvent), ('padding', ctypes.c_byte * 16)]
    class Record(ctypes.Structure):
        _fields_ = [('type', wintypes.WORD), ('event', Event)]

    kernel = ctypes.WinDLL('kernel32', use_last_error=True)
    kernel.GetStdHandle.restype = wintypes.HANDLE
    kernel.GetConsoleMode.argtypes = [wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD)]
    kernel.SetConsoleMode.argtypes = [wintypes.HANDLE, wintypes.DWORD]
    kernel.ReadConsoleInputW.argtypes = [wintypes.HANDLE, ctypes.POINTER(Record),
                                       wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
    inp = kernel.GetStdHandle(-10)
    out = kernel.GetStdHandle(-11)
    old_in, old_out = wintypes.DWORD(), wintypes.DWORD()
    if not kernel.GetConsoleMode(inp, ctypes.byref(old_in)) or not kernel.GetConsoleMode(out, ctypes.byref(old_out)):
        raise OSError('Please run this prototype in an interactive Windows console.')
    # Extended flags + mouse input; disable Quick Edit so clicks reach the program.
    if not kernel.SetConsoleMode(inp, (old_in.value | 0x0080 | 0x0010 | 0x0008) & ~0x0040):
        raise OSError('Could not enable mouse input.')
    kernel.SetConsoleMode(out, old_out.value | 0x0004)
    selected, offset = 0, 0
    markers = {1: 'class RequestHandler', 2: 'class SnowService', 3: 'class WeatherGateway', 4: 'class MockWeatherAPI'}

    def choose(index):
        marker = markers.get(index)
        path = STEPS[index][2]
        if not marker or not path:
            return 0
        try:
            lines = (ROOT / path).read_text(encoding='utf-8').splitlines()
            return max(0, next((i for i, line in enumerate(lines) if marker in line), 0) - 2)
        except OSError:
            return 0

    sys.stdout.write('\x1b[?1049h\x1b[?25l\x1b[2J')
    try:
        while True:
            size = shutil.get_terminal_size((120, 40))
            display, total, page = screen(selected, offset, size.columns, size.lines)
            # Cursor home + one buffered frame avoids shell clears and flicker.
            sys.stdout.write('\x1b[H' + colored(display, selected) + '\x1b[J')
            sys.stdout.flush()
            while True:
                record, count = Record(), wintypes.DWORD()
                if not kernel.ReadConsoleInputW(inp, ctypes.byref(record), 1, ctypes.byref(count)):
                    raise OSError('Could not read console input.')
                if record.type == 4:  # Console resize: rebuild layout and click targets.
                    break
                if record.type == 1 and record.event.key.down:
                    k = record.event.key
                    if k.char.lower() == 'q' or k.key == 27:
                        return
                    if k.key in (37, 39):
                        selected = (selected + (-1 if k.key == 37 else 1)) % len(STEPS)
                        offset = choose(selected)
                    elif k.key == 38: offset = max(0, offset - 1)
                    elif k.key == 40: offset = min(max(0, total - 1), offset + 1)
                    elif k.key == 33: offset = max(0, offset - page)
                    elif k.key == 34: offset = min(max(0, total - 1), offset + page)
                    else: continue
                    break
                if record.type == 2:
                    m = record.event.mouse
                    if m.flags == 0 and m.buttons & 1:
                        for x0, y0, x1, y1, index in HITBOXES:
                            if x0 <= m.pos.X < x1 and y0 <= m.pos.Y < y1:
                                selected, offset = index, choose(index)
                                break
                        else:
                            continue
                        break
                    elif m.flags == 4:
                        delta = ctypes.c_short((m.buttons >> 16) & 0xffff).value
                        offset = max(0, min(max(0, total - 1), offset - (3 if delta > 0 else -3)))
                        break
    finally:
        kernel.SetConsoleMode(inp, old_in.value)
        kernel.SetConsoleMode(out, old_out.value)
        sys.stdout.write('\x1b[0m\x1b[?25h\x1b[?1049l')
        sys.stdout.flush()

if __name__ == '__main__':
    main()
