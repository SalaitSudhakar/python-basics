# __name__
""" It is a special built-in variable that represents the name of the current module.
The name of variable is automatically set by Python interpreter when a module is imported
as a main program.
When a module is imported, __name__ is set to the module name.
However, when a program is executed as a main program, __name__ is set to the string "__main__"
"""

import my_module

print("Importing my_module.")
print(my_module.greeting())
