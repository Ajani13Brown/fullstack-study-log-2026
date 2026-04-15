# -------------------------------------------------------------------------
# CS50 Python – Lecture 01: Conditionals

# This file contains follow-along notes and example code written while
# watching the lecture from the CS50 Python course. The purpose of this
# file is to practice concepts, experiment with examples, and document
# my learning process as I refresh my programming fundamentals.
# -------------------------------------------------------------------------------

# Comparison operator using %

x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Insights:
#

#-------------------------------------------------------------------------------

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")



def is_even(n):
   if n % 2 == 0:
       return True
   else:
       return False
   
main()

#-----------------------------------------------------------------------------------

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")



def is_even(n):
   return True if n % 2 == 0 else False
   
main()

#-------------------------------------------------------------------------------------

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")



def is_even(n):
   return  n % 2 == 0
   
main()