# Functions

# Defining a function
def greeting(): # use 'def' keyword to define a function
    print("Good Morning!")
    print("Have a nice day.")

# To execute a code block inside a function, you have call it's name.
greeting()

# Example 2 :
def add_numbers(): # Defining a function
    """This function takes two numbers prompt from user and add them."""
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter another number: "))
    sum_of_numbers = number1 + number2
    print(sum_of_numbers)

add_numbers()

# Note :
""" In function, we can add comments using triple quote like above in add_numbers()
function which is known as docstring.
you can access the comment using function_name.__doc__ , don't use parentheses while 
writing function_name here.
"""
# Example :
print(add_numbers.__doc__)


# Functions with inputs
""" 'Parameter' is a name of variable in which data been passed in, which is defined when a defining a function.
'Argument' is a actual value which is passed in when calling a function.
"""

# Example for functions with input:
def greet_with(name):
    """ name is a parameter which gets actual value when calling the function which is known as arguments."""
    print(f"Hello {name}!")
    print("Good Morning.")

# call greet_with function
greet_with("sudhakar")  # If you forget to give the value to parameter, program will raise error.

# Types of arguments
""" There ara two types of arguments 
1) positional arguments 2) keyword arguments"""

# Positional arguments
""" Problem statement:
Create a program using maths and f-string that tells us how many day, weeks, months we
have left if we live until 90 years old.
"""
def life_remaining(name, age):
    """ This function takes name and age as input and returns their months, weeks and
    days left in this world"""
    years = 90 - age # calculates years left
    months = years * 12 # months left
    weeks = years * 52 # weeks left
    days = years * 365 # days left
    life_left = f"hello {name}!\nYou have {months} months, {weeks} weeks and {days} days left in this word."
    print(life_left)

# calling the function
life_remaining("Hagrid", 55)

# Explanation
"""while calling this function you have assigned two arguments.
Here, first argument assigned to first parameter and second argument assigned to 
second parameter. If you change the order of argument, you will not get a desired
result."""

# Keyword argument
""" To avoid above problem keyword arguments are used. we can take above function as a
example here also."""

# Just need to change argument assignment while calling the function
life_remaining(age=55, name="Hagrid")
""" if you change the order without keyword, you will get a error."""
