# -------------------------------------------------------------------------
# CS50 Python – Problem Set 5: Meal Time
#
# Focus: String parsing + functions + conditional logic for time ranges
# -------------------------------------------------------------------------


# Problem: Meal Time
#
# Goal:
# - Prompt the user for a time in 24-hour format (e.g., "7:30", "13:00")
# - Convert the time into a float representing hours (e.g., 7.5)
# - Output "breakfast time", "lunch time", or "dinner time" based on:
#   - Breakfast: 7:00–8:00
#   - Lunch: 12:00–13:00
#   - Dinner: 18:00–19:00
# - Output nothing if the time does not fall within these ranges
# - Treat all time ranges as inclusive
#----------------------------------------------------------------------------------------------------


# Approach:
# - Prompt user for time using input() and store it in variable "time"
# - Convert string time into hours and minutes variables using "hours, minutes = time.split(":")"
# - Convert hours and minutes into float values
# - Divide minutes by 60 and add to hours to get decimal time
# - Assign return value of convert() function to variable "meal"
# - Use conditional logic based on meal value to print meal time message


# Solution:

def main():
    time = input("What time is it?: ")
    meal = convert(time)
    print(meal)

    if 7.0 <= meal <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal <= 13.0:
        print("lunch time")
    elif 18.0 <= meal <= 19.0:
        print("dinner time")
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    conversion = float(hours) + float(minutes) / 60
    return conversion


if __name__ == "__main__":
    main()


# Challenge (Optional):
# - Initially struggled converting hours and minutes into a float representation
# - Conditional output did not display correctly due to incorrect comparison logic
# - Issue was caused by using inverted comparison operators (>/<)
# - Adjusted conditional logic to correctly evaluate time range