"""
BMI Calculator - OIBSIP Python Programming Task 2
--------------------------------------------------
Features:
    1. Prompts user for weight (kg) and height (m).
    2. Calculates Body Mass Index (BMI).
    3. Classifies BMI into WHO standard categories:
         - Underweight  : BMI < 18.5
         - Normal       : 18.5 <= BMI < 25.0
         - Overweight   : 25.0 <= BMI < 30.0
         - Obese        : BMI >= 30.0
    4. Displays the result and category clearly.
    5. Handles invalid inputs gracefully (letters, negatives, zero).
    6. Allows the user to calculate multiple times without restarting.

Run:
    python bmi_calculator.py
"""


def get_positive_float(prompt):
    """Keep asking until the user enters a valid positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")


def calculate_bmi(weight_kg, height_m):
    """Return BMI rounded to 2 decimal places."""
    return round(weight_kg / (height_m ** 2), 2)


def classify_bmi(bmi):
    """Return the WHO BMI category and a short health note."""
    if bmi < 18.5:
        return "Underweight", "Consider consulting a doctor about healthy weight gain."
    elif bmi < 25.0:
        return "Normal weight", "Great! You are within the healthy weight range."
    elif bmi < 30.0:
        return "Overweight", "Consider a balanced diet and regular exercise."
    else:
        return "Obese", "Please consult a healthcare professional for guidance."


def display_result(weight, height, bmi, category, note):
    """Print a neatly formatted result."""
    print("\n" + "=" * 45)
    print("         BMI CALCULATION RESULT")
    print("=" * 45)
    print(f"  Weight        : {weight} kg")
    print(f"  Height        : {height} m")
    print(f"  BMI           : {bmi}")
    print(f"  Category      : {category}")
    print(f"  Health Note   : {note}")
    print("=" * 45 + "\n")


def main():
    print("=" * 45)
    print("   BMI Calculator - OIBSIP Python Task 2")
    print("=" * 45)
    print("  BMI Categories (WHO Standard):")
    print("  < 18.5          -> Underweight")
    print("  18.5 - 24.9     -> Normal weight")
    print("  25.0 - 29.9     -> Overweight")
    print("  >= 30.0         -> Obese")
    print("=" * 45 + "\n")

    while True:
        weight = get_positive_float("Enter your weight in kilograms (e.g. 70): ")
        height = get_positive_float("Enter your height in meters   (e.g. 1.75): ")

        bmi = calculate_bmi(weight, height)
        category, note = classify_bmi(bmi)
        display_result(weight, height, bmi, category, note)

        again = input("Calculate again? (yes / no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nThank you for using the BMI Calculator. Stay healthy!")
            break


if __name__ == "__main__":
    main()
