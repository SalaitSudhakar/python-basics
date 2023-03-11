# If you want the line that don't want to be considered or executed by Python interpreter, then comments are used.
# This line is a comment. Use '#' in the line to comment it.

""" For multi line comment you can use triple quotation
like this.
"""

# Print function used to display something.
print("my name is Harry.")

# printing multiple variables
name = "Harry"
age = 18
print("My name is", name, "and my age is", age)


# "sep" parameter. It is a seperator which separates the arguments. By default, the separator is space character
# without separator
print("Apple","Banana","Cherry")
# with separator
print("Apple", "Banana", "Cherry", sep=", ")


""" 'end' parameter. You can use "end" parameter to specify a string to be added after the arguments.
By default, the "end" parameter is a newline character("\n")
"""
# without end
print("Apple", "Banana", "Cherry")
print("Orange")
# with end
print("Apple", "Banana", "Cherry", end=" ")
print("Orange")
