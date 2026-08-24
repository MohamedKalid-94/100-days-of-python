#Exercise 13 — Debugging Leap Year

#Problem: 
#The original program incorrectly assumed that every year divisible by 4 is a leap year.

#Bug:
#Century years require additional logic.


year = int(input("Enter the Year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")