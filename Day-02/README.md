# 🐍 Day 02 — Data Types, Mathematical Operations & Tip Calculator

Day 2 of my **100 Days of Python** journey.

Today I focused on understanding Python's basic data types, type conversion, mathematical operations, number manipulation, and formatted output.

## 📚 Topics Covered

* Primitive data types
* Type checking
* Type conversion
* Type errors
* Arithmetic operators
* Operator precedence
* Augmented assignment operators
* Number manipulation
* Rounding numbers
* F-strings
* Number formatting
* User input and calculations
* Building a Tip Calculator

## 🧠 Concepts Learned

### 1. Primitive Data Types

```python
str
int
float
bool
```

Examples:

```python
name = "Mohamed"
age = 32
height = 175.5
is_learning = True
```

### 2. Type Checking

Used `type()` to identify the data type of a value.

```python
print(type(age))
```

### 3. Type Conversion

Learned how to convert values between different data types.

```python
int()
float()
str()
```

Example:

```python
age = int("32")
price = float("99.99")
score = str(95)
```

### 4. Type Errors

Learned why Python cannot directly combine incompatible data types.

```python
age = 32

# This causes a TypeError:
# print("Age: " + age)
```

Correct approach:

```python
print(f"Age: {age}")
```

### 5. Mathematical Operations

Practiced:

```text
+     Addition
-     Subtraction
*     Multiplication
/     Division
//    Floor Division
%     Modulus
**    Exponentiation
```

### 6. Operator Precedence

Learned how Python determines the order of mathematical operations and how parentheses can change that order.

```python
result = 10 + 5 * 2
result = (10 + 5) * 2
```

### 7. Augmented Assignment

Learned shorthand assignment operators:

```python
score += 10
score -= 5
score *= 2
score /= 2
```

### 8. Number Manipulation

Practiced modifying and calculating values using variables and arithmetic operators.

### 9. Rounding Numbers

Learned how to round numerical values.

```python
round(99.9876, 2)
```

### 10. F-Strings

Learned how to insert variables and expressions directly into strings.

```python
name = "Mohamed"
age = 32

print(f"My name is {name} and I am {age} years old.")
```

### 11. Number Formatting

Learned how to control decimal places when displaying numbers.

```python
price = 99.9876

print(f"₹{price:.2f}")
```

Output:

```text
₹99.99
```

### 12. User Input and Calculations

Learned how to collect information from users and convert the input into the appropriate data type.

```python
age = int(input("How old are you? "))
```

## 🚀 Main Project — Tip Calculator

Built an interactive Tip Calculator that:

* Accepts the total bill
* Accepts the tip percentage
* Accepts the number of people
* Calculates the tip amount
* Calculates the total bill
* Splits the bill between people
* Displays the final amount with two decimal places

### Formula

```text
Tip Amount = Bill × Tip Percentage ÷ 100

Total Bill = Bill + Tip Amount

Amount Per Person = Total Bill ÷ Number of People
```

## 🧪 Extra Practice — Shopping Bill Calculator

Created an additional practice project to reinforce Day 2 concepts.

The program:

* Accepts product name
* Accepts product price
* Accepts quantity
* Accepts discount percentage
* Calculates subtotal
* Calculates discount amount
* Calculates final price
* Formats the final result to two decimal places

## 📁 Files

```text
Day-02/
│
├── 01_primitive_data_types.py
├── 02_type_checking.py
├── 03_type_conversion.py
├── 04_type_errors.py
├── 05_arithmetic_operators.py
├── 06_operator_precedence.py
├── 07_augmented_assignment.py
├── 08_number_manipulation.py
├── 09_rounding_numbers.py
├── 10_f_strings.py
├── 11_number_formatting.py
├── 12_user_input_calculations.py
├── 13_tip_calculator_logic.py
├── 14_tip_calculator.py
├── 15_shopping_bill_challenge.py
```

## 🎯 Day 2 Learning Outcome

By the end of Day 2, I can:

* Identify basic Python data types
* Check data types using `type()`
* Convert values between data types
* Understand and troubleshoot basic type errors
* Perform mathematical calculations
* Understand operator precedence
* Use augmented assignment operators
* Round and format numbers
* Use f-strings
* Work with user input
* Build simple calculation-based programs

## 📈 Progress

**100 Days of Python**

* Day 01 — ✅ Completed
* Day 02 — ✅ Completed
* Day 03 — ⬜ Next

**Progress: 2 / 100 days**

---

### Course

**100 Days of Code — The Complete Python Pro Bootcamp**

Instructor: Angela Yu

### Status

🟢 **Day 2 Completed**
