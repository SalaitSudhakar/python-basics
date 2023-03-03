# For Loop
""" The for loop is used to iterate over a sequence of values such as string, list, tuples, dict and
execute a block of code for each iteration. You can use for loop when know how many iteration required.
"""

# Example :
word = "Virat Kohli"
for letter in word:
    print(letter) # Indentation is very important. use 4 spaces to indent

# Explanation
""" line 7, string 'Virat Kohli' assigned to variable named word.
line 8, for loop iterate over character by character in a variable names word.
letter is variable which stores a character. it frees up the previous value, 
stores next character once the block of code is executed.
Then in line 9, each character is printed one after another.
"""

# range() :
""" The range() function used to generate a sequence of numbers within a specified range."""

# with one argument range(stop) :
for index in range(5): # it generates a sequence of number from 0 up to (but not included) 5
    print(index)       # prints numbers one by one

# with two arguments range(start, stop):
for index in range(1, 5): # it generates numbers from 1 up to (but not included) 5
    print(index)

# with three arguments range(start, stop, step):
for index in range(2, 12, 2): # it generates even numbers from 2 to up to (but not included) 12
    print(index)


# while loop :
""" The 'while' loop is used to repeatedly execute a block of code as long as certain condition is True.
You can use 'while' loop when you don't know how many iterations required.
"""

# Example:
x = 0
while x < 5: # code will be executed till this condition is True
    print(x)
    x += 1  # you need something to stop the loop. otherwise, it will run infinite time. Program will crash


# break keyword :
""" The 'break' keyword is used to exit a loop prematurely. When 'break' keyword is encountered 
inside a loop, the loop will immediately terminated, and control is transferred to the next statement 
after a loop
"""

# Example:
for index in range(0, 6):
    if index == 2:
        break       # when the index is 2, it breaks out of the loop and control is transferred to line after 57
    print(index)


# continue keyword :
""" The 'continue' keyword is used to skip over the rest of current iteration of a loop and move on to 
next iterators. That means, remaining statements of that iteration is skipped.
"""

# Example:
num = 0
while num < 5 :
    x += 1
    if num == 3:
        continue  # if the number is 3 then it stops the iteration here and move on to next iteration without executing line 71
    print(num)


# pass keyword:
""" The 'pass' keyword is used as a placeholder in a situation where a statement is requires syntaticallly,
(to avoid syntax error), but no action is required. When 'pass' keyword is encountered, nothing happens
and control is immediately transferred to next statement.
"""

# Example :
counter = 1
maximum = 10
if counter < maximum :
    counter += 1
# when above if statement become it will execute counter += 1. but in else clause if you don't want to happen anything, you can use pass key word
else:
    pass