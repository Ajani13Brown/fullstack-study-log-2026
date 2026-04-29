# -------------------------------------------------------------------------------------------
# CS50 Python – Lecture 03: Loops (While Loops)

# Focus:
# Using while loops to control repetition by building small programs
# (e.g., printing "meow" a set number of times).

# Purpose:
# Understand condition-based execution, loop control, and avoiding infinite loops
# through follow-along notes and code experiments.
# ----------------------------------------------------------------------------------------
# Version 1: Manual Repetition (Before Loops)

# Goal:
# Before using loops, write code manually to make the computer print
# "meow" three times.


print("meow")
print("meow")
print("meow")


# Version 1.5: String multiplication variation (still no loop)

print("meow\n" * 3, end="")


# Insight:
# - Repetition is hardcoded and not scalable
# - Using loops enables more dynamic, scalable solutions
# -------------------------------------------------------------------------------------------

# Version 2: Introduction to while loops

# While Loop:
# A while loop executes a block of code repeatedly as long as a specified
# Boolean condition evaluates to True, and terminates when it becomes False.

# Goal:
# make the computer print "meow" three times using while loop

i = 0  # Counter to track iterations
while i < 3:  # Condition controls how long the loop runs
    print("meow")
    i += 1  # Update counter to eventually terminate the loop


# Insight:
# - Syntax: "while" + condition + colon (:), followed by an indented block
# - Infinite loops occur when the condition never becomes False
# - Use Ctrl + C to stop a running infinite loop in the terminal

#-------------------------------------------------------------------------------------------

# Version 3: While True loops

# While True Loop:
# A while True loop creates an intentional infinite loop that runs continuously
# until explicitly exited using a break statement when a condition is met.


while True:
    n = int(input("What's n?"))
    if n < 0:
        continue # Skips the rest of the current iteration and restarts loop
    else:
        break    # Immediately exits the loop

print("meow\n" * n, end="")

# Insight:
# - while True enables input validation until a valid value is provided
# - break exits the loop once conditions are satisfied
# - separates validation from final output logic

#---------------------------------------------------------------------------------------------