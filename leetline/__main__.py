#CreatedBy: Mitchell Ciupak
#Created On: 20200612

import sys
import os
from program import Program, checkFlats, llhelp
from problem import Problem


def main():

    #init
    checkFlats()
    prog = Program()

    #check arguments
    args = sys.argv[1:]
    if not (args):
        llhelp()
    else:
        for arg in args:
            print('passed argument :: {}'.format(arg))


    

    # while(sys.argv[1:] != 'end'):
        #TODO Create Command
    
        #create new problem
        # newProb = Problem()

if __name__ == '__main__':
    main()