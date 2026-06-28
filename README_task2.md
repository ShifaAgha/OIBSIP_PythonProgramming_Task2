# BMI Calculator — OIBSIP Python Programming Task 2

A simple command-line **Body Mass Index (BMI)** calculator built using Python. This application calculates BMI based on a user's weight and height, classifies the result according to **WHO (World Health Organization)** standards, and provides a brief health note.



## Features

* Accepts user weight (in kilograms) and height (in meters)
* Calculates BMI using the standard formula:

  ```
  BMI = weight / (height²)
  ```
* Classifies BMI according to WHO standards:

  * **Underweight** (BMI < 18.5)
  * **Normal weight** (18.5–24.9)
  * **Overweight** (25.0–29.9)
  * **Obese** (BMI ≥ 30.0)
* Displays a health note based on the BMI category
* Validates user input and handles invalid entries gracefully
* Allows users to perform multiple BMI calculations in a single session

## How to Run

Run the program using Python:

```bash
python bmi_calculator.py
```

## Example Output

```text
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
Enter your height in meters (e.g. 1.75): 1.75

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

```text
ShifaAgha_Task2/
├── bmi_calculator.py
└── README.md
```

## Key Concepts Used

* User input using `input()`
* Input validation
* Exception handling with `try`/`except`
* Functions for modular programming
* Conditional statements (`if`, `elif`, `else`)
* Loops for repeated calculations

## Author

**Shifa Agha**
OIBSIP Python Programming Internship

GitHub: https://github.com/ShifaAgha/OIBSIP
