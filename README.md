## OIBSIP_BMI_01
# BMI Calculator
Beginner Python BMI Calculator

A simple, interactive Body Mass Index (BMI) calculator written in Python that helps users calculate their BMI and determine their health category based on standard WHO classifications.

## Features

- **Accurate BMI Calculation**: Uses the standard BMI formula: `BMI = weight / height²`
- **Health Classification**: Categorizes BMI results according to WHO guidelines
- **Input Validation**: Ensures valid, positive numeric inputs
- **Error Handling**: Gracefully handles invalid inputs with clear error messages
- **User-Friendly Interface**: Clean, interactive command-line interface with helpful prompts

## BMI Categories

The calculator uses the following standard BMI classifications:

| BMI Range | Category |
|-----------|----------|
| < 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25.0 - 29.9 | Overweight |
| ≥ 30.0 | Obese |

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Download the `main.py` file
2. Ensure you have Python installed on your system

## Usage

### Running the Calculator

```bash
python main.py
```

### Input Format

- **Weight**: Enter your weight in kilograms (e.g., 70)
- **Height**: Enter your height in meters (e.g., 1.75)

### Example Usage

```
=== Welcome to the BMI Calculator ===
Enter your weight in kilograms (e.g. 70): 70
Enter your height in meters (e.g. 1.75): 1.75

=== Result ===
Your BMI is: 22.86
Health Category: Normal weight

Thank you for using the BMI Calculator!
```

## Code Structure

The calculator consists of three main functions:

- `calculate_bmi(weight, height)`: Performs the BMI calculation
- `classify_bmi(bmi)`: Determines the health category based on BMI value
- `main_bmi_calculator()`: Handles user interaction and program flow

## Input Validation

The calculator includes comprehensive input validation:

- Checks for positive numbers only
- Handles non-numeric inputs gracefully
- Provides clear error messages for invalid inputs
- Prevents division by zero or negative values

## Important Notes

⚠️ **Medical Disclaimer**: BMI is a general health indicator and may not be accurate for:
- Athletes or individuals with high muscle mass
- Elderly individuals
- Children and adolescents (different BMI charts apply)
- Individuals with certain medical conditions

BMI should not be used as the sole indicator of health. Consult with healthcare professionals for comprehensive health assessments.

## Unit Conversions

If you need to convert your measurements:

**Weight Conversions:**
- Pounds to kg: divide by 2.205
- Example: 154 lbs ÷ 2.205 = 70 kg

**Height Conversions:**
- Feet/inches to meters: 
  - Example: 5'9" = (5 × 12 + 9) inches = 69 inches
  - 69 inches × 0.0254 = 1.75 meters

## Example Calculations

| Height | Weight Range (Normal BMI) |
|--------|---------------------------|
| 1.60m (5'3") | 47-64 kg (104-141 lbs) |
| 1.70m (5'7") | 53-72 kg (117-158 lbs) |
| 1.80m (5'11") | 60-81 kg (132-178 lbs) |

## Contributing

Feel free to submit issues or pull requests to improve the calculator. Potential enhancements could include:

- GUI interface
- Imperial unit support
- BMI tracking over time
- Additional health metrics

## License

This project is open source and available under the [MIT License](LICENSE).

---
