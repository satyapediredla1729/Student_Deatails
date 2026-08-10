# Student Details

A simple console-based Student Management System built in Python. It lets you add, view, search, remove, and analyze student records — all stored in memory using a nested dictionary. No external libraries or database required.

## Features

- **Add Student** – Enter roll number, name, age, three subject marks (0–20 each), and section. Duplicate roll numbers are rejected.
- **Display Student** – View all stored student records.
- **Search Student** – Look up a student's full details by roll number.
- **Remove Student** – Delete a student record by roll number.
- **Show Class Topper** – Calculates total marks for each student and displays the one with the highest score.
- **Display Unique Sections** – Shows all distinct sections currently in use.
- **Exit** – Ends the program.

## Requirements

- Python 3.x
- No third-party packages needed (uses only built-in Python)

## How to Run

python studentdetails.py

or, depending on your setup:

python3 studentdetails.py

## Usage

On running the script, you'll see a menu:

1. Add student
2. Display student
3. Search student
4. Remove student
5. Show class Topper
6. Display unique Section
7. Exit

Enter a number from 1–7 to choose an action, and follow the on-screen prompts.

### Example: Adding a Student

Enter your Roll No: 103
enter your name: ravi
enter your age: 20
enter marks: 18
enter marks: 19
enter marks: 20
enter your section: c
student added successfully!

## Data Structure

Each student record is stored as a dictionary inside the main Student_Data dictionary, keyed by roll number:

Student_Data = {
    101: {
        "name": "satya",
        "age": 19,
        "marks": (19, 20, 20),
        "section": "A",
    },
    102: {
        "name": "shiva",
        "age": 19,
        "marks": (15, 14, 20),
        "section": "B",
    }
}

- marks is stored as a tuple of 3 integers, each between 0 and 20.
- section is automatically converted to uppercase.

## Notes / Limitations

- Data is stored in memory only — all records are lost when the program exits (no file or database persistence).
- Two sample students (roll numbers 101 and 102) are pre-loaded when the script starts.
- Input validation covers non-numeric entries (via try/except) and out-of-range marks, but does not currently prevent empty name/section fields.

## License

Feel free to use, modify, and distribute this project for learning purposes.
