#CreatedBy: Mitchell Ciupak
#Created On: 20200612

import sys
from program import Program
from problem import Problem

def main():

    #init
    #TODO Integrate Pickle, then check if new user exists on startup
    Program().newUser()
    
    #create new problem
    newProb = Problem()



if __name__ == '__main__':
    main()

def checkArgs():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))