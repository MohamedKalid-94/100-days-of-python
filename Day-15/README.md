# ☕ Day 15 - Coffee Machine

## 📌 Project Overview
Day 15 of my **#100DaysOfCode** Python journey.

In this project, I built a fully functional **Coffee Machine** program using Python.

The program allows users to:

- Choose a coffee
- Check available ingredients
- Insert coins
- Calculate payment
- Check whether payment is sufficient
- Calculate and return change
- Deduct ingredients after a successful purchase
- Track the machine's money
- Display a resource report
- Turn the machine off

---

## 🎯 Concepts Practiced

- Functions
- Function parameters
- Return values
- Dictionaries
- Nested dictionaries
- Dictionary iteration
- Variables
- Variable scope
- `while` loops
- `if / elif / else`
- User input
- Arithmetic operations
- String formatting
- Program state management
- Input validation
- Debugging
- Resource management

---

## 🧠 How the Program Works

The coffee machine follows this process:

```text
User selects coffee
        ↓
Check if coffee is valid
        ↓
Check available resources
        ↓
Display coffee cost
        ↓
Process coins
        ↓
Check payment
        ↓
Payment sufficient?
     /       \
   Yes        No
    ↓          ↓
Add money    Refund
    ↓
Calculate change
    ↓
Deduct ingredients
    ↓
Serve coffee