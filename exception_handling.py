# Try-Except
# Try-Except block allows you to try a piece of code and catch any exceptions(errors)
# that occur during execution, then take appropriate action based on type of error.

try:
    # code that may raise an error
    num1 = int(input("Enter a number:  "))
    num2 = 10 / num1
except ValueError:
    # Handle value error
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("A number cannot be divided by zero")
except Exception as e:
    # Handle other type of error other than above mentioned
    print("An error occurred", e)
else:
    # Executed only if no exceptions are raised
    print("Result: ", num2)
# else clause will only be executed if try clause raises no error.

# finally: clause
# Block of code in finally clause will be executed no matter what,
# whether an exception was raised or not
try:
    file = open("example.txt")
    content = file.read()
except FileNotFoundError:
    print("File Not Found!")
else:
    print(content)
    print("File opened successfully.")
finally:
    file.close()
    print("File closed.")

# 1) else clause will be executed only if file is existed and no error was raised.
# 2) finally clause will be executed no matter what

# raise statement:
# You can raise your own exceptions using the "raise" statement.
# Raising on exception is away to signal that an error has occurred in your code.
# It allows you to handle error that are not caught by Python interpreter
# but that's inappropriate to your application

class InvalidInputExecption(Exception):
    pass

def validate_input(input_str):
    if not input_str.isnumeric():
        raise InvalidInputExecption("Input must be a positive integer.")
    return int(input_str)


try:
    user_input = input("Enter a positive number: ")
    num = validate_input(user_input)
    print(f"The square of {num} is {num ** 2}")
except InvalidInputExecption as e:
    print(f"Error: {e}")



