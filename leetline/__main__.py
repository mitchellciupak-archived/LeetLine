#CreatedBy: Mitchell Ciupak
#Created On: 20200612

import sys
import os
from program import Program
from problem import Problem

def checkFlats():
    #Check for the existance of pickles
    path = 'flats/' 
    if not os.path.exists(path):
        os.makedirs(path)

def main():

    #init
    checkFlats()
    prog = Program()
    
    #create new problem
    #newProb = Problem()



if __name__ == '__main__':
    main()


def checkArgs():
    print('in main')
    args = sys.argv[1:]
    print('count of args :: {}'.format(len(args)))
    for arg in args:
        print('passed argument :: {}'.format(arg))