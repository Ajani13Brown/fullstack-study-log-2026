#--------------------------------------------------------------------------------------------
# Notes and code created while watching NetworkChuck's
# "You Need to Learn Python RIGHT NOW!!" video series (Episode 9).
# Focus: deleting items from Python lists using list methods like clear(),
# remove(), and pop(), and understanding how list data changes after removal.
#---------------------------------------------------------------------------------------------

# lets learn about removing items from a list

supplies = ["tent","sleeping bags","water","raspberry pi","coffee","knife","ethernet cable","flash drive","beard oil", "marshmallows"]



# remove() deletes a specific value from the list
# It removes only the first matching element and cannot remove multiple items at once
# The item must exist in the list or Python will raise an error
supplies.remove("raspberry pi")

print(supplies)


# pop() removes an item by its index position
# After removing index 0, all remaining items shift left, so the next item becomes index 0
supplies.pop(0)


# Calling pop(0) again removes the new first item because the list order has shifte
supplies.pop(0)

print(supplies)

supplies.pop(0)

# pop() not only removes the item, it RETURNS the removed value
# Here, the removed element is printed instead of the full list
print(supplies.pop(0))


# clear() removes ALL items from the list
# The list still exists, but becomes an empty list []
supplies.clear()

print(supplies)