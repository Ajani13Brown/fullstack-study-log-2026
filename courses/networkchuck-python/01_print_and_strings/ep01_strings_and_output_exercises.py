# ============================================================
# NetworkChuck Python Refresher – Intermediate String Exercises
# Focus: strings, print(), formatting, repetition, and escapes
# Constraints: no variables, no loops, no conditionals
# ============================================================


# ------------------------------------------------------------
# Exercise 1: Controlled Formatting
#
# Reproduce the following output EXACTLY:
#
# ===== SYSTEM START =====
# Loading modules...
# Loading modules...
# Loading modules...
# System online.
# ========================
#
# Constraints:
# - Use string repetition (*) for the repeated line
# - Use ONLY one print() statement
# - Do NOT use triple-quoted strings
# ------------------------------------------------------------

# --- Solution 01---

print("==== SYSTEM START =====\n" + "Loading modules...\n" *3 + "System online.\n" +"========================" )

# ------------------------------------------------------------
# Exercise 2: Quote Strategy
#
# Print the following output EXACTLY:
#
# The AI said: "I'm learning Python the right way."
#
# Constraints:
# - Do NOT escape any characters
# - Choose single or double quotes strategically
# - Use ONE print() statement
# ------------------------------------------------------------

# --- Solution ---

print("The AI said: " + '"' +"I'm learning Python the right way." + '"')

# --- Notes/Explanation ---
# This solution uses string concatenation (+) by breaking the sentence into smaller strings
# Each part uses single or double quotes strategically based on its content
# "The AI said: " is wrapped in double quotes since it contains no apostrophes
# '"' is its own string and represents a literal double-quote character in the output
# "I'm learning Python the right way." is wrapped in double quotes to avoid conflicts with the apostrophe in "I'm"


# ------------------------------------------------------------
# Exercise 3: Hybrid Construction
#
# Create the following output:
#
# --- LOG START ---
# User: Iron Man
# User: Tony Stark
# User: Poppy
# --- LOG END ---
#
# Constraints:
# - Use concatenation (+) to build the header and footer
# - Use string repetition (*) to generate the three user lines
# - Do NOT use triple-quoted strings
# - Use ONE print() statement
# ------------------------------------------------------------

# --- Solution ---
print("-" * 3 + " LOG START " + "-" * 3 + "\nUser: Iron Man\n" + "User: Tony Stark\n" + "User: Poppy\n" + "-" * 3 + " LOG END " + "-" * 3)

# ------------------------------------------------------------
# Exercise 4: Whitespace Awareness
#
# Generate the following output EXACTLY (blank lines matter):
#
# BEGIN
#
# DATA LINE 1
# DATA LINE 2
#
# END
#
# Constraints:
# - Use \n intentionally (no extra blank lines)
# - Use ONLY one print()
# - Do NOT use triple-quoted strings
# ------------------------------------------------------------

# --- Solution ---
print("BEGIN\n\nDATA LINE 1\nDATA LINE 2\n\nEND")

# ------------------------------------------------------------
# Exercise 5: Multi-Line vs Escapes (Design Choice)
#
# Produce the following output:
#
# ERROR: Invalid input
# Please try again.
#
# Requirements:
# - Solution A must use a triple-quoted string
# - Solution B must use \n and string concatenation
# - Each solution must use exactly ONE print()
# ------------------------------------------------------------
# --- Solution A ---
print('''ERROR: Invalid input
Please try again.''')

# --- Solution B ---
print("ERROR: Invalid input\n" + "Please try again.")

# ------------------------------------------------------------
# Exercise 6: Repetition with Structure
#
# Produce the following output:
#
# [!] ALERT
# [!] ALERT
# [!] ALERT
#
# Constraints:
# - Use string repetition (*)
# - Do NOT manually repeat the text
# - Use \n correctly so there is NO extra blank line at the end
# - Use ONE print() statement
# ------------------------------------------------------------

# --- Solution ---
print("[!] ALERT\n" * 3)

# ------------------------------------------------------------
# Exercise 7: Visual Separator Challenge
#
# Generate the following output:
#
# --------------------
# SESSION ACTIVE
# --------------------
#
# Constraints:
# - Create the dashed lines using string repetition (*)
# - Use concatenation (+) to assemble the final output
# - Use ONE print() statement
# ------------------------------------------------------------

# --- Solution ---
print("-" * 20 + "\nSESSION ACTIVE\n" + "-" * 20)

# ------------------------------------------------------------
# Exercise 8: Single-Line Code Challenge
#
# Write ONE line of Python code that prints:
#
# I am Iron Man
# I am Iron Man
# I am Iron Man
# I am Iron Man
#
# Constraints:
# - Must be a single print() statement
# - Must use string repetition (*)
# - Must include \n
# - Do NOT use triple-quoted strings
# ------------------------------------------------------------
print("I am Iron Man\n" * 4)

# ------------------------------------------------------------
# Meta Challenge (Optional but Recommended)
#
# Choose ANY TWO exercises above and:
# 1. Rewrite the solution using the fewest characters possible
# 2. Rewrite the solution to be maximally readable
# 3. Add comments explaining why you chose each approach
#
# Goal:
# - Practice clarity vs conciseness trade-offs
# - Reinforce formatting precision and intent
# ------------------------------------------------------------
