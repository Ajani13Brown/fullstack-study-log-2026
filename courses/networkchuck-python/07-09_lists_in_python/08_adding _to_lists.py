#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 8).
# Focus: adding items to Python lists, modifying list contents, and how lists grow dynamically.
#----------------------------------------------------------------------------------

# Lets learn about lists

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee","knife", "ethernet cable", "flash drive", "beard oil", "Marshmallows"]

print(supplies)

# lets experiment with adding to our SUPPLIES list.

# A *method* in Python is a function that belongs to an object (like a list).
# Methods are called using dot notation: object.method()
# They are used to perform actions on that specific object, such as modifying a list.




# .append() adds ONE single element to the END of the list.
# It cannot add multiple separate elements at once — only one item per call.
supplies.append("toilet paper")

print(supplies)


# .extend() adds MULTIPLE elements to a list at once.
# It takes an iterable (like another list) and adds each item to the end individually.
supplies.extend(["sunscreen","Compass"])

print(supplies)


# Using + creates a NEW list by combining two lists together.
# This is not a method — it’s list concatenation, and the result must be reassigned.
supplies = supplies + ["first-aid kit", "walking sticks"]

print(supplies)


# += also combines lists, but modifies the existing list in place (similar to extend).
supplies += ["trash bags", "toothbrush"]

print(supplies)


# .insert(index, value) adds an item at a SPECIFIC position in the list.
# Syntax: list.insert(index, element)
# The first argument is the position (index), and the second is the item being added.
# insert() adds ONE element at a time — to add multiple, you must call it multiple times.
supplies.insert(0,"bug spray")

print(supplies)