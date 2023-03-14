# Module
""" A module is simply a file containing Python code that can be imported
and used in other Python programs.
"""

# Different ways to import a module
# 1) import <module-name>
import sample_module
print(sample_module.virat_kohli())

# 2) import module name as alias
import sample_module as sample
print(sample.virat_kohli())
# You can call this module using alias name

# 3) from module-name import function-name
from sample_module import virat_kohli
print(virat_kohli())
# you don't need to specify the module name. Here, you can directly use function name

# 4) from module-name import *
from sample_module import *
print(virat_kohli())
# It imports all the functions now, you can directly use the functions without specifying module name
