#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 5).
# Focus: conditional logic using if, elif, and else to control program flow.
#----------------------------------------------------------------------------------

name = input("what is your name?\n")

# A nested if statement is an if block placed inside another if block.
# It allows us to make a second decision only if the first condition is true.
# This creates more specific logic paths without running unnecessary checks.
if name == "Ben":
    evil_status = input("Are you evil?\n")
    
    # This inner if only runs because the outer condition (name == "BEN") was true.
    # Nested if statements help handle dependent conditions in a clear, structured way.
    if evil_status == "Yes":
        print("You're not welcome here Ben!! GET OUT!!!")
        exit()
    else:
        print("Oh wow so you like a GOOD Ben, thats great! Well come on in good Ben!")

else:
    print ("Hello " + name + ", thank you so much for coming in today\n\n\n")


#----------------------------------------------------------------------------------
# New Lab Section – Introducing elif
# This section focuses on using elif to handle multiple related conditions
# in a cleaner, more efficient decision structure.
#----------------------------------------------------------------------------------



# Coffee Menu
menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

# Ask the customer what they would like from the menu
# Store it in the variable order

order = input(name + ", what would you like from our menu toady? Here is what we are serving. \n" + menu + "\n")

# Ask the customer how many coffees they would like.
# Store it in the variable QUANTITY

quantity = input("How many coffees would you like?\n")


# elif (short for "else if") lets us check another condition only if
# the previous if/elif conditions were False.
# This keeps related decisions in one structured flow instead of separate if blocks.

if order == "Frappuccino":
    # First condition checked — if True, this block runs and the rest are skipped.
    price = 13

elif order == "Black Coffee":
    # This runs only if the first condition was False.
    # elif helps handle multiple specific cases without checking everything again.
    price = 3
elif order == "Espresso":
    price = 5
elif order == "Latte":
    price = 9
elif order == "Cappucino":
    price = 10
else:
    print("Sorry we dont have that here.")