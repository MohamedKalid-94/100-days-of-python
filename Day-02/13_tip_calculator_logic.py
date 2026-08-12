#Before writing the complete project, understand the mathematics.
#Bill = ₹1000 and Tip = 10%

#Calculate the tip:
bill = 1000
tip_percentage = 10
tip = bill * tip_percentage / 100
print(tip)

#Result: 100

#Calculate the total:
total_bill = bill + tip
print(total_bill)

#Result: 1100

#Now split between 2 people:

number_of_people = 2
amount_per_person = total_bill / number_of_people
print(amount_per_person)

#Result: 550

#So the complete mathematical logic is:
#Tip = Bill × Tip% ÷ 100
#Total = Bill + Tip
#Per Person = Total ÷ Number of People

#Understand this before touching the final project.