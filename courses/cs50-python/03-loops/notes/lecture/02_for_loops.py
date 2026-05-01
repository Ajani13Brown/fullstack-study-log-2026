# CS50 Python – Lecture 03: Loops (For Loops)

# Focus:
# Using for loops to simplify repetition by iterating over sequences and ranges
# (e.g., printing "meow" a set number of times).

# Purpose:
# Understand iteration-based execution, cleaner loop syntax, and when to use
# for loops instead of while loops through follow-along notes and code experiments.
#------------------------------------------------------------------------------------------------

# Version 1: Introduction to for loops

# For Loop:
# A for loop iterates over each item in a sequence (such as a list or range),
# executing a block of code once per item in the sequence.



for i in [0,1,2]:
    print("meow")

# Insight:
# - Syntax: for variable in sequence: (e.g., for i in [0, 1, 2]:)
# - Executes the indented block once per item in the sequence

#--------------------------------------------------------------------------------------------------

# Version 2: For loops using range function

# Range:
# The range() function generates a sequence of integers for iteration in loops.
# Syntax: range(start, stop[, step]) — includes start, excludes stop.
# Defaults: start = 0, step = 1; range(n) produces n values from 0 to n-1.
# The step controls how values change (positive for forward, negative for backward).
# Only integer arguments are allowed.

for _ in range(3):
    print("meow")

# Insight:
# - range(3) generates values 0, 1, 2, controlling the number of iterations
# - The loop runs once per value in the range
# - "_" is used as a throwaway variable when the value is not needed

#-----------------------------------------------------------------------------------


# Version 3: Combining while and for loops in functions

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


# Insight:
# - while True is used for input validation, ensuring only valid data is returned
# - Loops serve different roles: while (validation) vs for (iteration)
# - Demonstrates separation of concerns (input validation vs execution)
#-----------------------------------------------------------------------------------