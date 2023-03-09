# List comprehension :
""" It is concise way of creating list based on existing list."""
# Syntax :
# [ expression for item in list if condition]

# Example 1 :
numbers = [1, 2, 4, 5]
squared_numbers = [number ** 2 for number in numbers] # it is concise way of iterating a list
print(squared_numbers)

# Example 2 :
even_numbers = [ number for number in range(10) if number % 2 == 0]
print(even_numbers)

# example 3 :
my_list = [1, 2, 3, 4, 5, 3, 7, 9]
new_list = [number if number % 2 ==0 else -number for number in my_list ]
print(new_list)


# list unpacking :
# List unpacking allows you to assign the elements of a list to multiple variable at once
# Example :
my_list = [1, 2, 3]
num1, num2, num3 = my_list
print(num1)
print(num2)
print(num3)

# Example 2 :
colors = ["red", "Blue", "Green", "Yellow", "Orange", "brown"]
color1, color2, *other_color = colors
print(color1)
print(color2)
print(other_color)

# Explanation :
# First two elements assigned to first 2 variables in a list respectively.
# Because of * sign, the other variable packs the remaining variable in a list
