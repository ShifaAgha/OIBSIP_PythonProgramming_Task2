# BMI Calculator — OIBSIP Python Programming, Task 2

A simple command-line Body Mass Index (BMI) calculator built in Python.
No external libraries needed — runs on any machine with Python 3 installed.

## Features

- Prompts user for weight (kg) and height (m)
- Calculates BMI using the standard formula: `BMI = weight / height²`
- Classifies result into WHO standard categories:
  - Underweight (BMI < 18.5)
  - Normal weight (18.5 – 24.9)
  - Overweight (25.0 – 29.9)
  - Obese (≥ 30.0)
- Displays a health note alongside the result
- Handles invalid inputs (letters, negative numbers, zero) gracefully
- Allows multiple calculations in a single session

## How to Run

No installation needed. Just run:

```bash
python bmi_calculator.py
```

## Example Output

```
=============================================
   BMI Calculator - OIBSIP Python Task 2
=============================================
  BMI Categories (WHO Standard):
  < 18.5          -> Underweight
  18.5 - 24.9     -> Normal weight
  25.0 - 29.9     -> Overweight
  >= 30.0         -> Obese
=============================================

Enter your weight in kilograms (e.g. 70): 70
Enter your height in meters   (e.g. 1.75): 1.75

=============================================
         BMI CALCULATION RESULT
=============================================
  Weight        : 70.0 kg
  Height        : 1.75 m
  BMI           : 22.86
  Category      : Normal weight
  Health Note   : Great! You are within the healthy weight range.
=============================================
```

## Project Structure

```
ShifaAgha_Task2/
├── bmi_calculator.py   # main program
└── README.md           # this file
```

## Key Concepts Used

- User input handling with `input()`
- Error handling with `try/except` (ValueError for non-numeric input)
- Functions for clean, modular code
- Conditional logic for BMI classification
- Loops for repeated calculations and input validation

## Author

Shifa Agha — OIBSIP Python Programming Internship
GitHub: https://github.com/ShifaAgha/OIBSIP
