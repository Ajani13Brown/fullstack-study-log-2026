#----------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 7).
# Focus: understanding Lists in Python, storing multiple values, indexing,
# accessing items, and modifying list data.
#----------------------------------------------------------------------------------

#lets learn about lists

# Hey, we're going on a camping trip!!

# Here is stuff we need
# tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, Flash drive, Beard oil, marshmallows

camping_stuff = "tent, sleeping bags, water, raspberry pi, coffee, knife, ethernet cable, Flash drive, Beard oil, marshmallows"

print(camping_stuff)

# A list is a data type that stores multiple values in one variable
# You can recognize a list by the opening and closing square brackets []
# Commas , are used to separate each item inside the list
# Each value in the list is called an element, and Python treats them as individual items
camping_list = ["test", "sleeping bags", "water", "raspberry pi", "coffee",
                "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]


# type() shows the data type of a variable
# This will display <class 'list'>, confirming camping_list is a list data type
print(type(camping_list))

# Lists can store different data types at the same time (strings, numbers, booleans, etc.)
# This shows Python lists are flexible and can hold mixed types in one structure
camp_site = ["Crystal Lake", 404, 89.3, True]



# Lists are ordered collections, meaning each item has a fixed position
# An index is the position number of an item in the list
# Indexing lets us access a specific item using list_name[index]

# List indexing starts at 0 (first item) and goes up to length of list - 1
# camping_list[4] selects the 5th item in the list
me =camping_list[4]

# Negative indexing counts from the end of the list
# -1 refers to the last item, -2 the second-to-last, etc.
# camping_list[9] would access the last item using forward indexing
# camping_list[-1] accesses the same last item using negative (reverse) indexing
# Both refer to the same element, just counted from different directions

you = camping_list[9]
you = camping_list[-1]

print(me)
print(you)

print(camping_list)

