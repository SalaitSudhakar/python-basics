# Arithmetic operator

# Arithmetic operator perform mathematical operation on numbers
num1 = 5
numb2 = 3
# Addition operator '+'
print(num1 + numb2)
# Subtraction operator '-'
print(num1 - numb2)
# Multiplication operator '*'
print(num1 * numb2)
# Division operator '/'
print(num1 / numb2)
# Modulus operator '%' - this return remainder after dividing 2 values
print(num1 % numb2)
# Exponentiation operator
print(num1 ** numb2)


# comparison operator
"""
This operators compare two values or variables and return a Boolean value ( True or False)
"""
# <
print(num1 < numb2) # checks whether num1 less than num2 or not
# >
print(num1 > numb2) # checks whether num1 greater than num2 or not
# ==
print(num1 == numb2) # checks whether num1 equal to num2 or not
# != (not equal to)
print(num1 != numb2 ) # checks whether num1 not equal to num2 or not


#Logical operator
"""
these operators combine two or more Boolean expressions and return a Boolean value.
"""
number1 = 5
number2 = 2
number3 = 8
# and
print(number1 > number2 and number2 < number3) # this will be True only when both the conditions are True
# or
print(number1 < number2 or number2 < number3)  # This will return True when one of them is True
# not
print(not number1 == number2) # This returns opposite of what that condition returns


# Assignment operator
"""
These operators are used to assign a value to variable
"""
# = :
a = 6 # assign right side value to left

# += :
a += 3 # similar  to a = a + 3
print(a)

# -=:
a -= 4 #
print(a)

# *= :
a *= 5
print(a)

# /=:
a /= 5
print(a)

# **= :
a **= 3
print(a)


# Membership Operator
"""
These operators test whether a value or variable is a member of sequence or collection
"""
str1 = "Harry Potter is one my all time favourite movies."
# in
print('Harry' in str1) # checks whether "Harry" is in str1 or not and return True or False.
# not in
print('Black' not in str1) # checks the "Black" not in str1. If the value not in str1 return True. else, return False


# Identity operator
"""
These operator test whether two variables refers to same object in memory.
"""
a = 5
b = 5
# is
print(a is b)

# NOTE :
"""
1) If the same value assigned to multiple variables, then a reference to the same object is created in memory.
This means that all the variables will refer to the same memory location where the value is stored. 
so above code will return true
"""

b = 4
# is not
print(a is not b)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
print(list1 is not list2)

"""
Even though value of both list's value are same it is two distinct objects stored in a memory. So it is False.
"""
