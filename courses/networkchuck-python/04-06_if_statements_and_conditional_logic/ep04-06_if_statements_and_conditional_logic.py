# ============================================================
# NetworkChuck Python Practice – Intermediate Decision Logic
# Focus: if, elif, else, comparison operators, logical operators
# Episodes Covered: 4–6
# Notes: Exercises are original, designed to challenge intermediate skills
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Temperature Classification (Fahrenheit)
#
# Ask the user for the current temperature in Fahrenheit.
# Print:
# - "Freezing!" if temperature <= 32
# - "Cold" if temperature > 32 and <= 50
# - "Cool" if temperature > 50 and <= 65
# - "Warm" if temperature > 65 and <= 80
# - "Hot!" if temperature > 80
#
# Focus:
# - if, elif, else
# - comparison operators
# - multi-condition logic
# ------------------------------------------------------------

# --- Solution ---

temp = int(input("What is the tempature?\n"))
if temp <= 32:
    print("Freezing!")
elif temp > 32 and temp <= 50:
    print("Cold")
elif temp > 50 and temp <= 65:
    print("Cool")
elif temp > 65 and temp <= 80:
    print("Warm")
else:
    print("Hot!")

# ------------------------------------------------------------
# Exercise 2: Valid Triangle Check
#
# Ask the user for three side lengths.
# Determine if the sides can form a valid triangle using the triangle inequality:
#   A triangle is valid if the sum of any two sides > the third side.
# Print "Valid triangle" or "Invalid triangle".
#
# Focus:
# - logical operators (and)
# - multiple conditions combined
# - critical thinking
# ------------------------------------------------------------

# --- Solution ---
side_a = int(input("What is the length of the first side:"))
side_b = int(input("What is the length of the second side:"))
side_c = int(input("What is the length of the third side:"))

if side_b + side_c > side_a:
    print("Valid triangle")
elif side_a + side_c > side_b:
    print("Valid triangle")
elif side_b + side_a > side_c:
    print("Valid triangle")
else:
    print("Invalid triangle")


# ------------------------------------------------------------
# Exercise 3: Exam Grade Evaluation
#
# Ask the user for their exam score (0–100).
# Print:
# - "Fail" if score < 60
# - "Pass" if score >= 60 AND < 75
# - "Merit" if score >= 75 AND < 90
# - "Distinction" if score >= 90
#
# Focus:
# - if, elif, else
# - comparison operators
# - combining conditions with logical operators
# ------------------------------------------------------------

# --- Solution ---
score = int(input("What was your test score?\n"))

if score < 60:
    print("Sorry you FAIL")
elif score >= 60 <= 75:
    print("Great you PASS!")
elif score >= 75 <= 90:
    print("did great you pass with MERIT")
elif score >= 90:
    print("Amazing you pass with flying color, this is a special DISTINCTION")

# ------------------------------------------------------------
# Exercise 4: Discount Eligibility
#
# Ask the user:
# - Age
# - Membership status (Yes/No)
# - Number of items they are purchasing
#
# Apply a discount if:
# - Age < 18 OR Age >= 65 OR Membership == "Yes"
# AND
# - Number of items >= 3
#
# Print "Discount applied" or "No discount".
#
# Focus:
# - combining OR and AND
# - reasoning with multiple conditions
# ------------------------------------------------------------

# --- Solution ---
age = int(input("How old are you?\n"))
membership = input("do you have a membership:(Yes/No)\n")

if age < 18 or age >= 65 or membership == "Yes":
    print("Discount applied")
else:
    print("No discount")

# ------------------------------------------------------------
# Exercise 5: Password Retry Limit with Not
#
# Ask the user to enter a secret code.
# They have 3 attempts. Use a variable to track attempts.
# If they enter the wrong code, print how many attempts remain.
# If they succeed, print "Access Granted" and stop asking.
# If attempts run out, print "Access Denied".
#
# Focus:
# - not operator
# - controlling flow with multiple checks
# - using loops with conditionals (extra challenge)
# ------------------------------------------------------------

# --- Solution ---
attempts = 0

while attempts < 3:

    password = input("What is the password?\n")

    if password == "Happy123":
        print("Access Granted")
        break
    else:
        attempts += 1
        print(attempts)
        print("Access Denied, You have " + str(3 - attempts) + " attempts left")
        


# ------------------------------------------------------------
# Exercise 6: Complex Number Range Classification

# Ask the user to input an integer.
# Print a message based on these overlapping conditions:
# - If the number is divisible by 3 AND even, print "Fizz-Even"
# - If divisible by 3 AND odd, print "Fizz-Odd"
# - If divisible by 5 AND NOT divisible by 3, print "Buzz"
# -If divisible by 2 only, print "Even"
# - Otherwise, print "Other"
#
# Focus:
# - multiple logical operators combined
# - not operator
# - elif structure to avoid conflicts
# - critical thinking about condition order
# ------------------------------------------------------------

# --- Solution ---

def fizz_count(num):
    if num % 3 == 0 and num % 2 == 0:
        print("Fizz-Even")
    elif num % 3 == 0 and num % 2 != 0:
        print("Fizz-Odd")
    elif num & 5 == 0 and num % 3 != 0:
        print("Buzz")
    else:
        print("Other")

fizz_count(6)

# I did not include the logic for If divisible by 2 only, print "Even" because that is mathmatically impossible
# There are no number only divisable by 2 all numbers should at least be divisable by 1