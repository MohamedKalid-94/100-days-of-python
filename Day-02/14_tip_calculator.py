# Day 2 Project - Tip Calculator

print("================================")
print("       TIP CALCULATOR")
print("================================")

# Get information from the user

bill = float(input("What was the total bill? ₹"))

tip_percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? ")
)

number_of_people = int(
    input("How many people are splitting the bill? ")
)

# Calculate the tip

tip_amount = bill * tip_percentage / 100

# Calculate the total bill

total_bill = bill + tip_amount

# Calculate the amount each person should pay

amount_per_person = total_bill / number_of_people

# Display the results

print()
print("================================")
print("           BILL SUMMARY")
print("================================")

print(f"Original bill: ₹{bill:.2f}")
print(f"Tip amount: ₹{tip_amount:.2f}")
print(f"Total bill: ₹{total_bill:.2f}")
print(f"Number of people: {number_of_people}")
print(f"Amount per person: ₹{amount_per_person:.2f}")

print("================================")