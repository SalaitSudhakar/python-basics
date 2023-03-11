# Tuple :
""" A tuple is an ordered, immutable collection of elements.
It is similar to list, but unlike a list, the elements of tuple cannot be changed
once it created. You cannot add new element to a tuple.
"""

# 1) DEFINING A TUPLE :
# Empty tuple = ()
print(())
# 1) Use comma separated values within a parentheses
colors = ("red", "green", "blue")
print(colors)
# 2) You can even create a parentheses without using parentheses
numbers_tuple = 1, 2, 3, 4
print(numbers_tuple)
# 3) To create a tuple with just one element
one_element_tuple = 1,
print(type(one_element_tuple))
print(one_element_tuple)

# Note :
# You can create tuple without parentheses. But you cannot create them without comma.

# 2) ACCESSING ELEMENTS :
# You can access tuple with using indexing
colors_tuple = ("red", "green", "blue")
print(colors_tuple[0]) # Output : red
print(colors_tuple[2])  # Output : blue

# 3) UNPACKING A TUPLE :
# Tuple unpacking allows you assign the elements of a tuple to multiple variables at once.
# Example 1 :
num1, num2 = (1, 2)
print(num2)
print(num1)

# # Example 2 :
# number1, number2 = 10, 20, 30
# print(number1)
# print(number2)
# # You will get ValueError : too many values to unpack

# Extended unpacking
# You can solve above problem using * operator
color1, color2, *colors = ("red", "green", "blue", "orange", "purple", "yellow")
print(color2)
print(color1)
print(colors)
print(type(colors))
# * operator unpacks the remaining elements in the variable named colors.
# and returns a list object

# you can do lots of other operation like in list :
# len()
MY_TUPLE = (1, 3, 5, 4, 5, 6)
print(len(MY_TUPLE))

# slicing
print(MY_TUPLE[1:5])
print(MY_TUPLE[-1:-6:-1])
print(MY_TUPLE[::-1])
print(MY_TUPLE[:])

# index()
print(MY_TUPLE.index(3))
print(MY_TUPLE.index(6))

# Concatenation :
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)

# Repetition
# It duplicates elements of existing element for specified time
print(MY_TUPLE * 2)

# max()
print(max(MY_TUPLE))

# min()
print(min(MY_TUPLE))

# Sorting :
# It will return a new sorted list
# Example :
sorted_tuple = tuple(sorted(MY_TUPLE)) # It sorts the elements and store it in list
print(sorted_tuple)

# NOTE :
# Because tuple is immutable, you cannot do append(), insert(), pop(), remove(), discard() operations.
