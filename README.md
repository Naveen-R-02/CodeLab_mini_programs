# Python Security & Utility Scripts Collection

A collection of beginner-friendly Python scripts covering password security, password generation, file handling, regular expressions, keyboard event monitoring, and HTTP requests.

## Project Structure

```
├── filedir.py
├── gen_pass.py
├── key_loger.py
├── password.py
├── regex.py
├── request.py
└── year.py
```

---

## Scripts Included

### 1. filedir.py
Counts the number of Python (.py) files in a given directory.

**Features**
- Accepts a directory path from the user
- Scans the folder
- Counts Python files

**Example**
```bash
Enter the path of the file: C:\Projects
.py files in the directory: 12
```

---

### 2. gen_pass.py
Generates a secure random password using letters, numbers, and special characters.

**Features**
- Uses Python's `secrets` module
- Generates strong random passwords
- Includes special characters

**Example Output**
```bash
Generated password: J@8kLp#4zQ!9xT7mN$2A
```

---

### 3. key_loger.py
Monitors and displays keyboard key presses in real time.

**Features**
- Detects keyboard events
- Displays pressed keys
- Uses the `pynput` library

**Note**
This project is intended for educational and learning purposes only.

---

### 4. password.py
Basic password strength checker.

**Features**
- Checks password length
- Minimum requirement: 8 characters

**Example**
```bash
Enter your password: mypass
Password isn't lengthy enough
```

---

### 5. regex.py
Advanced password strength validation using Regular Expressions.

**Requirements**
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

**Example**
```bash
Enter your password: Strong@123
Password is strong
```

---

### 6. request.py
Makes an HTTP GET request and displays response information.

**Features**
- Sends web requests
- Displays response headers
- Displays status code

**Example Output**
```bash
200
```

**Note**
The script may require correction to use the `requests` library properly.

---

### 7. year.py
Generates password combinations using:
- Name
- Birth year
- Common password patterns

**Example**
```bash
Enter your name: John
Enter your birth year: 2005
John2005123
John2005@123
John123
```

---

## Requirements

Install required packages:

```bash
pip install pynput requests
```

---

## Running the Scripts

```bash
python filename.py
```

Example:

```bash
python gen_pass.py
```

---

## Learning Concepts Covered

- Python Basics
- Loops
- Conditional Statements
- String Manipulation
- File Handling
- Regular Expressions
- HTTP Requests
- Keyboard Event Handling
- Password Security Concepts

---

## Disclaimer

These scripts were created for educational and learning purposes only. Users are responsible for complying with all applicable laws, regulations, and organizational policies when running or modifying them.

---

## Author

**Naveen R**

Bachelor of Computer Applications   
Nitte Institute of Professional Education
CodeLab systems

---
If you found these scripts useful, consider starring the repository.
