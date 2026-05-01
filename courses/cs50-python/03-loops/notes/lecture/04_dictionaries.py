# CS50 Python – Lecture 03: Dictionaries (Key-Value Access and Iteration)

# Focus:
# Accessing data in dictionaries using keys and iterating through key-value pairs.

# Purpose:
# Learn how to work with key-value data structures, retrieve values using keys,
# and iterate through dictionaries to process structured data efficiently.
#------------------------------------------------------------------------------------------------

# 1. Introduction to Dictionaries

# Dictionary:
# Stores data as key-value pairs, enabling access by key instead of index.
# Syntax: {key1: value1, key2: value2}

# Key: Immutable identifier used to retrieve a value
# Value: Data associated with a key (any data type)


students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"
            }


print(students["Hermione"])

#------------------------------------------------------------------------------------------------

# Loops with Dictionaries

# Version 1: Looping by Keys

# Goal:
# Use key iteration to access and print values from a dictionary

students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
            "Draco":"Slytherin"
            }

for student in students:
    print(student,students[student], sep =",")

# Insight:
# - Iterating over a dictionary returns keys by default
# - print(key) outputs only the key (e.g., student name)
# - print(key, dictionary[key]) uses the key to access and print its associated value
# - Syntax: dictionary[key] retrieves the value linked to that key



# Version 2: .items() Method

# .items() Method:
# Used to iterate through both keys and values in a dictionary at the same time.
# Syntax: for key, value in dictionary.items():
# Each iteration assigns the key and its corresponding value to separate variables


# Goal:
# Use .items() to iterate over key-value pairs directly

for student, house in students.items():
    print(student, house, sep = ",")

# Insight:
# - .items() allows unpacking into two variables directly in the loop (key, value)
# - Eliminates the need to access values separately using dictionary[key]
# - Leads to cleaner, more readable iteration when working with both key and value