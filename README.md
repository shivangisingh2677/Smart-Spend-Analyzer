# Personal Expense Tracker

## Project Description
This is a Python-based command-line application developed to help students manage their monthly finances. It allows users to log daily expenses, categorizes them, and provides a real-time summary of total spending against a set budget.

## Features
- **Data Persistence:** Uses a CSV file to save data permanently.
- **Budget Tracking:** Automatically calculates remaining balance from a fixed monthly budget.
- **Input Validation:** Prevents the program from crashing if non-numeric amounts are entered.
- **Reporting:** Generates a clean, readable table of all expenses.

## Tech Stack
- Language: Python 3.x
- Libraries: `csv`, `os`, `datetime`

## How to Run
1. Ensure Python is installed on your system.
2. Clone this repository.
3. Open a terminal in the project folder.
4. Run the command: `python main.py`

## Project Structure
- `main.py`: The source code.
- `my_expenses.csv`: The database file (auto-generated).
- `screenshots/`: Folder containing proof of execution.