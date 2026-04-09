#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 6).
# Focus: logical operators, combining conditions, and improving decision logic.
#----------------------------------------------------------------------------------

print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!!")

name = input("What is your name?\n")

# Logical operators combine multiple conditions in one decision
# "or" is True if at least ONE condition is True (widens a check)
# "and" is True only if ALL conditions are True (narrows a check)

# "or" is used here to allow either name to trigger the same logic path
if name == "Ben" or name == "Patricia":

    evil_status = input("Are you evil\n")
    good_deeds = int(input("how many good deeds have you done today?\n"))

    # "and" requires BOTH conditions to be True before running this block
    # This creates stricter decision logic than a single condition alone
    if evil_status == "Yes" and good_deeds < 4:

        # Full decision logic:
        # (name is Ben OR Patricia) AND (evil_status is Yes AND good_deeds < 4)
        # Combining operators allows layered, real-world style decisions
        print("You're not welcome here " + name + "!! Get out !!")
        exit()

    else:
        print("Hello " + name +", thank you so much for coming in today.\n\n\n")

    beard_length = int(input("how long is your beard?\n"))

    if beard_length >= 1:
        print("oh, hello good sir, nice beard, You may go to the front of the line.")

#--------------------------------------------------
# New Lab Section
# Instructor starts a fresh example to introduce
# the "not" logical operator and condition reversal.
# Focus: using "not" to invert boolean logic.
#--------------------------------------------------

print("Hello, welcome to NetworkChuck Cofee!!!!")


name = input("what is your name?\n")

# "not" lets us check when a condition is false instead of true
# Used to run code when something is NOT equal or does NOT meet a condition

# Runs when the name is anything except "Ben"
if not name == "Ben":
    print("Get out of here!!")

else:
    print("come on in!")

# Runs only when the name IS "Ben"
me = "A.J"

# Comparison and logical operators produce Boolean values (True or False)
# These True/False results are a Boolean data type used in decision-making
print(me == "A.J")
print(type(me == "A.J"))

# "!=" means "not equal to"
# This condition is True when the two values are different
if 7 != 8:
    print("Yea that sounds right")
