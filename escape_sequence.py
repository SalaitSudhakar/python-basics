# Escape Sequence
""" An escape sequences is a combination of characters that represents a special
characters or a series of characters that cannot be typed directly in string literal."""

# 1) Newline character(\n):
# It is used to insert a new line break in a string
# Example :
print("Hello\nworld")
print("Welcome\nThank you")
# The characters after \n will be printed in next line.

# 2) Tab character(\t) :
# It is used to insert a horizontal tab in a string.
print("Name\tAge")   # Name    Age
print("Virat\t34")   # Virat   34

# 3) To escape single or double quote(\' or \")
# This backslash is used to include a quotes in a string
# print('Welcome to coder's')
# if you use single quote to represent the string outside you cannot use single quote
# inside of that string which will raise an index error
# so backslash is used to escape the quote. these are similar to double quote also
print('welcome to coder\'s world') # backslash will help you avoid error
print("He said, \"Hello, world\"") # so the double quote will be printed

# 4) Backslash character(\\)
# '\' is taken as a escape character by Python interpreter.
# So it will not be included in printed statement
# example : print("c:\users\John\documents") output: c:usersJohndocuments
# So it will not include \. So to escape '\' you can use double '\\'
print("c:\\users\\John\\documents") # Output : c:\users\John\documents

# 5) Backspace character(\b):
# It is used to move curser back to one space in a string
print("Hello\bWorld") # Output: Hellworld
# Cursor moves back to one space
print("Hello \bWorld") # Output: HelloWorld

# 6) Carriage return character(\r):
# It is used to return the cursor to the beginning line in a string
print("Welcome to my \rgithub") # Output : github
# It takes the cursor to the beginning, here it takes world to the beginning and removes "welcome to my"
print("Hello \r world") # Output :  World

# 7) r" " - raw string:
# A raw string tells Python to treat backslashes(\) as literal characters rather than as the start of an escape sequence character
# print("c:\\users\\John\\documents") instead of using backslash to escape a backslash from Python interpreter,
# you can use raw string which tells Python to take whatever inside a string as it is.
print(r"C:\user\John\document") # Output: C:\user\John\document

