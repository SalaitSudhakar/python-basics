# List :
"""List is a primitive data structure which accepts any type of data in it.
It is defined by enclosing a comma-separated sequence of items within a square bracket [].
A list is an ordered, mutable and iterable data structure.
# ordered :
Every element has its own index. Index starts from 0.
# mutable :
You can add new element and override or replace existing element
# iterable :
Iterable means you can loop through individual items in a list.
"""

# Creating a list :
# It can be created by defining a sequence of items within a square bracket.
# Example :
# I am going to take this list for most of the operation
MY_LIST = [1, 23, 34.0, "Hello", True]

# Accessing element (indexing) :
# Indexing starts from zero
print(MY_LIST[0]) # output: 1 (fist item in the list)
print(MY_LIST[3]) # output : "Hello (fourth item in the list)
print(MY_LIST[-1]) # output : True (it prints last element in the list). '-1' index starts from end of the list
print(MY_LIST[-2]) # output : "Hello (second element from last)

# Slicing : [start:stop:step]
# It is used to extract a subset of element from a list
print(MY_LIST[:]) # output: [1, 23, 34.0, 'Hello', True]. It prints entire list
print(MY_LIST[1:]) # output: [23, 34.0, 'Hello', True]. It prints elements from index 1 to rest of the list element
print(MY_LIST[1:3]) # output: [23, 34.0]. It prints elements from index 1 up to (not included) 3
print(MY_LIST[::2]) # output: [1, 34.0, True]. It prints elements from alternative index
print(MY_LIST[::-1]) # output: [1, 34.0, True]. It reverses the list
print(MY_LIST[-1:-5:-1]) # output: [True, 'Hello', 34.0, 23]. It prints 4 elements from last
print(MY_LIST[-1::]) # output: [True]. It prints last element in list
print(MY_LIST[-1::-1]) # output: [True, 'Hello', 34.0, 23, 1]. It prints reversed version of the list


# Adding element to a list :
# 1) append() method :
MY_LIST.append("Sachin")
MY_LIST.append("Virat")
print(MY_LIST) # output : [1, 23, 34.0, 'Hello', True, 'Sachin']

# 2) "+" operator :
new_list = MY_LIST + [False, "Harry"]
print(new_list) # Output : [1, 23, 34.0, 'Hello', True, 'Sachin', 'Virat', False, "Harry"]


# Removing elements :
# 1) del keyword :
del MY_LIST[-3] # 0r del MY_LIST[5]
print(MY_LIST) # Output : [1, 23, 34.0, 'Hello', 'Sachin', 'Virat']

# You can del MY_LIST, which will delete the list completely not just elements
# And If you try to print MY_LIST, you will get NameError: name 'MY_LIST' is not defined

# 2) pop() method :
popped_element = MY_LIST.pop() # it will last element in a list and returns that element. You can print that element
print(popped_element)

# Also, if you enter any index inside pop(0), it will remove that element and returns that element
popped_element = MY_LIST.pop(0)
print(popped_element)

# 3) remove() method :
# To remove an item using the value, you can use remove() method
MY_LIST.remove("Hello")
print(MY_LIST)

# Updating element or changing the value of existing element :
MY_LIST[0] = "Virat" # This will replace the element in index 0 with new value "Virat"
MY_LIST[1] = "Cricket"
print(MY_LIST)

# len() function to find the length or number of elements in a list :
length_of_list = len(MY_LIST)
print(length_of_list)

# Checking membership :
# The 'in' and 'not in' operators can be used to check, if an element i present in a list or not
print("Virat" in MY_LIST)
print(1 not in MY_LIST)

# sorting a list :
# It sorted out the list in ascending order
MY_LIST.sort() # It sorts the list with ASCII value of alphabets
print(MY_LIST)
# reverse parameter
new_list = [22, 3, 54, 6, 15]
new_list.sort(reverse=False) # "reverse" Parameter used to reverse the sorted list
# Key parameter : it takes a function as argument
new_list.sort(key=lambda x: x % 2 ==0, reverse=False)
# This above function finds odd number and after sorted out, Python prioritise odd numbers then it places even number
print(new_list)

# count() method :
# It counts number of occurrence of a specified element in a list
new_list = [2, 5, 6, 7, 2, 5, 2]
count_of_2 = new_list.count(2)
print(count_of_2)

# clear () method :
# It clear out (removes) every element in the list and make it empty
new_list.clear()
print(new_list)

# Copying a list :
new_list = MY_LIST.copy()
print(new_list)

# insert element at any index :
MY_LIST.insert(1, "India")
print(MY_LIST)
