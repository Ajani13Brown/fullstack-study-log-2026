# -------------------------------------------------------------------------
# CS50 Python – Lecture 01: Conditionals

# This file contains follow-along notes and example code written while
# watching the lecture from the CS50 Python course. The purpose of this
# file is to practice concepts, experiment with examples, and document
# my learning process as I refresh my programming fundamentals.
# -------------------------------------------------------------------------------

# Comparison using "and" operator

score = int(input("Score:"))

if score >= 90 and score <= 100:
     print("Grade: A")
elif score >= 80 and score <= 90:
     print("Grade: B")
elif score >= 70 and score <= 80:
     print("Grade: C")
elif score >= 60 and score <= 70:
     print("Grade: D")
else:
     print("Grade: F")

# Insights:
# and evaluates if both conditions must be True
# used to define ranges or enforce multiple constraints

#--------------------------------------------------------------------------------------

# Range comparison using chained operators (preferred over "and")


score = int(input("Score:"))

if 90 <= score <= 100:
     print("Grade: A")
elif 80 <= score <= 90:
     print("Grade: B")
elif 70 <= score <= 80:
     print("Grade: C")
elif 60 <= score <= 70:
     print("Grade: D")
else:
     print("Grade: F")

# Insights:
# Uses chained comparisons → shorter and easier to read than "and"
# Reduces repetition (no repeated "score" checks)
# Clearly expresses ranges (reads like math)
# Preferred Python style for range checks

#-------------------------------------------------------------------------------------------

# Simplified range checks using descending conditions

score = int(input("Score:"))

if score >= 90:
     print("Grade: A")
elif score >= 80:
     print("Grade: B")
elif score >= 70:
     print("Grade: C")
elif score >= 60:
     print("Grade: D")
else:
     print("Grade: F")

# Insights:
# Eliminates upper bounds since earlier checks handle higher values
# Reduces redundancy, simpler and easier to maintain

#----------------------------------------------------------------------------------------------

# range checks using descending conditions with "if" operator

score = int(input("Score:"))

if score >= 90:
     print("Grade: A")
if score >= 80:
     print("Grade: B")
if score >= 70:
     print("Grade: C")
if score >= 60:
     print("Grade: D")
else:
     print("Grade: F")

# Insights:
# Code will not work as expected
# "elif" only checks when previous condition is false
# "if" checks all coditions independentlyy