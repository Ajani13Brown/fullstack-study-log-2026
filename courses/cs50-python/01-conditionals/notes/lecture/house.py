# -------------------------------------------------------------------------
# CS50 Python – Lecture 01: Conditionals - Match

# This file explores conditional logic using both if/elif/else and match-case
# -------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------
# Version 1: if / elif / else approach

# - Best suited when evaluating different types of conditions


name = input("What is your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Syltherin")
else:
    print("Who?")


# ----------------------------------------------------------------------------------------------------------
# Version 2: match / case approach

# The match statement (Python 3.10+) is used to compare a single value
# against multiple possible patterns in a clean and readable way.

# Syntax:
# - match variable:
# - case "value1" | "value2":
# - case _:

# Notes:
# - match evaluates one variable against multiple fixed values
# - use "|" to check multiple values in the same case
# - case _ acts as a default for anything not matched above
# - match is cleaner when comparing one variable to many exact values


name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Syltherin")
    case _:
        print("Who?")