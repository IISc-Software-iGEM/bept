# Improvised CLI - BEPT
Bept - Beginner friendly Proteins analysis Electrostatics Tool 

## How to build the project on your system to run

### Step 1: Install `uv` on your system
- Downloading by copy-pasting to your Terminal:
For MacOS/Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For Windows(Powrshell)
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

If you don't want the above method and want to use your package manager - 

- For Arch Linux
```bash
sudo pacman -S uv
```

Find more here - https://docs.astral.sh/uv/getting-started/installation/

### Step2: Clone the repo
Clone the repository anywhere in your system.
```bash
git clone https://github.com/IISc-Software-iGEM/improvised-cli
```

## Running the code
Enter the cloned repository, it should have `pyproject.toml`, `src`, etc. Now run the command `uv run bept --help`. That's it :D.

Rest of the things have been shown in the demo. Play around and see how things work. 
