from pathlib import Path
from . import config_path

# Variables to hold info for config file creation
VERSION = '1.0'
VER_STR = f"""--------------------------
Installed QuickScript version: {VERSION}
--------------------------"""
OWNER = "NevrenDev"
CREDITS = f"""--------------------------
QuickScript
Made by {OWNER}
--------------------------"""
SYNTAXES = """
QuickScript Command Syntaxes
    qs [--ver --credits --synt] -> Shows version, credits and command syntaxes
    qs-create <script> -> Opens web-based creator for a new script
    qs-run <script> [args] -> Runs a script with optional script arguments
    qs-list -> Lists all available scripts
    qs-update [--auto] -> Checks for updates or toggles auto-check on boot
    qs-delete <script> -> Permamently deletes a script"""

SYNTAX_STRING = f"""--------------------------
{SYNTAXES}
--------------------------"""

FULL = f"""--------------------------
QuickScript {VERSION}
Made by {OWNER}
{SYNTAXES}
--------------------------"""

# Getting the config file path
cff = config_path()

# Convert data input into Objects (so the code can use ex. qsconfig.get().version instead of qsconfig.get('version'))
class DotDict:
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, item):
        if item == "_data":
            return object.__getattribute__(self, item)

        if item in self._data:
            return self._data[item]
        
        raise AttributeError(f"`{self.__class__.__name__}` object has no attribute '{item}'")
    
    def __repr__(self):
        return f"DotDict({self._data})"

# Creates the initial .qsconfig content
def create():
    cfg = f"""[version]
{VERSION}

[ver_str]
{VER_STR}

[credits]
{CREDITS}

[syntaxes]
{SYNTAX_STRING}

[full]
{FULL}"""

    cff.write_text(cfg, encoding='utf-8')

# Outputs data from .qsconfig
def get():
    cfg = parser(cff)
    return cfg

# Formats .qsconfig for it to be able to be used in code
def parser(file: Path):
    cfg = {}
    current_key = None
    current_value = []

    with file.open(encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith('[') and line.endswith(']'):
                if current_key is not None:
                    cfg[current_key] = "\n".join(current_value)
                current_key = line[1:-1].strip()
                current_value = []
            else:
                current_value.append(line)

        if current_key is not None:
            cfg[current_key] = '\n'.join(current_value)

    return DotDict(cfg)
