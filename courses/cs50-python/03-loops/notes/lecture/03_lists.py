# CS50 Python – Lecture 03: Lists (Indexing and Iteration)

# Focus:
# Accessing elements in lists using indexing and iterating through list data.

# Purpose:
# Learn how to work with ordered collections, access specific elements,
# and combine lists with loops to process multiple values efficiently.
#------------------------------------------------------------------------------------------------

# 1. Lists and list indexing

# List:
# An ordered, mutable collection of values stored in a single variable.
# Syntax: [item1, item2, item3] (e.g., [0, 1, 2])

# Key Characteristics:
# - Ordered (index-based access)
# - Mutable (can be modified)
# - Allows duplicates
# - Can store multiple data types

students = ["Hermione","Harry","Ron"]

# Indexing (Lists):
# Indexing is used to access individual elements in a list by their position.
# Syntax: list[index] (e.g., my_list[0])

print(students[0])
print(students[1])
print(students[2])

# Insight:
# - Lists organize collections of related data into a structured format for easier processing
# - Indexing allows efficient, direct access to specific elements by position

#-----------------------------------------------------------------------------------------------------------

# 2. List Iteration

# Goal:
# Print each student name by iterating through the list

for student in students:
    print(student)


# Insight:
# - Lists can be traversed using a for loop to access each element sequentially

#-----------------------------------------------------------------------------------------------------------

# 3. len function

# len() function:
# - returns the number of items (length) of an object
# - always returns an integer
# - can be used with many data types (e.g., string, list, dictionary)

# Goal:
# Print students in academic order using their index positions
# (e.g., 1: Hermione, 2: Harry, ...)

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):  
    print(i + 1, students[i], sep=": ") 


# Insight:
# - len(students) returns 3; range(len(students)) becomes range(3), generating indices 0, 1, 2
# - len() is evaluated first and passed into range()
# - students[i] uses the index to access each element