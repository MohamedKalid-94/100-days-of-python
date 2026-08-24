🐛 Day 13 — Final Debugging Tips
You've learned how to find a bug. Now we need to build the habit of fixing bugs systematically.

1. Don't panic when you see an error
An error is not your enemy.

For example: print(name)

If name doesn't exist, Python gives you a NameError.
Don't randomly change code.

Read the error:
NameError
   ↓
Which line?
   ↓
Which variable?
   ↓
Why doesn't it exist?

Error messages are clues.

2. Read the traceback from the bottom

When Python gives you something like:

Traceback (most recent call last):
  File "main.py", line 10, in <module>
    print(result)
NameError: name 'result' is not defined

The most useful part is usually the last line:
NameError: name 'result' is not defined

Then look at the indicated line.
Don't stare at the whole traceback and get overwhelmed.

3. Check your assumptions
This is a big one.

Suppose:
age = 18

if age > 18:
    print("Adult")

You might think:
"Why isn't it printing Adult?"
Python isn't wrong.
Your assumption was wrong.

You wrote:
age > 18

But perhaps you intended:
age >= 18
Your program may be doing exactly what you told it to do.

4. Check the value, not just the code
If something looks wrong:

print("DEBUG:", variable)
Ask:
What did I expect?
What did I actually get?

For example:
score = 0
print("DEBUG score:", score)
If you expected 50 and got 0, now you've narrowed the problem.

5. Reduce the problem
This is a powerful engineering habit.
If you have:
500 lines of code
and something breaks, don't stare at all 500 lines.
Find the smallest section that reproduces the problem.

500 lines
    ↓
100 lines
    ↓
20 lines
    ↓
5 lines
    ↓
FOUND IT

This is often called creating a minimal reproducible example.

6. Change one thing at a time

Bad debugging:

Change condition
Change variable
Rewrite loop
Add function
Change input
Run

It works.

Now you don't know which change fixed it.

Better:

Hypothesis
   ↓
One change
   ↓
Run
   ↓
Observe

Then repeat.

7. Test edge cases
Don't only test the obvious case.
The edge cases exposed the bugs.
That's not coincidence.

8. Don't fix the symptom
This is important for your engineering career.

Suppose:
result = something()
throws an error.
You shouldn't immediately do something like:

try:
    result = something()
except:
    result = 0

just to make the red error disappear.
You may have hidden the actual bug.
A proper fix addresses the root cause.

9. After fixing, retest
Never think:
"I changed the line, so it's fixed."
Think:

Fix
 ↓
Run
 ↓
Original failing case
 ↓
Edge cases
 ↓
Normal cases
 ↓
PASS

That's how you know the fix actually worked.

🧠 Building Confidence
This is the final mindset lesson.
You will eventually encounter code where you think:
"I have no idea what's happening."
That's normal.
Don't jump straight to:
"I'm bad at Python."

Instead:
I don't understand the behavior yet.
        ↓
I can reproduce it.
        ↓
I can inspect the values.
        ↓
I can trace execution.
        ↓
I can isolate the problem.
        ↓
I can test a hypothesis.
        ↓
I can fix it.

That's debugging confidence.
Not knowing the answer immediately isn't the problem.
Being unable to systematically find the answer is the problem.
And you're already practicing that process.