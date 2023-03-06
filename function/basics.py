# Functions

# Defining a function
def greeting(): # use the 'def' keyword to define a function
    print("Good Morning!")
    print("Have a nice day.")


# To execute a code block inside a function, you have call it's name.
greeting()

# Example 2 :
def add_numbers(): # Defining a function
    """This function takes two numbers prompted from user's and add them."""
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
""" 'Parameter' is a name of variable in which data being passed in, which is defined when a defining a function.
'Argument' is receives an actual value which is passed in when calling a function.
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
    days left in this world """
    years = 90 - age # calculates years left
    months = years * 12 # months left
    weeks = years * 52 # weeks left
    days = years * 365 # days left
    life_left = f"hello {name}!\nYou have {months} months, {weeks} weeks and {days} days left in this world."
    print(life_left)


# calling the function
life_remaining("Hagrid", 55)

# Explanation :
"""while calling this function you have assigned two arguments.
Here, first argument assigned to first parameter and second argument assigned to 
second parameter. If you change the order of argument, you will not get a desired
result.
"""

# Keyword argument :
""" To avoid above problem keyword arguments are used. we can take above function as a
example here also.
"""

# Just need to change argument assignment while calling the function
life_remaining(age=18, name="Harry")
""" if you change the order without keyword, you will get a error."""


# Default argument :
""" In Python you can add argument value during defining a function itself."""
# Example :
def average(num1, num2, num3=23):
    """This function gets three number inputs and finds average of numbers"""
    total_of_num = num1 + num2 + num3
    average_of_num = total_of_num / 3
    print(average_of_num)


average(num1=54, num2=34)

# Explanation :
""" In above function, you give 2 inputs as a argument when calling the function. but it has 3 parameters
num1, num2, num3. Because, the third parameter num3 has default argument, num3=23. So, you don't have to give
a value to that parameter. If you want to change the argument of num3 parameter, you can even change them while 
calling the function.
"""

# Example :
average(num1=3, num2=35, num3=65)
""" Here, num3 parameter will override the default argument."""


# return keyword :
""" You can use a outside variable(Global variable) inside a function. But, 
you cannot use a variable inside a function(Local Variable), outside anywhere in a program. so You can use 'return' keyword.
'return' keyword will be used in function to return something from a function. That returned value is stored in
function name. You can access that returned value outside of function using function name. 
"""
# Example :

def average(num1, num2, num3):
    total_of_numbers = num1 + num2 + num3
    average_of_numbers = total_of_numbers / 3
    return average_of_numbers


avg = average(23, 56, 78)
print(avg)


# Local scope of a variable
# Example :
def drink_potion():
    """ This function is just a example for explain local variable."""
    potion_strength = 2 # local variable
    print(potion_strength)


drink_potion()
""" Here, if you try to access potion_strength variable outside of a function, you will get error.4
It'll show potion_strength is not defined.
"""

# Global variable:
# Example :
player_health = 10 # Global variable
def drink_potion():
    potion_strength = 2 # Local variable
    print(potion_strength)
    print(player_health)


drink_potion()
""" Here, if you try to print player_health which is outside of a function(Global variable) which will work.
Global variable can be used anywhere in a program.
"""

# Note :
"""Local Variable : A variable inside a function is known as local variable which cannot be accessed outside of a function.
Global variable : Variable outside of a function is known as global variable which can be accessed anywhere in a
program.
"""


# Global Keyword :
""" If you want use local variable in outside of function, you can use 'global' keyword"""
# Example :
enemies = 1
def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}.")


print(f"enemies outside of function {enemies}.") # 1
increase_enemies() # 2
print(f"enemies outside of function after function execution : {enemies}") # 2

# Explanation :
"""In above function, you can see in line 174 , i have printed the enemies variable, before executing the function, 
the enemies value is 1.
In line 175, i have called the function, now i have changed the local variable into a global variable, now it's value is 2.
In line 176, because function already exist and the local variable changed into global variable, now you will only get a
variable enemies value as 2. 
"""
