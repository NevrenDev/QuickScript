from pathlib import Path
import os, platform, datetime, logging

# Debug mode and text styling ✨
DEBUG = False
try:
    from rich.console import Console
    console = Console()
    def styled(text, style=None):
        return f"[{style}]{text}[/{style}]" if style and not DEBUG else text
    def qprint(text, style=None, **kwargs):
        console.print(styled(text, style), **kwargs)
except ImportError:
    def styled(text, style=None):
        return text
    def qprint(text, style=None, **kwargs):
        print(text, **kwargs)

# Log files location duh
log_file = Path.home() / "QuickScript_logs" / f"log-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
log_file.parent.mkdir(parents=True, exist_ok=True)

# Log file structure
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Returns if your system is Windows or Linux (required for .qsconfig location)
def get_os():
    ost = platform.system()
    if ost == "Windows":
        return "Windows"
    elif ost == "Linux":
        return "Linux"

# Setting up config and scripts folder location
if get_os() == "Windows":
    lcad = Path(os.environ.get('LOCALAPPDATA', Path.home() / "AppData" / "Local"))
elif get_os() == "Linux":
    lcad = Path.home() / ".local" / "share"
else:
    qprint("---WARNING---", "white on red")
    qprint("MacOS or other operating systems than Windows/Linux are not officially supported", "red")
    qprint("For the program to operate normally on other systems, you need to edit the source code by yourself", "red")
    qprint("NevrenDev is not responsible for errors in modified QuickScript instance", "red")
    exit(0)

# Other paths
path = lcad / "NevrenDev" / "QuickScript"
qsscripts = path / "Scripts"
cfg = path / "config.qsconfig"
rt = path / "Runtime"

# Initial function is called in every compiled file, so the program doesn't crash because some directory doesn't exist
def init():
    try:
        from . import qsconfig

        path.mkdir(parents=True, exist_ok=True)
        qsscripts.mkdir(exist_ok=True)
        rt.mkdir(exist_ok=True)

        cfg.touch()
        if cfg.read_text(encoding='utf-8') == "": qsconfig.create()

        ver = qsconfig.VERSION
        print(qsconfig.VER_STR)
        if qsconfig.get().version != ver: qsconfig.create()

        logging.info("QuickScript initialized successfully.")
        return 0

    except Exception as e:
        logging.error(f"QuickScript failed to initiate: {e}")
        qprint(f"QuickScript has failed to initiate.\nCheck {log_file} for more information.", "red")
        return 1

# Had trouble getting .qsconfig location to be sent to other files, so this function basically just returns the location
def config_path():
    return cfg

# List of functions that can be called by other files
__all__ = ['init', 'get_os', 'path', 'qsscripts', 'config_path', 'qprint']
