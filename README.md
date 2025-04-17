# Welcome to QuickScript!
QuickScript is a tool that lets you perform actions just by typing a simple command in your terminal
Just open cmd on Windows or Terminal on Linux and type `qs-create` and add a Script name after that and press enter.
This will open your browser with a special web-based creator for QS Script and after saving the script just return to console and type `qs-run` and the name of the QS Script you just created.


For example if you have a local server running via Flask now you don't have to go to it's files and running the server manually, you can just open cmd/terminal and type `qs-run flaskserver`. Or if you customize the Script you can also use `qs-run flaskserver --start` to start the server and `qs-run flaskserver --stop` to stop the server

---

# Installation
There are 3 methods to install QuickScript on your PC

### 1. Manual Installation
Download and unpack your OS's specific binary release and add the unpacked folder to your PATH so you can access QuickScript anywhere on your PC

### 2. OS specific Installer
Download and run your OS's specific installer that will install the newest release and add it to PATH for you

### 3. Universal Installer
Download `Uni-installer.py` and run it. It will automatically detect your OS and install the correct version and add it to PATH. 
⚠️ Note: This method requires Python 3.13 or newer to work properly.

---

# Command Syntaxes
To avoid using long commands like `qs --run --script="..." --start` there are simple command syntaxes to make the usage easier.

Also here are some inline blocks for commands: `[...]` is an optional argument and `<...>` is a required argument

| Command | Arguments | Description |
|---------|-----------|-------------|
| `qs` | `[--ver --credits --synt]` | Shows version, credits, and all command syntaxes|
| `qs-create` | `<script>` | Opens web-based creator for a new script |
| `qs-run` | `<script> [args]` | Runs a script with optional script arguments |
| `qs-list` | None | Lists all available scripts |
| `qs-update` | `[--auto]` | Checks for updates or toggles auto-check on boot |
| `qs-delete` | `<script>` | Permamently deletes a script |

---

# What is a QS Script?
QS Script is a custom script file that stores all data about a script. It is created via `qs-create` in the web-based creator and run using `qs-run`. QS Script is stored as `ScriptName.qsx` and is hidden from basic user to avoid messing with the structure

---

# Future of QuickScript
QuickScript will be available on Windows and Linux Ubuntu based systems. Maybe later there will be an official support of other Linux distros, but currently QuickScript will be exclusive to Windows and Ubuntu. Note that QuickScript will not officially come out on macOS and you will have to download the source code and use it instead of compiled application

Besides the main features there are no additional features planned but I am fully open for suggestions and bug reports which you can post on the Issues tab in the Github Repo

---

# Compiling
You will need to have at least Python 3.13 to be able to use the source code and install `pyinstaller` to compile QuickScript to your OS's native executable file