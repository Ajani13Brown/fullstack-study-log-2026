#----------------------------------------------------------------------------------
# Notes and code created while following along with NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 2).
# Focus: input and variables.
#----------------------------------------------------------------------------------

# Let's start a coffee shop together!! 
# We're going to build a coffee shop uising some new Python programming concepts!!

# Let's build a robot Barista!!

print("Hello, welcome to NetworkChuck Coffee!!!!!!")

# The input() function pauses the program and waits for the user to type something.
# Whatever the user types is returned as a string (text).
# input() is commonly used to collect information from the user,
# such as names, choices, or other data the program needs to continue.
#input("What is your name?")

# A variable is a way to store data in memory so it can be reused later in the program.
# The variable name comes first, followed by the assignment operator (=).
# The equals sign assigns the value on the right side to the variable on the left.
# In this example, the string "Ajani" is stored in the variable named `name`.
name = "Ajani"

# The print() function outputs information to the screen.
# When a variable is passed into print(), Python looks up the value
# stored in that variable and displays it.
print(name)

# Variables can be reassigned to new values at any time.
# When a variable is given a new value, it replaces the old one.
# Python will always use the most recent value assigned to the variable.
name = "Iron Man"
print(name)

# Variables can store values from many sources, including user input.
# Instead of a fixed value, input() gets a string from the user and stores it in name.
name = input("what is your name?\n")

# Variables can be included in strings to dynamically change the message.
# The value stored in the variable `name` is inserted into the message.
# When the program runs, Python replaces `name` with its current value in the printed output.
#print("Hello " + name + ", Thank you so much for coming in today")


menu = "Black Coffee, Latte, Nitro Cold-Brew or Cappucino"

# Combine variables and strings in a single message to create dynamic, personalized output.
print(name + ", What would you like from our menu today, Here is what we are serving.\n\n" + menu)

# Store the user's menu choice in the variable `order` using input().
order = input()

# Use the value stored in `order` along with `name` to create a personalized confirmation message.
print("Sounds good " + name + ", well have that " + order + " ready for you in a moment.")

