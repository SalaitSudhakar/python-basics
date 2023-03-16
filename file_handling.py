# File handling
"""File I/O (input/Output) operations in Python refer to the ability to read from and
write to a file.
"""

# 1) Reading a file:
# open() method :
# file = open("example.txt", mode="r") # open the file in r - read mode,
# # by default open() uses 'r' read mode as argument, it is not necessary to mention it
# # Read the entire file
# content = file.read()
# print(content)
# file.close() # Closing file is important, Because it will leak memory.
# This will create FileNotFoundError : Because there is no file name example.txt. So, before reading a file write to it.
# Because if you open a file in "w"- writing mode , if the file not exist it wil create the file we specified.

# Writing to a file :
file = open("example.txt", mode="w")
file.write("Hello, World!\n") # Write mode will overwrite the entire file's content if file already exists with some content
file.close()

# Appending to a file :
file = open("example.txt", "a") # append (a) mode will append to a existing content of a file
file.write("This is a new line.")
file.close()

# with phrase :
# The "with" statement in Python is used to ensure that a resource, such as a file, is properly manages and cleaned up
# when the block of code using it is exited. This statement will automatically close the file.
# So, You don't need to explicitly close a file
with open("example.txt") as file:  # it will open example.txt file in read mode and store it in file variable
    content = file.read()
    print(content)
# Once the block of code in "with" statement exited, it automatically closes the file.

# readline():
# readline() is used to read a single line in a file
with open("example.txt") as file:
    line = file.readline()
    print(line)

# readlines() :
# It is used to read all the lines of a file and return them as a list of strings
# Each string represent a single line of the file.
with open("example.txt") as file:
    lines = file.readlines()
    print(lines)

# modes in file operations :
# "r" - read mode
# "w" - write mode (overwrite the existing data of a file)
# "a" - append mode (to append new content to existing content)
# "b" - Binary mode (To read image, audio, video files, only can read the file)
# "r+" - read and write mode (can read and write in same time)
# "x" - Exclusive creation mode (To create a new file and open it for writing.
# If a file already exist, python will raise error)


