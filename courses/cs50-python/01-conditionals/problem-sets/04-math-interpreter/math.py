# -------------------------------------------------------------------------
# CS50 Python – Problem Set 4: Math Interpreter
#
# Focus: String parsing + conditional logic for arithmetic operations
# -------------------------------------------------------------------------


# Problem: Math Interpreter

# Goal:
# - Prompt the user for an arithmetic expression in the format: x y z
# - Interpret x and z as integers and y as an operator (+, -, *, /)
# - Perform the corresponding calculation based on the operator
# - Output the result as a float formatted to one decimal place

# Supported Operators:
# - + = addition
# - - = subtraction
# - * = multiplication
# - / = division
#-----------------------------------------------------------------------------

# Approach:
# - Prompt user for arithmetic expression with input()
# - Utilize .split(" ") method to seperate as values to invidvual variables "x, y, z = expression.split(" ")
# - Convert x and z variables to float data type
# - use coditional logic to decide which math operation to use based on y value

# Solution:

def interpreter():
    expression = input("Math Expression: ")

    x,y,z = expression.split(" ")

    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))


interpreter()
# Challenge (Optional):
# - Explored parsing input via list indexing before learning to unpack values directly with split()
# - Initially thought the operator needed conversion before using it as a condition for selecting the operation