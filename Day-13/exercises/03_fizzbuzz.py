#Exercise 14 — Debugging FizzBuzz

#Problem: The FizzBuzz program contained a logic error caused by the order of the conditions.
#Bug: The program checked divisibility by 3 before checking divisibility by both 3 and 5.

for number in range(1, 101):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")

    elif number % 5 == 0:
        print("Buzz")

    elif number % 3 == 0:
        print("Fizz")

    else:
        print(number)