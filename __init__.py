from pathlib import Path
import os, platform, configparser, datetime, logging

log_file = Path.home() / "QuickScript_logs" / f"log-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_os():
    ost = platform.system()
    if ost == "Windows":
        return "Windows"
    elif ost == "Linux":
        return "Linux"

if get_os() == "Windows":
    lcad = Path(os.environ.get('LOCALAPPDATA', Path.home() / "AppData" / "Local"))
else:
    lcad = Path.home() / ".local" / "share"

path = lcad / "NevrenDev" / "QuickScript"
qsscripts = path / "Scripts"
config = path / "config.cfg"

def init():
    try:
        path.mkdir(parents=True, exist_ok=True)
        qsscripts.mkdir(exist_ok=True)

        config.touch()

        logging.info("QuickScript initialized successfully.")
        return 0

    except Exception as e:
        logging.error(f"QuickScript failed to initiate: {e}")
        print(f"QuickScript has failed to initiate.\nCheck {log_file} for more information.")
        return 1
    
def get_version():
    return "1.0"

__all__ = ['init', 'get_os', 'path', 'qsscripts', 'config', 'get_version']
