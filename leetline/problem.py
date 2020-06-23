#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import sys
import pickle
from program import Program

## Problem IDs are 1 indexed
## TODO Need Categories like Trees or Something 

class Problem: 
    def __init__(self, id):
        self.id = id

    #Flatten Class
    def save(self):
        f = open("flats/prob" + str(self.id) + ".pickle","wb")
        pickle.dump(self.__dict__, f, 2)
        f.close()

    def __del__(self):
        self.save()

        #Unflatten Class
    def load(self):
        f = open("flats/prob" + str(self.id) + ".pickle","rb")
        tmp_dict = pickle.load(f)
        f.close()          
        self.__dict__.update(tmp_dict) 

    # Method creates the template to implament a new problem
    @classmethod
    def createNewProblem(cls, prog): 
        newcls = cls(prog.newProblemID())
        newcls.name = input("1. Please enter the problem name: ")
        newcls.source = input("2. Please enter a link or description of the source: ") 
        newcls.dateTimeCreated = prog.getDateTime()

        newcls.filename = ''.join(word.title() for word in newcls.name.split(' '))
        newcls.foldername = "C:/leetline" + "/" + newcls.filename + "/" + newcls.filename
        #TODO Debug
        #newcls.foldername = newcls.prog.getPrefDirectory() + "/" + newcls.filename + "/" + self.filename

        #Create Project File
        #if(newcls.prog.getPrefLanguage == 'Python'):
        #    fptr = open(newcls.filename + ".py","w+")
        #    fptr.write("Write in basic template with descripion and everything")
        #    fptr.close()
        return newcls

    # Method Loads class based on dict
    @classmethod
    def loadbyID(cls, id):
        newcls = cls(id)
        newcls.load()
        return newcls


# [Classmethods](https://iscinumpy.gitlab.io/post/factory-classmethods-in-python/)
# Class methods take the class as the first argument, traditionally newcls.
# Class methods that are factories call cls(), and return the new instance they created.
# Both __new__ and __init__ not ran