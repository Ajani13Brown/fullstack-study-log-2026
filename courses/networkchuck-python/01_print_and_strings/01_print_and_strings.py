#Notes and code created while watching NetworkChuck's "You Need to Learn Python RIGHT NOW!!" video series (Episode 1).
#Focus: basic output, print() function, and strings

#-------------------------------------------------------------------------------------------------------------------------

# print() is a built-in Python function that sends output to the console/terminal.
# The value inside the parentheses is a string, which is a sequence of chraraters representing text data in Python.
# "Hello World!!!!" is a string enclosed in quotes and is displayed exactly as written.
print("Hello World!!!!")

# Strings in Python can be enclosed in either single (' ') or double (" ") quotation marks.
# Both work the same, but it is important to be consistent and stick to one style throughout your code.
# Most Python style guides (such as PEP 8) recommend choosing one and using it consistently.
print('I am Iron Man')

# Triple quotes (""" """) allow you to create a multi-line string.
# This lets text span multiple lines while preserving line breaks and formatting.
# print() outputs the entire multi-line string to the console exactly as written.
print("""I am Iron Man
No, I am Tony Stark
No, I am Poppy""")

# The + operator is used to concatenate (join) multiple strings together.
# Each string is combined into one single string before being printed to the console.
print("I am Iron Man." + " No, I'm Tony Stark." + " No I am Poppy.")

# \n is an escape character that creates a new line in a string.
# It tells Python to move the cursor to the next line when printing text.
# This allows multiple lines of output to be displayed from a single string.
print("I am Iron Man.\n" + "No, I'm Tony Stark.\n" + "No I am Poppy.")

# The * operator repeats a string a specified number of times.
print("I am Poppy\n" * 100)
