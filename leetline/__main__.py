import sys
#from .classmodule import MyClass
#from .funcmodule import my_function

## https://code.visualstudio.com/docs/python/python-tutorial
## https://trstringer.com/easy-and-nice-python-cli/

def main():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))

    #my_function('hello world')

    #my_object = MyClass('Thomas')
    #my_object.say_name()

if __name__ == '__main__':
    main()

    # & C:/Users/mjcre/AppData/Local/Programs/Python/Python38-32/python.exe c:/Users/mjcre/Documents/LeetLine/leetline/__main__.py test