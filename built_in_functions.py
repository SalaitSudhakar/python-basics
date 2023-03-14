# Built-in functions are come with built-in with Python

# map():
# It applies a given functions to each element of an iterable
# and returns a new iterable object containing the result
# Example :
NUMBERS = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, NUMBERS)
print(list(squared))
# In line 9 the lambda function applies to each element in numbers list and return a new object
# It returns an object. So, to access the values, you can use for loop
# or convert it into any iterable object like list, tuple, set

# filter():
# This function creates a new iterable object from elements of an existing iterable that
# satisfies a certain condition
# SYNTAX : filter(function, iterable)
even_numbers = filter(lambda  x: x % 2 == 0, NUMBERS)
print(list(even_numbers))
# It returns a new object that satisfies the condition in  any type of function.

# reduce():
# It takes an iterable object and reduce it to a single value by applying a given function
# to each element of the iterable.
from functools import reduce
sum_of_numbers = reduce(lambda  x, y : x+y, NUMBERS)
print(sum_of_numbers)
# reduce() is not a built-in function. But it is also on the important functions in Python.
# It returns a single value by applying the function to the NUMBERS list

# enumerate():
# It adds a counter to an iterable and returns a enumerate objects.
# SYNTAX : enumerate(iterable, start)
# Start is a optional parameter which is 0 by default.
fruits = ["Apple", "Orange", "Cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
# Output :
# 1 Apple
# 2 Orange
# 3 Cherry

# zip() :
# It is used to combine two or more iterable objects into a single tuple
# where each tuple contains the corresponding indexed elements from the input iterables
# It takes two or more iterable objects as a argument
names = ["Harry", "Ron", "Hermoine"]
ages = [18, 20, 19]
heights = [1.7, 1.8, 1.6]
people = zip(names, ages, heights)
for person in people:
    print(person)
# Output:
# ("Harry", 18, 1.7)
# ("Ron", 20, 1.8)
# ('Hermoine', 19, 1.6)
# The resulting operator stops when the shortest iterable is exhausted.

# unzipping using zip()
people = [("Harry", 18, 1.7), ("Ron", 20, 1.8), ("Hermoine", 19, 1.6)]
names, ages, heights = zip(*people)
print(names) # Output : ('Harry', 'Ron', 'Hermoine')
print(ages)  # Output : (18, 20, 19)
print(heights)  # Output : (1.7, 1.8, 1.6)

# dir() :
# It returns a list of valid attributes and methods of specified object.
# If no object is specified, it returns a list of valid attributes of current namespace
print(dir()) # This will return methods and attributes in current file.
name = "Harry"
print(dir(name)) # This will return attribute and methods of str class

# help():
# This function provides help and documentation for a specified object or function.
# If no object is specified, it provides help and documentation for the current namespace
print(help(zip()))

# iter():
# It returns an iterator object for a specified iterable object.
# An iterable can be used to traverse an iterable object like list, tuple, set
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list) # It creates a object which is just a memory location
for num in my_iterator: # To access elements in a object we can use for loop or converting it to a iterable object
    print(num)

# divmod():
# It returns a tuple containing the quotient and remainder of dividing two numbers
# It takes two arguments. First one is the dividend and second one is divisor.
quotient, remainder = divmod(15, 4)
print(quotient)
print(remainder)

# isinstance():
# It returns "True" if the specified object is an instance of a specified class
# or a subclass and "False" otherwise.
# It takes two arguments : First object is to be  checked and second one is the class or
# tuple of classes to check against
num = 10
print(isinstance(num, int))
print(isinstance(num, (int, float))) # It checks whether num is instance of either of them.

# abs():
# It returns the absolute value of a number which is a positive number.
num = -125
print(abs(num)) # 125

