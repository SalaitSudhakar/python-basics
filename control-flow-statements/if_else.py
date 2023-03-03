# 1) if statement :
""" 'if' statement is used to execute a block of code only if a condition is True. """

# Example 1:
age = input("Enter your age: ")
if int(age) >= 18:
    print("You're eligible to vote.") # use 4 space to indent this line
    print("Let's go and vote.")

# Explanation :
""" in line 5, it gets prompt from you for your age. line 6, converts your input into integer using int().
then checks whether your age is greater than or not. If True, then the block code indented beneath the if 
statement will be executed. If false, nothing happens.
"""

# note
""" If you don't indent line 7, you will get error. But if you don't indent the line 8 or kept that 
line in a same indentation level as if statement, it will be executed independent of if statement. 
That means, it will executed always whether the condition is True or False
"""


# 2) if....else statement :
"else statement only executed when if statement is False"

# Example 2:
age = input("Enter your age: ")
if int(age) >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")

# 3) if...elif...else statement :
""" if 'if' statement becomes False, then 'elif' statement will be evaluated. if elif statement also become
 False, then else statement will be executed."""

# Example 3 :
age = input("Enter your age: ")
your_age = int(age)
if your_age < 5:
    ticket_price = 5
elif your_age < 13:
    ticket_price = 7
elif your_age <= 18:
    ticket_price = 10
else:
    ticket_price = 15
print("Your ticket price is $", ticket_price)

# Explanation :
""" in line 38, it get prompt for your age. line 39, converts it into integer.
in line 40, if checks whether your age is less than 5 or not. If True, executes it's block of code,
then prints line 48, program will be stopped. If False, then it checks elif statement in line 42.
It does the same process for next elif statement also. if nothing True, else block will be executed.
"""

# Note :
""" 
You can use multiple elif statement. But next elif statement only executed when above if..elif statement " \
is False. but if you use two if statement both of them will be executed even above if statement is True.
"""

# Ternary operator :
"it is short hand for if else statement"
# Example :
num1 = 5
num2 = 6
print("numb1 is less than num2" if num1 < num2 else "num1 is greater than num2")
