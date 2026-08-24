#Exercise 12 — Debugging Odd or Even
#Problem: The original program contained a syntax error while checking whether a number was even or odd.
#Bug: The equality comparison operator was incorrectly written as:

#= instead of: ==

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")