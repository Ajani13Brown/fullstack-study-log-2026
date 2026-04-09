# --------------------------------------------------------------------------------------------------
# F-STRING FORMAT SPECIFIERS - Notes

#  Deep dive into format specifiers while taking notes on CS50 Python Lecture 00 (Functions, Variables)
# Video: https://www.youtube.com/watch?v=JP7ITIXGpHk&t=4758s   
# Course page: https://cs50.harvard.edu/python/weeks/0/

# GENERAL SYNTAX
# f"{value:format_spec}"

# value = variable or expression to display
# ":" = starts formatting instructions
# format_spec = rules for how the value should look

# Think:
# "Take value and DISPLAY it like this"

# Full structure order:
# {value : fill align width .precision type}
# Not all parts are required

# Based on Python Official Documentation:
# https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings
# https://docs.python.org/3/library/string.html#format-specification-mini-language

# --------------------------------------------------------------------------------------------------

# THOUSANDS SEPARATOR

x = 1
y = 999
z = x + y

print(f"{z:,}")      # 1,000

# "," adds commas every 3 digits
# Useful for large numbers like money or population
# --------------------------------------------------------------------------------------------------

# DECIMAL PRECISION

pi = 3.14159
print(f"{pi:.2f}")    # 3.14

# Breakdown of :.2f
# "."  = start decimal precision section
# "2"  = number of digits AFTER decimal point
# "f"  = display as floating-point number

# So 3.14159 becomes 3.14

# If you remove the "."
print(f"{pi:2f}")     # width = 2, NOT decimal precision

# Without ".", Python uses default float precision (~6 decimals)

# Increase decimals:
print(f"{pi:.4f}")    # 3.1416

# Remove decimals:
print(f"{pi:.0f}")    # 3  (rounded)

# NOTE
# :.0f only changes DISPLAY, pi is still a float in memory
# --------------------------------------------------------------------------------------------------

# PERCENT FORMAT

score = 0.875
print(f"{score:.1%}")   # 87.5%

# What "%" does:
# 1. Multiplies the number by 100
#    because percent means "per 100"
#    0.875 * 100 = 87.5
# 2. Adds "%" symbol
# 3. Applies decimal precision

# Breakdown of :.1%
# "."  = start decimal precision
# "1"  = show ONE digit after decimal
# "%"  = multiply by 100 and add percent sign

# More examples
print(f"{score:.0%}")   # 88%  (rounded whole number)
print(f"{score:.2%}")   # 87.50%

# If written as :1%
print(f"{score:1%}")    # width = 1, NOT decimal precision

# Works with integers too
print(f"{1:.0%}")       # 100%

# NOTE
# Percent is usually used with decimals like 0.5 = 50%
# --------------------------------------------------------------------------------------------------

# WIDTH, ALIGNMENT, AND PADDING  (COMBINED SECTION)

name = "Ajani"

print(f"{name:>10}")    # Right aligned
print(f"{name:<10}")    # Left aligned
print(f"{name:^10}")    # Center aligned

# Breakdown of :>10
# ">" = align right
# "<" = align left
# "^" = center
# "10" = TOTAL width of field (not number of spaces)

# Example:
# "Ajani" has 5 characters
# Width 10 means total result must be 10 characters
# So 5 spaces are added

# If value is LONGER than width
print(f"{'LongerThanTen':>10}")
# No trimming happens, Python just prints full text

# CUSTOM FILL CHARACTERS
print(f"{name:_>10}")   # _____Ajani
print(f"{name:*^10}")   # **Ajani***

# Breakdown of :_>10
# "_" = fill character
# ">" = align direction
# "10" = total width

# Order is:
# fill + align + width

# Common real example of padding numbers
n = 42
print(f"{n:05}")        # 00042
print(f"{n:1>5}")       # 11142

# NOTE
# Width is total width, not number of leading zeros
# --------------------------------------------------------------------------------------------------

# SCIENTIFIC NOTATION

big = 1234567
print(f"{big:.2e}")     # 1.23e+06

# Breakdown of :.2e
# "."  = decimal precision
# "2"  = digits after decimal
# "e"  = scientific notation

# Scientific notation means:
# number written as:
# a x 10^n

# Example:
# 1.23e+06 means
# 1.23 x 10^6
# = 1.23 x 1,000,000
# = 1,230,000

# Why not exactly 1,234,567 ?
# Because rounding happened when keeping only 2 decimal digits

# More examples
print(f"{big:.4e}")     # more precision

# NOTE
# "e" stands for exponent
# Used for very big or very small numbers
# --------------------------------------------------------------------------------------------------

# FORMAT SPECIFIER ORDER

# Structure reminder:
# {value : fill align width .precision type}

num = 12.3456
print(f"{num:0>10.2f}")   # 0000012.35

# This combines:
# fill + align + width + precision + type
# --------------------------------------------------------------------------------------------------

# TYPE SPECIFIERS - COMMON ONES

# f = float
# d = integer
# e = scientific notation
# % = percent
# s = string (default)

num = 3.9
print(f"{num:.0f}")   # 4  float displayed like integer

# IMPORTANT
# Format specifiers change DISPLAY only
# They do NOT change the real data type

print(type(num))      # still float

# Real conversion requires functions
# int(), float(), str(), list(), bool()
# --------------------------------------------------------------------------------------------------

# KEY RULE TO REMEMBER

# Format specifiers change HOW a value LOOKS
# They do NOT change WHAT TYPE it is

# f-strings mainly format numbers and strings
# Lists and dictionaries use default string display

num = 3.9
print(f"{num:.0f}")   # shows 4
print(type(num))      # still float

# Real type conversion uses functions:
# int(), float(), str(), list(), bool()
# --------------------------------------------------------------------------------------------------
