# -------------------------------------------------------------------------
# CS50 Python – 01 Conditional 
# Problem Set 1: Deep Thought
#
# Focus: Conditional logic + handling multiple valid input formats
# -------------------------------------------------------------------------


# Problem: Deep Thought
#
# Goal:
# - Prompt the user for the answer to the "Great Question of Life, the Universe and Everything"
# - Output "Yes" if input is 42, "forty-two", or "forty two" (case-insensitive)
# - Output "No" for any other input
#
# Approach:
# - Create a function named deep()
# - Prompt user using input() inside the function and store response in variable "meaning"
# - Utilize .lower() function to ensure response is case insensitive
# - Use match conditional operator to print yes or no based on user response
# - Utilize "|" to evaluate multiple conditions for yes and "case _" for all other cases


# Solution:

def deep():
    meaning = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    match meaning.lower():
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

deep()


# Challenge (Optional):
# - initially placed .lower() function on the input prompt "meaning = input("...").lower"
# - Moved .lower() to the variable being called in the match conditional operator "match meaning.lower():"
