# QuizGen 🧠

**QuizGen** is a Python tool that helps you quickly create command-line quizzes and convert them into standalone `.exe` files using [PyInstaller](https://pyinstaller.org/). It's useful for making lightweight educational tools, revision utilities, or testing modules — all without needing a GUI.

---

## 📦 What It Does

- Prompts the user for questions and answers
- Generates a Python quiz script (`quizname.py`)
- Automatically compiles the script into a Windows executable (`quizname.exe`)
- Cleans up PyInstaller folders to keep things neat

---

## 🧩 How It Works

1. 📋 **Create a `qtree`**: A dictionary structure holding your questions and answers.
2. 🐍 **Convert to Python**: Generates a Python script from the `qtree`.
3. ⚙️ **Compile with PyInstaller**: Turns the Python script into an `.exe` file.
4. 🧹 **Cleanup**: Removes temporary folders and files (`dist/`, `build/`, `.spec`, etc.)

---

## 🚀 Getting Started

### 📌 Requirements
- Python 3.10 or above
- [PyInstaller](https://pypi.org/project/pyinstaller/)

Install PyInstaller:
```bash
pip install pyinstaller
