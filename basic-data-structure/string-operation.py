# String
""" String is sequence of characters which is immutable and ordered collection."""

# Creating a string :
# Use double or single quote to create a string
string = "Virat Kohli"

# concatenation :
first_name = "Virat"
second_name = " Kohli"
name = first_name + second_name
print(name)

# Note :
# If you need a space between two concatenated string,
# you can give space after last character of first string (Ex): "Virat "
# or before first character of last string like in line 10. EX : " Kohli"
# or first_name + " " + last_name (add space by concatenating a spaced empty sting between two string

# Indexing : (accessing elements)
# You can access element using indexing
# example :
NAME = "Virat Kohli"
print(NAME[3]) # output : a (index starts from zero)
print(NAME[6]) # Output : K (space also counted as element of string

# slicing :
# You can slice string like in tuple amd list
print(NAME[::]) # Output : Virat Kohli
print(NAME[::-1]) # Output : ilhoK tariV
print(NAME[1:5]) # Output : irat
print(NAME[1:8:2]) # Output : ia o

# len() # To find a length of objects
print(len(NAME)) # 11

# upper() : converts all the letters into Capital letters
print("1234count".upper())
print(NAME.upper())

# lower() : converts all the letter into lower case letters
print(NAME.lower())

# swapcase() : converts capital letters into smaller ones and smaller letters into capital letter
print(NAME.swapcase())

# repetition : Multiplies every element specified times and creates a duplicate of tha characters
count_3 = NAME * 3
print(count_3)

# Comparison :
name1 = "Virat Kohli"
name2 = "virat kohli"
print(name2 == name1) # False
# Python is case-sensitive, so capital v and small v are not same

# title() : It converts first letter of all words into capital
name = "sachin Tendulkar"
print(name.title())

# capitalize() : converts first letter of first word into capital
print(name.capitalize())

#replace() : to replace any character or word with any word
print(NAME.replace("Kohli", "Sachin"))

# find() : it is used to find index of any word or letter
# It only gives the index of starting letter of that word.
print(NAME.find("l")) # If that letter or word doesn't exist it will return -1
print(NAME.find("Kohli"))

# count() : It counts occurrence of any letter or word.
print(NAME.count("Virat"))
print(NAME.count("i"))

# startswith() : it checks whether the string starts with specified letter or word
print(NAME.startswith("Virat"))
print(NAME.startswith("K"))

# endswith() : it checks whether the string ends with specified letter or word
print(NAME.endswith("Kohli"))
print(NAME.endswith("i"))

# Strip() : It removes the space in both side of a string
str1 = " Virat Kohli "
print(str1.strip() + "18")

# lstrip() : it removes space in left side of a string
print(str1.lstrip() + "Cricketer")

# rstrip() : it removes space in right side of a string
print(str1.rstrip())

# split() :
# This method is used to split a string into a list based on a delimiter.
# The delimiter can be a space , comma, semicolon or any other character.
# syntax : string.split(sep=, maxsplit=)
# delimiter(sep or separator) is used to split the string. Default delimiter is  space (' ')
name_list = NAME.split()
# it separates a strings before space and after space
# For example : "Virat Kohli", string before space "virat" and after space "Kohli"
# and store it in lit ["Virat", "Kohli"]
print(name_list)

# Example :
fruits_str = "apple, banana, grape, orange"
fruits_list = fruits_str.split(", ") # it splits the words before comma and after comma
print(fruits_list) # Output : ['apple', 'banana', 'grape', 'orange']


# maxsplit parameter : it is optional parameter
# That specifies the maximum number of splits to be performed
# example :
fruits_list_with_maxsplit = fruits_str.split(sep=", ", maxsplit=2)
print(fruits_list_with_maxsplit) # Output : ['apple', 'banana', 'grape, orange']

# join() method :
# This method is used to join a sequence of strings into a single string.
# SYNTAX : separator.join(sequence)
fruits = ["apple", "Orange", "cherry", "Guava"]
string1 = ", ".join(fruits)
print(string1)

