import Fibo

# This is a script. Scripts end with .py and can be executed at a later date
# with a python interpreter.

# Scrips can be imported into other scrips (and the interpreter) to reuse their
# functions in another setting using the "import" keyword. Imports should be
# called at the beginning of the file or the function which needs them.

# These imported scrips are called modules, and their name is stored inside
# the __name__ variable. To call each function inside a module we must use its
# name. For example, notice the import Fibo.py in the top of the page.

print(Fibo.__name__)

# The name of the Fibo module is Fibo. To use its functions:

Fibo.fib(100)

# We can assign functions inside the module to local variables:

fibonacci = Fibo.fib
fibonacci(100)

# Each module has its own private sybol table, to not collide with the global
# environment. We can reach these variables using the modules name.
# Each module can have executables inside it that are meant to initialize
# itself on import. We can import specific functions from a module directly
# inside the global environment using

# from Fibo import fib1, fib2

# Note that this way Fibo is not needed to call the functions as they are
# directly brought to the local symbol table.

# The wildcard * can be used to import all functions, however it may be
# dangerous as it can overwrite local-defined functions. * ignores functions
# starting with an underscore (such as _export).

# The as keyword can change a Module's __name__ variable upon importing

# import Fibo as Banana

# the as keyword can be used im combination with from:

# from Fibo import fib as fibonacci

# To make a script executable, you can call it from the console using

# $python Fibo.py 50

# This will cause the module to be importer in the interpreter with the name
# "__main__". This can be exploited by using:

if __name__ == "__main__":
    import sys
    fibonacci(int(sys.argv[1]))

# Since sys.argv is the argument passed with the "python" call, the module
# will recognize it being called, and will execute "fibonacci(50)".

# When importing, python searches: the folder from which the script is run,
# the pythonpath and the installation-dependent path for modules such as "math"
# These paths are stored in the sys.path variable, which is a list.

# sys is a particular built-in module that is loaded by default by the
# interpreter. It contains system variables such as the ">>>" at the beginning
# of each interactive prompt and the sys.path variable seen before.
# It is important to note that these variables may be changed by the user.

# dir() can be used to return what names a module defines.

dir(sys)
dir(Fibo)
dir()  # By itself, returns what has been defines locally.

# Built-in functions (such as dir()), can be found in the module builtins, but
# only after it is imported.

# Leading dots can be used to call subpackages from a subpackage. See the tut.
