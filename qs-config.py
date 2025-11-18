from . import init, qsconfig, qprint, get_os
import os

if init() != 0:
    exit(1)

config = dict(qsconfig.get()._data)

def default():
    if get_os() == "Windows":
        os.system('cls')
    else:
        os.system("clear")
    qprint("QuickScript Config Editor", None, qsconfig.get().debug)
    qprint("Press ENTER or type 'exit' to exit", "green", qsconfig.get().debug)
    qprint("Type `<key> <value>` to edit config option", None, qsconfig.get().debug)
    for k, v in config.items():
        if k in {"debug"}:
            qprint(f"{k}: {v}", None, qsconfig.get().debug)

def edit(key, value):
    if value == "false":
        value = "False"
    elif value == "true":
        value = "True"
    elif isinstance(value, int or float):
        value = str(value)

    config[key] = value

while True:
    default()

    i = input(">>>")

    try:
        if i == "exit":
            break
        k, v = i.split(maxsplit=1)
        edit(k, v)
    except:
        if not i:
            break

for k, v in config.items():
    qsconfig.update(k, v)

qprint("Config has been saved", "green", qsconfig.get().debug)