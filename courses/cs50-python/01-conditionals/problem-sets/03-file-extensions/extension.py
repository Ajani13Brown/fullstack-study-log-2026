# -------------------------------------------------------------------------
# CS50 Python – Problem Set 3: File Extensions
#
# Focus: String methods + conditional logic for suffix matching
# -------------------------------------------------------------------------


# Problem: File Extensions

# Goal:
# - Prompt the user for a file name
# - Determine the file’s media type based on its extension (case-insensitive)

# Supported Extensions:
# - .gif   = image/gif
# - .jpg   = image/jpeg
# - .jpeg  = image/jpeg
# - .png   = image/png
# - .pdf   = application/pdf
# - .txt   = text/plain
# - .zip   = application/zip
# - Output "application/octet-stream" for unknown or missing extensions
#--------------------------------------------------------------------------------



#
# Approach:
# -  Prompt user to enter file name with input()
# - Utilize .strip method to remove white space
# -  match conditional operator to evaluate conditions with a single value 
# - Utilize .strip() method to remove leading or trailing whitespace
# - Utilize .endswith() method to print message based on ending suffix

# Solution:

def extention():
    file_name = input("File name: ")

    if file_name.strip().endswith(".gif"):
        print()
    elif file_name.strip().endswith(".jpg") or file_name.strip().endswith(".jpeg"):
        print("image/jpeg")
    elif file_name.strip().endswith(".png"):
        print("image/png")
    elif file_name.strip().endswith(".pdf"):
        print("application/pdf")
    elif file_name.strip().endswith(".txt"):
        print("text/plain")
    elif file_name.strip().endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

extention()


# Challenge (Optional):
# - After attempting the problem using the match operator,
# - I realized it does not accommodate the condition-based logic required
# - Switched to using if/elif/else for clearer and more appropriate control flow