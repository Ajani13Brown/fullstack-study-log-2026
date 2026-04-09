# -------------------------------------------------------------------------
# CS50 Python – Lecture 00: Functions & Variables

# This file contains follow-along notes and example code written while
# watching the lecture from the CS50 Python course. The purpose of this
# file is to practice concepts, experiment with examples, and document
# my learning process as I refresh my programming fundamentals.
# -------------------------------------------------------------------------

# 1. FUNCTIONS

# A Function is a reusable block of code that performs a specific task when it is called. 
# Some functions are Built-into Python and can be used without first being defined.
# Functions can take arguments (input values) to work with and may also return results.
# The Print() function is a built-in function that displays text or values in the terminal.
# print("Hello, world") calls the print() function with the argument "Hello, world",
# which is then displayed in the terminal.

print("hello, world")

#-----------------------------------------------------------------------------------------------------

# return values and variables

# Functions can perform actions and also return values.
# The input() function displays a prompt and returns the text the user types.
# Variables store values so they can be used later in the program.
# input("What's your name?") asks the user for their name and returns their response as a string.
# The returned value is stored in the variable 'name' using the assignment operator (=).
name = input("What's your name?\n")

#-------------------------------------------------------------------------------------------------------

# String concatenation and multiple arguments

# Below we explore different ways to combine the string "Hello" with the variable 'name'.

# This line uses string concatenation to join the string and the variable.
# Concatenation combines two strings using the + operator.
# The result is a single string made of the text on the left and right of +.
print("Hello " + name)



# Using multiple arguments in print()

# The print() function can take more than one argument, separated by commas.
# Each argument is converted to a string (if it isn’t already) and printed in order.
# By default, print() separates each argument with a space.

# This prints the value of "Hello" and the value stored in 'name' on the same line,
# separated by a space. It's an alternative to string concatenation with +.
print("Hello", name)

# This method does not join the two strings into one.
# The print() function still treats them as two separate arguments and prints them as separate values.

#----------------------------------------------------------------------------------------------------------

# Named Parameters

# Named parameters are arguments passed to a function using the parameter name
# (e.g., end="") so you can control specific behavior without relying on position.

# Python print() documentation:
# https://docs.python.org/3/library/functions.html#print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

# *objects → print() can take multiple arguments (values to display).
# sep=' ' → defines the separator between arguments (default is a space).
# end='\n' → defines what is printed at the end (default is a newline).
# Using end="" prevents a newline so the next print() continues on the same line.

name = input("what is your name? ")
print("Hello ", end="")
print(name)

# -------------------------------------------------------------------------------------------------------------

# Escape Characters

# Escape characters are backslash codes that represent special characters in a string (e.g., \n, \t).
# Escape characters can also use \ to display characters literally in text (e.g., \" shows quotation marks).
print ("hello \"friend\"")

# -------------------------------------------------------------------------------------------------------------------

# format strings / F-string

# f-strings (format strings) let you place variables or expressions inside a string using {}.
# f-strings are created by adding f before the quotes

name = input("What's your name? ")

# This f-string uses f"..." with {} to embed the variable name directly into the string.
print(f"hello, {name}")

# ----------------------------------------------------------------------------------------------------------------------

# String Methods

# String methods are built-in functions that operate on strings and return modified results.
# They are called using dot notation after the string, like string.method().
# Official Python docs: https://docs.python.org/3/library/stdtypes.html#string-methods

# .strip() – removes leading and trailing whitespace.
# .title() – capitalizes the first letter of each word.
# .strip() and .title() modify the string returned by input()
name = input ("What's your name? ").strip().title()

print (f"Hello, {name}")

# Function – standalone code for general use, called like function(object).

# Method – a function that belongs to a specific data type,
# called like object.method().

# Rule of thumb:
# If the action is something the object itself can do, look for a method.
# If it’s a general operation on data, look for a function.


#------------------------------------------------------------------------------------------------------------------------

# Multiple Assignment with .split()

name = input ("What's your name? ").strip().title()

# .split() divides a string into a list of substrings based on a specified separator 
first, last = name.split(" ")

print(f"hello, {first}")

# -------------------------------------------------------------------------------------------------------------------------
 
