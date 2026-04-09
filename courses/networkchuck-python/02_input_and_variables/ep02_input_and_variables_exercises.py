# ============================================================
# NetworkChuck Python Refresher – Standalone Practice Exercises
# Focus: variables, input(), reassignment, string composition
# Rule:
# Each exercise is meant to be written in its OWN file.
# Do NOT rely on variables or code from any other exercise.
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Modify a Variable After Input
#
# In this file:
# 1. Ask the user for their name and store it in a variable.
# 2. Change the value of THAT SAME variable by adding a title
#    in front of the name (for example: "Captain ").
# 3. Print the final result.
#
# Example output:
# Welcome, Captain Ajani
# ------------------------------------------------------------

# --- Solution ---
# name = input("what is your name\n")
# title = "King"
# full_name = title + " " + name
# print("Hello I am, " + full_name)

# ------------------------------------------------------------
# Exercise 2: Build and Print a Menu Message
#
# In this file:
# 1. Store three menu items in three different variables.
# 2. Store a customer's name in a separate variable.
# 3. Print ONE message that shows the customer's name
#    followed by the menu items on separate lines.
#
# Example output:
# Ajani, here is today's menu:
# Coffee
# Latte
# Cappuccino
# ------------------------------------------------------------

# --- Solution ---
# menu_item_1 = "cheese"
# menu_item_2 = "pepperoni"
# menu_item_3 = "pickle"

# customer = input("Welcome to Aj's Pizzeria\nwhat is your name?\n")

# print("Hello " + customer + ", what kind of pizza would you like to order, we offer " + menu_item_1 + ", " + menu_item_2 + " and " + menu_item_3 + " pizzas.")

# ------------------------------------------------------------
# Exercise 3: Change Input Before Printing
#
# In this file:
# 1. Ask the user what drink they want and store it in a variable.
# 2. Change the value of that variable by adding a description
#    in front of it (for example: "Large ").
# 3. Print the updated value.
#
# Example output:
# Order received: Large Latte
# ------------------------------------------------------------

# --- Solution ---
drink = input("what drink would you like?\n")

size = input("what is " + drink + " would you like?\n")

print("Your " + size + " " + drink + " will be ready in just a moment!")

# ------------------------------------------------------------
# Exercise 4: Preserve and Replace a Value
#
# In this file:
# 1. Store a user's name in one variable.
# 2. Store the SAME value in a second variable.
# 3. Change the first variable to a different name.
# 4. Print both values in ONE message.
#
# Example output:
# Original user: Ajani | Current user: Iron Man
# ------------------------------------------------------------

# --- Solution ---
original_user = "me"
current_user = "SMASH!"
original_user = "HULK"

print("Original user: " + original_user + " | Current user: " + current_user)

# ------------------------------------------------------------
# Exercise 5: One Message Using Three Variables
#
# In this file:
# 1. Store a customer's name in one variable.
# 2. Store a drink order in a second variable.
# 3. Store a menu in a third variable.
# 4. Print ONE message that includes all three values.
#
# Example output:
# Ajani ordered a Latte from the following menu:
# Coffee, Latte, Cappuccino
# ------------------------------------------------------------


# ------------------------------------------------------------
# Exercise 6: Reuse Without Rewriting
#
# In this file:
# 1. Build a confirmation message and store it in a variable.
# 2. Print the message twice.
#
# Example output:
# Order confirmed for Ajani: Latte
# Order confirmed for Ajani: Latte
# ------------------------------------------------------------


# ------------------------------------------------------------
# Exercise 7: Build a Message in Steps
#
# In this file:
# 1. Store a base message in a variable.
# 2. Add a customer's name to the SAME variable.
# 3. Add an order to the SAME variable.
# 4. Print the final message once.
#
# Example output:
# Thank you Ajani, your order of Latte is being prepared.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Exercise 8: Formatting and Spacing (Careful!)
#
# In this file, print the following output EXACTLY:
#
# ===== RECEIPT =====
# Customer: Ajani
#
# Item: Latte
#
# Thank you for your visit!
# ===================
#
# Rules:
# - Store the customer name in a variable.
# - Store the item name in a different variable.
# - Use \n for spacing.
# - Use exactly ONE print() statement.
# ------------------------------------------------------------


# ------------------------------------------------------------
# Optional Meta Exercise
#
# Pick ONE exercise above and:
# 1. Rewrite it to be as short as possible.
# 2. Rewrite it to be as readable as possible.
#
# Add comments explaining your choices.
# ------------------------------------------------------------
