#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import sys
from program import Program

## TODO Need Categories like Trees or Something 

class Problem: 

    def __init__(self):
        self.name = input("1. Please enter the problem name: ")
        self.source = input("2. Please enter a link or description of the source: ") 
        self.dateTimeCreated = Program.getDateTime()
        self.createNewProblem()

    def __del__(self):
        #Trigger Deconstructor by: del obj
        #Pickle it! 
        print("Self Destructing .....")

    # Method creates the template to implament and slove a problem
    def createNewProblem(self): 
        self.foldername = Program.getPrefDirectory + "/" + self.name
        self.filename = self.foldername + ''.join(word.title() for word in self.name.split(' '))

        #Create Project File
        if(Program.getPrefLanguage == 'Python'):
            fptr = open(self.filename + ".py","w+")
            f.write("Write in basic template with descripion and everything")
            fptr.close()