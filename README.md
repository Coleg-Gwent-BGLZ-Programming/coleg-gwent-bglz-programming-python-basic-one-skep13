[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/jdhXoo2o)
[![Work in MakeCode](https://classroom.github.com/assets/work-in-make-code-8824cc13a1a3f34ffcd245c82f0ae96fdae6b7d554b6539aec3a03a70825519c.svg)](https://classroom.github.com/online_ide?assignment_repo_id=20600512&assignment_repo_type=AssignmentRepo)
# 🐍 Python Basics: Input/Output and Core Data Structures
## 📘 Overview

This repository contains beginner-friendly Python examples designed to help learners understand:

- Input and output statements
- String concatenation and formatted strings
- Lists, Tuples, Sets, and Dictionaries

These examples are ideal for Level 2 learners starting their journey with Python programming.

---

## 🧑‍💻 Part 1: Input and Output

### 🔹 Concepts:
- `input()` for user input
- `print()` for displaying output
- String concatenation using `+`
- Formatted strings using `f""`

### 💡 Example:

```python
name = input("What is your name? ")
age = input("How old are you? ")

# Using concatenation
print("Hello " + name + ", you are " + age + " years old.")

# Using formatted strings
print(f"Hello {name}, you are {age} years old.")
```
### 🧠 Explanation:

- input() collects user input as a string.
- Concatenation joins strings using the + operator.
- Formatted strings (f"") allow variables to be embedded directly into the output, making code cleaner and easier to read.

## 📋 Part 2: Lists
### 🔹 Concepts Covered:

- Lists are ordered and mutable collections.
- Accessing elements by index.
- Adding items using append().
- Looping through lists with for.

###💡 Code Example:

```python
# Create a list of fruits
fruits = ["apple", "banana", "cherry"]

# Access the first item
print(f"The first fruit is {fruits[0]}")

# Add a new fruit
fruits.append("orange")
print(f"Updated list: {fruits}")

# Loop through the list
for fruit in fruits:
    print(f"I like {fruit}")
```
### 🧠 Explanation:

- Lists use square brackets [].
- Indexing starts at 0.
- append() adds an item to the end of the list.
- Loops allow you to process each item individually.

## 📦 Part 3: Tuples
### 🔹 Concepts Covered:

- Tuples are ordered but immutable collections.
- Useful for storing fixed data.
- Tuple unpacking allows multiple variables to be assigned at once.

### 💡 Code Example:

```python
# Create a tuple
coordinates = (10, 20)

# Access elements
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuple unpacking
x, y = coordinates
print(f"x = {x}, y = {y}")
```
### 🧠 Explanation:

- Tuples use parentheses ().
- Once created, their values cannot be changed.
- Tuple unpacking is a clean way to assign multiple values at once.

## 🎨 Part 4: Sets
### 🔹 Concepts Covered:

- Sets are unordered collections of unique items.
- Duplicate values are automatically removed.
- Use add() to insert new items.

### 💡 Code Example:

```python
# Create a set
colors = {"red", "green", "blue", "red"}  # 'red' appears only once

print(f"Unique colors: {colors}")

# Add a new color
colors.add("yellow")
print(f"Updated colors: {colors}")
```
### 🧠 Explanation:

- Sets use curly braces {}.
- They automatically remove duplicates.
- Sets are useful for checking membership and ensuring uniqueness.

## 🗂️ Part 5: Dictionaries
### 🔹 Concepts Covered:

- Dictionaries store data as key-value pairs.
- Keys must be unique.
- Values can be accessed and updated using keys.

### 💡 Code Example:

```python
# Create a dictionary
student = {
    "name": "Alice",
    "age": 17,
    "grade": "B"
}

# Access values
print(f"{student['name']} is {student['age']} years old and got grade {student['grade']}.")

# Update a value
student["grade"] = "A"
print(f"Updated grade: {student['grade']}")
```
### 🧠 Explanation:

- Dictionaries use curly braces {} with key: value pairs.
- You access values using dictionary[key].
- You can update values by assigning a new one to a key.
