# Grocery List App

A small command-line grocery list program written in Python. You type items in, confirm them, and can remove them again. Everything runs in the terminal, with no extra libraries to install.

## What it does

- Add grocery items one at a time (it asks "Are you sure?" before adding each one)
- Remove items from the list
- Ignores extra spaces and capital letters (`  Milk ` is stored as `milk`)
- Type `q` at the item prompt to quit
- Type `q` at the removal prompt to cancel removing and go back to adding items

Note: the list is only kept while the program is running. When you quit, it is gone.

## Project files

| File | Purpose |
|------|---------|
| `grocery.py` | The grocery list logic |
| `main.py` | The file you run to start the app |

Keep both files **in the same folder**, because `main.py` imports from `grocery.py`.

---

## Step 1: Install Python

You need Python 3 (any current version works). If you already have it, check with the version command in your OS section below and skip ahead.

### Windows (10 or later)

1. Open the **Microsoft Store**, search for **Python Install Manager**, and click **Install**.
   - Alternative: open Command Prompt or PowerShell and run `winget install 9NQ7512CXL7T`
   - Alternative: download it from https://www.python.org/downloads/windows/
2. Close any open terminal windows, then open a **new** Command Prompt or PowerShell.
3. Run `py --version`. If it offers to install Python, accept and follow the prompts.
4. Run `py --version` again. You should see something like `Python 3.x.x`.

### macOS

Pick one:

- **Installer:** download the macOS installer from https://www.python.org/downloads/, open it, and follow the prompts.
- **Homebrew** (if you already use it): run `brew install python`

Then open **Terminal** (press `Cmd + Space`, type `Terminal`, press Enter) and check:

```
python3 --version
```

### Linux

Python 3 is usually already installed. Check with:

```
python3 --version
```

If it is missing, install it for your distribution:

```
# Debian / Ubuntu / Mint
sudo apt update && sudo apt install python3

# Fedora
sudo dnf install python3

# Arch
sudo pacman -S python
```

---

## Step 2: Go to the project folder

First, put `grocery.py` and `main.py` together in one folder, for example a folder called `grocery-app` inside your Downloads. Then open a terminal in that folder.

### Windows

**Easy way:** open the folder in File Explorer, click the address bar at the top, type `cmd`, and press Enter. A Command Prompt opens already in the right folder. (On Windows 11 you can also right-click empty space in the folder and choose **Open in Terminal**.)

**Typing way:** open Command Prompt or PowerShell and run:

```
cd "%USERPROFILE%\Downloads\grocery-app"      (Command Prompt)
cd "$HOME\Downloads\grocery-app"              (PowerShell)
```

If the folder is on another drive (for example D:), use `cd /d D:\path\to\grocery-app` in Command Prompt.

Check you are in the right place by listing the files. You should see `main.py` and `grocery.py`:

```
dir
```

### macOS

Open Terminal, then either:

**Easy way:** type `cd` followed by a space, drag the `grocery-app` folder from Finder into the Terminal window, and press Enter.

**Typing way:**

```
cd ~/Downloads/grocery-app
```

Check you are in the right place:

```
ls
```

### Linux

Open a terminal (`Ctrl + Alt + T` on most systems, or right-click inside the folder in your file manager and choose **Open in Terminal**), then run:

```
cd ~/Downloads/grocery-app
ls
```

### Useful tips for all systems

- If a folder name contains spaces, put the whole path in quotes: `cd "My Files/grocery-app"`
- `cd ..` moves up one folder
- `pwd` shows your current location (macOS, Linux, and PowerShell). In Windows Command Prompt, run `cd` with nothing after it.

---

## Step 3: Run the app

From inside the project folder:

| OS | Command |
|----|---------|
| Windows | `py main.py` |
| macOS | `python3 main.py` |
| Linux | `python3 main.py` |

Example session:

```
Add grocery item (q to quit): milk
Are you sure? [(y)es/(n)o]: y
Your current list: ['milk']
Wanna remove an item? [(y)es/(n)o]: n
Add grocery item (q to quit): q
```

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `python` or `py` is "not recognized" (Windows) | Close the terminal, open a new one, and try again. If it still fails, repeat the Python install step. |
| `command not found: python3` (macOS/Linux) | Python is not installed. Repeat Step 1 for your OS. |
| `can't open file ... main.py` / `No such file or directory` | You are in the wrong folder. Run `dir` (Windows) or `ls` (macOS/Linux) and make sure you can see `main.py`, then use `cd` to get there. |
| `ModuleNotFoundError: No module named 'grocery'` | `grocery.py` is missing or is not in the same folder as `main.py`. Check the file name spelling. |
| Typing `q` does nothing | Make sure you are at the "Add grocery item" prompt. At the removal prompt, `q` only cancels removing. |