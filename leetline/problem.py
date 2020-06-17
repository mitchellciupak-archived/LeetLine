#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import sys
#import Program

class Problem: 

    def __init__(self):
        self.getName()
        self.source = input("Please enter a link or description of the source: ") 
        #self.dateTimeCreated = Program.getDateTime()
        self.createNewProblem()

    def __del__(self):
        #Trigger Deconstructor by: del obj
        #Pickle it! 
        print("Self Destructing .....")
  
    # Method Gets Name By Input and Creates File Names
    def getName(self):
        self.name = input("Please enter the problem name: ")
        self.filename = ''.join(word.title() for word in self.name.split(' '))
        print(self.filename)


    # Method creates the template to implament and slove a problem
    def createNewProblem(self): 
        print(self.name) 

    


print("test")
obj = Problem()
del obj