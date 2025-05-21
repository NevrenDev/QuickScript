from . import init, qsscripts, qprint
from .qsx_parser import tokenize, parse
from pathlib import Path

# Checks if program doesn't finds an error
if init() != 0:
    exit(1)

qss = list(qsscripts.glob('*.qsx'))

if not qss:
    qprint("There are no QuickScript Scripts at the moment.\nYou can create one using `qs-create`", "white on green")
else:
    for file in qss:
        tokens = tokenize(file)
        ast = parse(tokens)
        sc = ast.ini
        desc = '\n'.join(s.strip('"') for s in sc.script.description)

        name = sc.script.name.strip('"')

        print(f"-------|{name}|-------")
        print(f"Script version: {sc.script.version}")
        print(f"Created with QuickScript ver {sc.qs.version}\n")
        print(desc)
        print("-------|-|-------")