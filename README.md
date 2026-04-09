# Password Strength Analyzer with Hashing

## Description
A simple Python command-line project that analyzes password strength based on common security rules and then hashes the password using SHA-256.

## Features
- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects digits
- Detects special characters
- Classifies password as Weak / Medium / Strong
- Gives suggestions to improve password strength
- Confirms password input
- Hashes password using SHA-256
- Verifies password again using hash comparison

## Technologies Used
- Python
- hashlib (built-in Python library)

## How It Works
1. User enters a password
2. Program analyzes the password
3. Password strength is displayed
4. Suggestions are shown if needed
5. User confirms the password
6. Password is hashed using SHA-256
7. User re-enters password for verification
8. Program compares hashes for login check


## How to Run
```bash
python password_checker.py


## Sample Output

Enter the password: Hello@123

Password Analysis:
Length: 9
Uppercase: 1
Lowercase: 4
Digits: 3
Special Characters: 1

Password Strength: Strong

Suggestions:
- No improvements needed

## What I Learned

- How to analyze strings in Python
- How to count uppercase, lowercase, digits, and special characters
- How to build a simple CLI-based validation tool
- Basics of password hashing using SHA-256
