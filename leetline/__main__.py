import sys
import creation_date from datetime.py
#from .classmodule import MyClass

## https://code.visualstudio.com/docs/python/python-tutorial
## https://trstringer.com/easy-and-nice-python-cli/

class ll: 
    # default constructor 
    def __init__(self): 
        self.datetime = creation_date()
        self.name = "Problem"
  
    # a method for printing data members 
    def print_Geek(self): 
        print(self.name) 
  

def my_function(text_to_display):
    print('text from my_function :: {}'.format(text_to_display))

def main():

    #init
    obj = ll()

    #Debug
    #print('in main')
    #args = sys.argv[1:]
    #print('count of args :: {}'.format(len(args)))
    #for arg in args:
    #    print('passed argument :: {}'.format(arg))


    my_function('hello world')

    #my_object = MyClass('Thomas')
    #my_object.say_name()

if __name__ == '__main__':
    main()

    # & C:/Users/mjcre/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/mjcre/Documents/LeetLine/leetline/__main__.py test