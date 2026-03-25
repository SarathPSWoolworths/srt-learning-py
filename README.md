# SRT Learning - Python

A simple Python project to learn the basics of Python and Flask.

---

## Prerequisites

- macOS
- [Homebrew](https://brew.sh/) installed

---

## 1. Install Python

```bash
# Install Python using Homebrew
brew install python

# Verify installation
python3 --version
```

---

## 2. Set Up the Project

```bash
# Clone or navigate to the project folder
cd srt-learning-py

# Create a virtual environment (keeps packages isolated from your system)
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

> **Note:** You'll see `(venv)` in your terminal when the virtual environment is active.

---

## 3. Run the Interactive Pyramid Script

```bash
# Make sure you're in the project folder
python3 hello.py
```

**Expected behavior:**
```
Enter a single character (or type 'exit'/'quit' to stop): *
Enter pyramid length (1 to 50): 4
Input symbol: *
Pyramid length: 4
Pyramid structure:
  *
  * *
 * * *
* * * *
```

The script runs in a loop and only exits when you type `exit` or `quit`.

---

## 4. Run the Flask API

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start the Flask server
python3 app.py
```

**Expected output:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

## 5. Test the API

Open a **new terminal** and run:

```bash
curl http://localhost:5000/health
```

**Expected output:**
```json
{
  "message": "Hello World"
}
```

Or open http://localhost:5000/health in your browser.

---

## Project Structure

```
srt-learning-py/
├── venv/              # Virtual environment (do not edit)
├── hello.py           # Interactive colored pyramid script
├── app.py             # Flask API with /health endpoint
├── requirements.txt   # Python package dependencies
├── .gitignore         # Files excluded from Git
└── README.md          # This file
```

---

## Useful Commands

| Command | What it does |
|---|---|
| `source venv/bin/activate` | Activate virtual environment |
| `deactivate` | Deactivate virtual environment |
| `pip install <package>` | Install a Python package |
| `pip freeze > requirements.txt` | Save installed packages to file |
| `python3 <file.py>` | Run a Python script |
| `ctrl + c` | Stop the Flask server |
