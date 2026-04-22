# -------------------------------------------------------------------------
# CS50 Python – Lecture 01: Conditionals - if/elif/else

# This file explores Conditional statements with comparison operators "if", "elif" and "else"
# This file also practices maniplualting control flow to produce more efficent, maintainable code.
# ----------------------------------------------------------------------------------------------------------
# Version 1: Independent if statements
# Each condition is evaluated separately (all can run if True)
x = int(input("What's x? "))
y= int(input("What's y? "))


if x < y:
    print("x is less then y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# Insight:
# With multiple "if" statements, control flow independently evaluates every condition
# Execution persists through all blocks, checking every condition regardless of prior outcomes 

#---------------------------------------------------------------------------------------------------------
# Version 2: if / elif chain
# Only ONE condition runs (mutually exclusive flow)


x = int(input("What's x? "))
y= int(input("What's y? "))

if x < y:
    print("x is less then y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# Insight:
# elif creates mutual exclusive control flow
# only one block in the if/elif chain will execute dependent on previous check being false
# Execution stop after first true condition

#----------------------------------------------------------------------------------------------------------

# Version 3: if / elif / else
# Final fallback replaces explicit equality check

x = int(input("What's x? "))
y= int(input("What's y? "))

if x < y:
    print("x is less then y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# Insight:
# else has no condition; else acts as default case
# cleaner when all outcomes are already covered

#-------------------------------------------------------------------------------------------------------------


# Version 1: OR condition vs explicit equality logic
# Combines two checks into one condition

x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Insight:
# Uses multiple comparisons to define "not equal"
# ----------------------------------------------------------------------------------------------------------
# Version 2: Direct inequality check (simpler logic)
# Uses a single operator instead of multiple conditions

x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Insight:
# Cleaner and more direct than OR conditions
# One operator replaces multiple comparisons
# ----------------------------------------------------------------------------------------------------------
