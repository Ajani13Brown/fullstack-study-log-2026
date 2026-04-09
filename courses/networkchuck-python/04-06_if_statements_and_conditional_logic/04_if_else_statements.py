#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 4).
# Focus: if, elif, and else statements for controlling program flow.
#----------------------------------------------------------------------------------

# Let's Start a coffee shop together!!
# We're going to build a coffee shop using some new python programing concepts!!!

# Let's build a robot barista!

print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!!!!!!")

name = input("What is your name?\n")

# An if statement starts with the keyword `if`, followed by a condition.
# The condition often uses `==` to compare two values for equality.
# `==` checks if values are equal, while `=` is used to assign a value to a variable.
# A colon (:) ends the line and tells Python a decision block is starting.
if name == "Ben":

    # Indentation defines which lines of code belong to this if statement.
    # Any code indented under the if statement is part of its decision block.
    print("Your not welcome here EVIL Ben!! Get Out!!")

# An else statement is used as a fallback when the if condition is False.
# It does not have its own condition and runs when all previous checks fail.
# else must be aligned with its matching if statement.
else:
    print("Hello " + name + ", thank you so much for coming in today. \n\n\n")

#------------------------------------------------------------
# New topic: using comparison operators to evaluate
# conditions in if statements (>, <, >=, <=)
#------------------------------------------------------------

# Comparison operators are used to compare two values.
# They return True or False and are commonly used in if statements.
# The `>` operator checks if the value on the left is greater than the value on the right.
if 4 > 3:
    print("Yep, it's true")
    print("It's still true!!")
else:
    print("Nope, not true!!")

# Other comparison operators in Python:
# `<`  checks if the left value is less than the right value.
# `<=` checks if the left value is less than or equal to the right value.
# `>=` checks if the left value is greater than or equal to the right value.
# `!=` checks if two values are not equal.


#------------------------------------------------------------
# Exploring how the exit() function is used to
# end the program in the coffee shop scenario
#------------------------------------------------------------

# Ask your customer what their name is with the input() function
# store that in the variable NAME.

name = name = input("What is your name?\n")

# Greet the customer with their name
# Thank them for coming in today using concatenation.

if name == "Ben":
    print("your not welcome here Ben!! get out")

    # exit() immediately stops the program when this condition is met.
    # This avoids nesting the rest of the coffee shop logic inside an else block.
    # It's used when you want the program to end early under a specific condition.
    exit()

else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

# Coffee Menu
menu = "Black Coffee, Espresso, Latte, Cappucino"

# Ask the customer what they would like from the menu
# Store it in the Variable ORDER
order = input(name + ", what would you like form our menu today? Here is what we are serving.\n" + menu + "\n")

# Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

# Set Price for coffee
price = 8

# Calculate the customer's Total
# Store it in a variable TOTAL
total = price + int(quantity)

print("Thank you, Your total is: $" + str(total))

