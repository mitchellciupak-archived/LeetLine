#CreatedBy: Mitchell Ciupak
#Created On: 20200612

import sys
import os
from program import Program, checkFlats, llhelp
from problem import Problem
from report import getProbList


def main():

    #init
    checkFlats()
    prog = Program()

    #check arguments
    args = sys.argv[1:]
    if not (args):
        llhelp()
    #Create New Problem Command
    elif (args[0] == 'n' or args[0] == 'new'):
        newProb = Problem(prog.newProblemID())
    #List all Problems
    elif (args[0] == 'ls' or args[0] == 'list'):
        getProbList()
    elif (args[0] == 'debug'):
        print(prog.getProbCount())
    else:
        print (args)

    

    # while(sys.argv[1:] != 'end'):
        #TODO Create Command
    
        #create new problem
        # newProb = Problem()

if __name__ == '__main__':
    main()