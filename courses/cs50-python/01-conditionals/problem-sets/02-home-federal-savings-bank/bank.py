# -------------------------------------------------------------------------
# CS50 Python – Problem Set 2: Home Federal Savings Bank

# Focus: Conditional logic + string normalization (case + whitespace)
# -------------------------------------------------------------------------


# Problem: Home Federal Savings Bank

# Goal:
# - Prompt the user for a greeting
# - Output "$0" if the greeting starts with "hello" (case-insensitive)
#   (e.g., "hello", "hello there", "hello, Newman")
# - Output "$20" if the greeting starts with "h" but not "hello"
# - Output "$100" for all other greetings
# - Ignore leading whitespace in the input
#----------------------------------------------------------------------------

# Approach:
# - Prompt greeting using input()
# - Use if/elif logic chain to handle multile Competing conditions rather then match
# - Utilize .lower() to handle case-sensitivity
# - Utilize .strip() method to remove leading white space
# - Utilize .startswith() to check is string starts with "hello" or "h"


# Solution:

def bank():
    greeting = input("A customer walks into the bank. How do you greet them? ")

    if greeting.strip().lower().startswith("hello"):
        print("$0")
    elif greeting.strip().lower().startswith("h"):
        print("$20")
    else:
        print("$100")



# Challenge (Optional):
# - while you can use "if greeting.strip().lower().startswith("hello"):"
# - this does not cover cases where hello is used but not at the start
# (e.g., "Hey, hello there", "Why, Hello", "Well hello and how do you do")
# - in operator use in operator to check if "hello" in greeting but not specific to the start

def bank_v2():
    greeting = input("A customer walks into the bank. How do you greet them? ")

    if "hello" in greeting.lower():
        print("$0")
    elif greeting.strip().lower().startswith("h"):
        print("$20")
    else:
        print("$100")

bank_v2()