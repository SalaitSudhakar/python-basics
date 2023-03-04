# Prompt the user to enter two numbers and an operator
print("Welcome to my calculator!")
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
print("""Choose any operator to perform arithmetic operation:
    Enter '+' for addition
          '-' for subtraction
          '*' for multiplication
          '/' for division
""")

operator = input("Enter any operator: ")

# Perform the requested arithmetic operation
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print("Invalid operator.")

# Display the result
print(f"{number1} {operator} {number2} = {result}")

f""" Formatted string improves the code readability.
2 ways to format a string:
# using built in format() method :
1) print('{number1} {operator} {number2} = {result}'.format(number1, operator, number2, result)

# using f-string method :
2) print(f'{number1} {operator} {number2} = {result}')
"""

