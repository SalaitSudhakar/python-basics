# *args :
"""This allows a function to accept an arbitrary number of positional arguments."""
# Example :
def add_numbers(*args): # You can use other variable name instead of args like *numbers.
    """This function accepts n number of , add them together ,and returns total"""
    # adding arguments using for loop. *args packs arguments in tuple.
    total = 0
    for number in args:
        total += number

    return total

# Call the function with desired number of arguments
result = add_numbers(2, 3, 5, 7)
print(result)
# call the function with additional arguments
result = add_numbers(2, 3, 6, 8, 9, 56, 45)
print(result)

# Note:
# *args keyword stores the arguments in a tuple.
# variable length arguments should be placed after other positional arguments.
# Or at least use keyword arguments. ex: def add_numbers(name, age, *args):
# Because the positional arguments you enter after *args will be taken by them and
# stored in a tuple data structure.


# **kwargs
"""This allows function to accept an arbitrary number of keyword arguments. 
That means **kwargs would accept any number of keyword arguments.
**kwargs value(arguments) are packed in a dictionary
"""

# Example :
def print_name_and_age(**kwargs):
    print(kwargs)

print_name_and_age(name="Virat", age=34)
