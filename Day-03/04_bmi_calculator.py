# Day 3 - Control Flow
# Coding Exercise: BMI Calculator with Interpretations

# BMI is calculated using:
# BMI = weight / height²

# This exercise combines concepts learned on Day 2
# with the conditional statements learned on Day 3.

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height ** 2)

print("Your BMI is:", bmi)


# ---------------------------------------------------------
# BMI Interpretation
# ---------------------------------------------------------
#
# The BMI value can be interpreted using conditions.

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


# ---------------------------------------------------------
# Debugging Exercise
# ---------------------------------------------------------
#
# Common mistakes to watch for:
#
# 1. Using height instead of height ** 2.
# 2. Forgetting float() when decimal input is required.
# 3. Using = instead of == in a condition.
# 4. Putting BMI conditions in the wrong order.
#
# Example of incorrect calculation:
#
# bmi = weight / height
#
# Correct calculation:
#
# bmi = weight / (height ** 2)