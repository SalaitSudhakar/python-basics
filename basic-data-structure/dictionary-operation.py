# Dictionary
""" A dictionary is a collection of unordered, mutable elements that are stored in a key-value pair format.
The keys in a dictionary are unique and immutable, while the value can be of any data type.
"""

# Creating a dictionary :
# Key should not be any mutable object
# 1) empty dict :
empty_dictionary = {}
print(empty_dictionary)
# 2) key-value pairs
MY_DICT = {"name": "Virat", "age": 34, "jersey Number": 18}
print(MY_DICT)

# Accessing values in a dictionary :
# To access the values of a specific key, use the key inside the square bracket [] or get() method.
# Square bracket method
print(MY_DICT["name"])

# If you use square bracket to access element, if the key does not exist, you wil get error.
# You can avoid these error using get() method
# 2) get() method :
print(MY_DICT.get("age"))

# NOTE :
# The get() method also returns the default value, if the key does not exist.
# SYNTAX : get(key, value) -> it is a default value, if the key does not exist in dict, the default value wil be return.
# But this default value will not be added to the dict
print(MY_DICT.get("number of century", 74))

# modifying existing value or update it :
MY_DICT["name"] = "Kohli"
print(MY_DICT)

# Adding element :
# You can use the same method as modifying value of a existing key using [] method.
MY_DICT["number of century"] = 74
MY_DICT["profession"] = "Cricketer"
print(MY_DICT)

# Removing element :
del MY_DICT["age"]
print(MY_DICT)

# Looping through dict :
# If you loop through a dict like other data structure, it'll only iterate over keys.
for key in MY_DICT:
    print(key)

# So you can use items() method :
# Which loop through both keys and values
for key, value in MY_DICT.items():
    print(key, value)

# To get all the keys :
print(MY_DICT.keys())

# To get all the values :
print(MY_DICT.values())

# copy() : copying a dict
new_dict = MY_DICT.copy()
print(new_dict)

# clear () : to remove all the key-value pairs and make dict empty
print(new_dict.clear()) #None

# update() : Merging two dict
dict1 = {"Apple": 1, "Orange": 2}
dict2 = {"Berry": 3, "Cherry": 4}
dict1.update(dict2)
print(dict1)

# pop() :
# To remove a key-value pair from a dict. You can use pop() to delete a value of a key and return it
number_of_century = MY_DICT.pop("number of century")
print(number_of_century)
print(MY_DICT)

# popitem() :
# it removes last key-value pair in a dict
popped_item = MY_DICT.popitem()
print(popped_item)
print(MY_DICT)



