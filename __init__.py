from pathlib import Path
import os, platform, configparser, datetime, logging

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
else:
    lcad = Path.home() / ".local" / "share"

# Other paths
path = lcad / "NevrenDev" / "QuickScript"
qsscripts = path / "Scripts"
cfg = path / "config.qsconfig"

# Initial function is called in every compiled file, so the program doesn't crash because some directory doesn't exist
def init():
    try:
        from . import qsconfig

        path.mkdir(parents=True, exist_ok=True)
        qsscripts.mkdir(exist_ok=True)

        cfg.touch()
        if cfg.read_text(encoding='utf-8') == "": qsconfig.create()

        logging.info("QuickScript initialized successfully.")
        return 0

    except Exception as e:
        logging.error(f"QuickScript failed to initiate: {e}")
        print(f"QuickScript has failed to initiate.\nCheck {log_file} for more information.")
        return 1

# Had trouble getting .qsconfig location to be sent to other files, so this function basically just returns the location
def config_path():
    return cfg

# List of functions that can be called by other files
__all__ = ['init', 'get_os', 'path', 'qsscripts', 'config_path']
