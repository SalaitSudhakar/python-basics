# input():
""" input() function used to get any details from user.
The value user enters after prompt is always a str object type.
"""

# Example 1 :
name = input("What is your name? ")
age = input("What is your age? ")
print("My name is", name, "and i am", age, "years old.")

# Exercise 2:
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print(first_name + last_name) # Like this, adding two str known as a string concatenation

# Example 3 :
number1 = input("Enter a number: ")
number2 = input("Enter another number: ")
print(int(number2) + int(number2)) # changing the value from one data type to another known as type casting

""" If you add to numbers that you get from user by input function means that number will be in string class.
example: num1 = input(enter: ) # 22
         num2 = input(enter: ) # 33
         print(num1 + num2) 
the result will be 2233 instead 55. because Python interpreter take them as str. 
So if you want the inputs to be taken as a numbers you have to convert the data type from str to int.
Converting a value from one data type to another known as type casting.
You cannot use other operators except '+' to do operations in strings.
int() - to convert into integer
float() - to convert into floating point number
str() - to convert into string object
bool() - to convert into Boolean object
"""

# type() :
""" type() functions used to check the type of any value or Variable. """
print(type(10))       # <class 'int'>
print(type(18.0))     # <class 'float'>
print(type("Sachin")) # <class 'str'>
print(type(12 > 15))  # <class 'bool'>


# Expression :
""" In Python, expression are evaluated by operator precedence, which determines the order in which operators are evaluated 
P - Parentheses ()
E - Exponentiation **
D - Division / -> //
M - Multiplication * -> %
A - Addition +
S - Subtraction -
In above order operators are evaluated.
"""
# Example :
result = (10 - 3) ** 2 + 123 / 3 * 2
print(result)

""" Always values inside a parentheses first evaluated. Then exponentiation, division etc... 
as per above PEDMAS Rule.
let me explain above example.
step1 : first the expression inside a parentheses evaluated. 7 ** 2 + 123 / 3 * 2
step2 : exponentiation operation evaluated. 49 + 123 / 3 * 2
step3 : then division - 49 + 41.0 * 2 
step4 : multiplication -   49 + 82.0 
final step - 131.0
"""