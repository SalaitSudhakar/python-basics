# my_module.py

def greeting():
    print("Hello")

if __name__ == "__main__" :
    print(__name__)  # __main__
    # when this file run as a main program, that means you run this file here,
    # above print(__name__) will print __main__

    # This block will only be executed if this file is run as a main program
    print("Running my_module.py as a main program")
    greeting()