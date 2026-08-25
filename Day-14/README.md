# Day 14 - Higher/Lower Followers Game

## 📌 Project Overview

Day 14 of my Python learning journey.

In this project, I built a Higher/Lower style game where the player compares two randomly selected social media accounts and predicts which account has more followers.

The game also supports a tie when both accounts have the same number of followers.

---

## 🎯 Objective

The player is shown two accounts:

- Account A
- Account B

The player must predict:

- `A` → Account A has more followers
- `B` → Account B has more followers
- `T` → Both accounts have the same number of followers

The player earns one point for every correct answer.

The game ends when:

1. The player gives a wrong answer, or
2. The player reaches the maximum score of 5.

---

## 🧠 Python Concepts Practiced

### 1. Dictionaries

Each account is represented using a dictionary.

```python
{
    "name": "Instagram",
    "followers": 1000000,
    "description": "Social media platform",
    "country": "USA"
}