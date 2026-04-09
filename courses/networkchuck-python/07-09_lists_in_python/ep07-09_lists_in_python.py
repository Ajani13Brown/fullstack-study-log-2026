# ============================================================
# NetworkChuck Python Practice – Working with Lists
# Focus: list creation, indexing, adding items, removing items, conditional logic
# Episodes Covered: 7–9 (with support from Episodes 1–6 for logic and type conversion)
# Notes: Exercises are original and designed to reinforce list mastery
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Convert and Update Value
#
# You have a list of numbers stored as strings:
# numbers = ["10", "5", "8", "12", "3"]
#
# Remove the FIRST item from the list using pop().
# Convert it to an integer and add 5.
# Insert the new value back at the first position in the list.
#
# Print the updated first item.
# Print the full list after the update.
#
# Focus:
# - pop() to remove items
# - int() conversion
# - math operations
# - insert() to restore value
# ------------------------------------------------------------

# --- Solution ---
numbers = ["10", "5", "8", "12", "3"]
addition = int(numbers.pop(0)) + 5

numbers.insert(0,str(addition))
print(numbers)

# ------------------------------------------------------------
# Exercise 2: Number Extraction + Math
#
# You have a list of numbers stored as strings:
# numbers = ["4", "7", "10", "2", "8", "5"]
#
# Remove THREE numbers from the list.
# Convert them to integers and add them together.
#
# Print the total sum.
# Print the remaining list.
#
# Focus:
# - pop() to remove items
# - int() conversion
# - addition
# ------------------------------------------------------------

# --- Solution ---

numbers = ["4", "7", "10", "2", "8", "5"]
number_1 = numbers.pop(0)
number_2 = numbers.pop(0)
number_3 = numbers.pop(0)

print(int(number_1) + int(number_2) + int(number_3))
print(numbers)

# ------------------------------------------------------------
# Exercise 3: VIP Line Management
#
# You have a list representing a line of people:
# line = ["Sam", "Alex", "Taylor"]
#
# Ask the user to enter a name.
# If the name matches "Ben" (VIP), place them at the FRONT of the line.
# Otherwise, place them at the END of the line.
#
# Print the updated line.
#
# Focus:
# - input() for user data
# - if / else
# - insert() vs append()
# ------------------------------------------------------------

# --- Solution ---
line = ["Sam", "Alex", "Taylor"]

name = input("what is your name\n")

if name == "Ben":
    line.insert(0,name)
else:
    line.append(name)

print(line)


# ------------------------------------------------------------
# Exercise 4: Survival Kit Decision
#
# You have a list of survival tools:
# tools = ["rope", "knife", "map", "compass"]
#
# The user enters the type of trip they are going on:
# - "easy" for a simple trip
# - "dangerous" for a risky trip
#
# If the trip is "dangerous", remove "map" from the list.
# Otherwise, add "flashlight" to the list.
#
# Print the final list.
#
# Focus:
# - if / else
# - remove()
# - append()
# - logical reasoning for list updates
# ------------------------------------------------------------

# --- Solution ---
tools = ["rope", "knife", "map", "compass"]
trip = input("what kind of trip will you be going on?\n")

if trip == "dangerous":
    tools.remove("map")
else:
    tools.append("flashlight")

print(tools)


# ------------------------------------------------------------
# Exercise 5: Modify and Restore Value
#
# You have a list of numbers stored as strings:
# numbers = ["8", "12", "5", "20"]
#
# Remove the SECOND item from the list.
# Convert it to an integer and subtract 3.
# Put the new value back into the same position.
#
# Print the updated list.
#
# Focus:
# - pop() and insert()
# - int() conversion
# - basic math
# - list updates
# ------------------------------------------------------------

# --- Solution ---
numbers = ["8", "12", "5", "20"]
subtract = int(numbers.pop(1)) - 3
numbers.insert(1,str(subtract))
print(numbers)

# ------------------------------------------------------------
# Exercise 6: Cart Total Evaluation
#
# A shopping cart contains numbers stored as strings:
# cart = ["5", "12", "3", "7"]
#
# Convert all numbers to integers and calculate the total sum.
# Print the total sum.
#
# If the total is greater than 20, add "Heavy Cart" to the FRONT of the list.
# Otherwise, add "Light Cart" to the END of the list.
#
# Print the updated cart.
#
# Focus:
# - int() conversion
# - math with multiple list items
# - if / else
# - insert() vs append()
# ------------------------------------------------------------

# --- Solution ---

cart = ["5", "12", "3", "7"]

item_1 = int(cart[0])
item_2 = int(cart[1])
item_3 = int(cart[2])
item_4 = int(cart[3])

total = item_1 + item_2 + item_3 + item_4
print(total)

if total >= 20:
    cart.insert(0,"Heavy Cart")
else:
    cart.append("Light Cart")

print(total)
print(cart)

