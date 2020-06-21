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
    else:
        print (args)

    #Create New Problem Command
    if (args[0] == 'n' or args[0] == 'new'):
        newProb = Problem()
        newProb.createNewProblem()
    #List all Problems
    if (args[0] == 'ls' or args[0] == 'list'):
        getProbList()

    

    # while(sys.argv[1:] != 'end'):
        #TODO Create Command
    
        #create new problem
        # newProb = Problem()

if __name__ == '__main__':
    main()