# Day 13 — Debugging
This day focuses on learning how to identify, reproduce, investigate, and fix bugs in Python programs.

---

## 🎯 Learning Objectives

By the end of Day 13, I learned how to:

- Describe a programming problem clearly
- Reproduce bugs consistently
- Trace code execution line by line
- Read Python error messages
- Identify syntax errors
- Identify logic errors
- Use `print()` for debugging
- Use breakpoints and a debugger
- Inspect variable values during execution
- Test edge cases
- Fix problems systematically
- Verify that a fix actually works

---

## 📚 Topics Covered

### 1. Describe the Problem
Before changing code, clearly identify:

- What did I expect?
- What actually happened?
- Where is the difference?

### 2. Reproduce the Bug
Run the program with the same input that causes the problem.
A bug that can be reproduced is much easier to investigate.

### 3. Play Computer
Manually trace the program line by line and track how variable values change.

### 4. Fix Errors and Red Underlines
Learn to recognize common Python errors such as:

- `SyntaxError`
- `NameError`
- `TypeError`
- `IndexError`
- `KeyError`

### 5. Debug Using `print()`
Use temporary print statements to inspect variable values and program flow.

Example:
```python
print("DEBUG:", variable)

6. Use a Debugger

Use VS Code debugging tools such as:
Breakpoints
Step Over
Step Into
Variable inspection

7. Final Debugging Tips
Important debugging principles:
Read the error message.
Reproduce the problem.
Don't change multiple things at once.
Check your assumptions.
Inspect variable values.
Reduce the problem.
Test edge cases.
Fix the root cause.
Retest after fixing.