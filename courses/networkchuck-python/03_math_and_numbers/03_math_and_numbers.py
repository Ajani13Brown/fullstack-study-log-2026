#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 3).
# Focus: math concepts in Python, operators, and numeric behavior.
#----------------------------------------------------------------------------------

# Let's play with some numbers

name = "Ajani"

# An integer represents a whole number (no decimals), used for counting or math operations
# Integers can be assigned as variable values, just like strings, to store numeric data
age = 7

print(name)
print(age)

# The type() built-in function is used to check the data type of a value or variable
# This helps confirm how Python is interpreting the data at runtime
type(name)

# Printing the result of type() lets us see the data type in the console
# Expected output: <class 'str'> — confirms that name is a string
print(type(name))

# type() can be used on different variables to compare their data types
# Expected output: <class 'int'> — confirms that age is an integer
print(type(age))

# A float represents a number with a decimal point, used for more precise values
actual_age = 33.417

# Python can perform basic math operations like addition, subtraction, multiplication, and division
# Using + adds two numbers together and returns the result
print(5 + 7)

# - Subtraction operator: subtracts the second number from the first
print(5 - 7)

# / Division operator: divides the first number by the second, always returns a float
print(5 / 7)

# * Multiplication operator: multiplies two numbers together
print(5 * 7)

# ** Exponentiation operator: raises the first number to the power of the second
print(5 ** 7)

# You can combine multiple math operators in one expression
# Python follows the order of operations (PEMDAS): parentheses, exponents, multiplication/division, addition/subtraction
print(5 + 7 - 9 / 2 * 5 ** 3)

# Assigning a math operation to a variable sets the variable's value to the result of the calculation
# In this example, the variable math is set to 25
math = 5 * 5

# You can use variables in math operations just like numbers
# Here, age, actual_age, and math are added together and the result is stored in the variable 'results'
results = age + actual_age + math

# the result
print(results)

#-----------------------------------------------------------------------------------------------------------------------------------

#Let's apply what we have learn to inproving or Networkchuck coffee application

price = 7


print("Hello, welcome to NetworkChuck Coffee!!!!!!!")

name = input("what is your name?\n")

print("Hello, " + name + ", thank you so much for coming in today. \n\n\n")

menu = "Black Coffee, Espresso, Latte and Nitro Cold-Brew"

print(name + ", what would you like from our menu today Here are our menu options " + menu + "?")

order = input()

quantity= input("how many " + order + " would you like?\n")

# quantity is stored as a string from input(), and strings cannot be used in math operations
# int() converts quantity into an integer so it can be multiplied by the price
total = price * int(quantity)

# quantity and total are numbers, and numbers cannot be directly combined with strings
# str() converts numeric values into strings so they can be concatenated with text
print("So you would like " + str(quantity) + order + " that will be $" + str(total))

print("Thank you " + name + ", we'll have your " + quantity +" " + order + " ready for you in a moment.")