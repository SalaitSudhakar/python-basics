# Set
"""Set is an unordered collection of unique elements.
Characteristics of set:
1) Sets are unordered :
The items in a set have no specific order(index).
2) Sets are unique :
Each item appears only once in a set. It does not allow duplication of a element.
3) Sets are mutable :
You can add or remove elements from a set after it created.
4) Elements in a set cannot be changed. You cannot remove existing element.
"""

# 1) CREATING A SET:
# empty set
print({})
# create set using curly braces
number_set = {1, 2, 3, 4, 5}
print(number_set)
# Create a set using set() function
set_function = set("letter")
print(set_function)

# Note :
# Because sets are unordered, the order of elements may vary from each runs of a program.
# Also, it does not allow second occurrence of any item.

# Adding element : add()
MY_SET = {1, 2, "hello", "world"}
MY_SET.add(5)
print(MY_SET)

# removing elements : remove()
MY_SET.remove(1)
print(MY_SET)

# Note :
# if you enter the value that is not in MY_SET, Python will raise an error.
# MY_SET.remove(3)
# To avoid an error, you can use discard()

# discard(), it removes an item, if it exists. Otherwise, it does nothing. It'll help you avoid raising error
MY_SET.discard(3)
print(MY_SET)

# pop()
# Because set is unordered, it removes random item and return it.
popped_value = MY_SET.pop()
print(popped_value)

# IMMUTABLE SET : frozenset() function
# The frozenset() used to make a set immutable. It is a built-in function, which returns a new immutable set from existing one.
# Example :
frozen_set = frozenset(MY_SET)
print(frozen_set)

# TRY IT
# Try to add and remove item from frozen set. You will not able to do that. You can only copy that set

# Union() method:
# You can use union() method ot the '|' operator to get the union of two sets
# union() method adds two sets by eliminating duplicate element (second occurrence of a element).
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)
#or '|' operator
set3 = set1 | set2
print(set3)

# NOTE :
# union() method accepts iteration to perform operation
# operators only accepts sets

# Intersection : intersection() method
# When intersecting two or more sets, you'll get a new set which consisting of elements that exists in all sets
# 1) intersection() method :
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.intersection(set2)
print(set3)
# or '&' operator
set3 = set1 & set2
print(set3)

# Symmetric difference :
# The symmetric difference between two sets is a set of elements that are not common in both sets.
# or that are in either set, but not in both sets .
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.symmetric_difference(set2)
print(set3)
# Or "^" operator :
set3 = set1 ^ set2
print(set3)

# difference method :
# It returns a new set that contains all the elements in the first set that are not in the second set.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.difference(set2)
print(set3)
# Or '-' operator :
set3 = set1 - set2
print(set3)

# issubset () method  and superset() method:
# Suppose that you have two sets A and B. Set A is a subset of B, if all elements of A are also elements of B.
# Then set B is a superset of set A.
# Set A and set B can be equal. If set A and set B are not equal, A is a proper subset of B
# Example :
set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {4, 5}
# subset
print(set2.issubset(set1)) # It will return True or False by checking whether set2 is subset of set1 or not
print(set3.issubset(set1))

# superset
print(set1.issuperset(set2))
print(set2.issuperset(set3))

# isdisjoint () method :
# If two  sets have no common elements, it will return True.
# Example :
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}
print(set1.isdisjoint(set2))

