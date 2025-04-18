from . import init, qsconfig
import argparse

# Checks if program doesn't finds an error
if init() != 0:
    exit(1)

# Arguments handler (makes that you can use ex. --version)
parser = argparse.ArgumentParser()

parser.add_argument('--ver', action='store_true', help='Show QuickScript version')
parser.add_argument('--credits', action="store_true", help='Show QuickScript credits')
parser.add_argument('--synt', action='store_true', help='Show QuickScript command syntaxes')

args = parser.parse_args()

# Logic of arguments
if args.ver:
    print(qsconfig.get().ver_str)
elif args.credits:
    print(qsconfig.get().credits)
elif args.synt:
    print(qsconfig.get().syntaxes)
else:
    print(qsconfig.get().full)