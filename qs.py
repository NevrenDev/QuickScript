from . import init, get_version
import argparse

if init() != 0:
    exit(1)

parser = argparse.ArgumentParser()

parser.add_argument('--ver', action='store_true', help='Show QuickScript version')
parser.add_argument('--credits', action="store_true", help='Show QuickScript credits')
parser.add_argument('--synt', action='store_true', help='Show QuickScript command syntaxes')

args = parser.parse_args()

ver = get_version()

crd = """QuickScript
    Made by: NevrenDev
"""

syntaxes = """QuickScript Command Syntaxes
    qs [--ver --credits --synt] -> Shows version, credits and command syntaxes
    qs-create <script> -> Opens web-based creator for a new script
    qs-run <script> [args] -> Runs a script with optional script arguments
    qs-list -> Lists all available scripts
    qs-update [--auto] -> Checks for updates or toggles auto-check on boot
    qs-delete <script> -> Permamently deletes a script
    """

if args.ver:
    string = "Installed QuickScript version: "+ver
    print("--------------------------")
    print(string)
    print("--------------------------")
elif args.credits:
    print("--------------------------\n")
    print(crd)
    print("--------------------------")
elif args.synt:
    print("--------------------------\n")
    print(syntaxes)
    print("--------------------------")
else:
    full = f"""QuickScript {ver}

Made by: NevrenDev

{syntaxes}"""
    print("--------------------------\n")
    print(full)
    print("--------------------------")