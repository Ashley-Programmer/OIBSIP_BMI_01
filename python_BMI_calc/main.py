def calculate_bmi(weight, height):
    return weight / (height ** 2) # formula: weight / height^2


def classify_bmi(bmi): # Return the category based on BMI value
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"


def main_bmi_calculator():
    print("=== Welcome to the BMI Calculator ===")
    try:
        weight = float(input(f"Enter your weight in kilograms (e.g. 70): "))
        height = float(input(f"Enter your height in meters (e.g. 1.75): "))

        # Check for valid input values
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        # Show result
        print("\n=== Result ===")
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Health Category: {category}")

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    print("\nThank you for using the BMI Calculator!")

# Run the program
if __name__ == "__main__":
    main_bmi_calculator()
