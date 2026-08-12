#Typo Error
#age = 32
#print("My age is " + age)
#This produces a TypeError. Why? Because you're trying to do: string + integer



#Fix 1 — Convert the number
age = 32
print("My age is " + str(age))

#Fix 2 — Use an f-string
age = 32
print(f"My age is {age}")