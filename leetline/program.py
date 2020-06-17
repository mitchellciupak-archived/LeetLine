#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import platform
import sys

# This class holds all important system information and user data
class Program: 

    def __del__(self):
        #Trigger Deconstructor by: del obj
        #TODO Set Some Values to null before pickiling
        #Pickle it!
        print("Self Destructing .....")

    # Pull Operating System ("Windows,"Linux","Darwin")
    def getOS(self):
        self.os = platform.system()
        return self.os

    # Pull Current DateTime (yyyyMMdd_hhmmssss)
    def getDateTime(self): 
        print ("Under Construction")
        return "17760704_00000000"

    def getPrefDirectory(self):
        try:
            os.path.isdir(self.dir)
            return self.dir
        except:
            self.dir = input("Please enter your folder path: ") 
            while not (os.path.isdir(self.dir)M):
                print("This folder was not found. Please Create and Try Again")
                self.dir = input("Please enter your folder path: ") 
            return self.dir

    def getPrefEditor(self):
        print("Under Construction")
        return "notepad++"

    def getPrefLanguage(self):
        try:
            return self.lang
        except:
            self.lang = input("Please enter your programming language: ") 
            while(self.lang != "Python" | self.lang != "C/C++"):
                print("I'm sorry, we are currently only supporting 'Python' or 'C/C++.'")
                self.dir = input("Please enter your programming language: ") 
            return self.dir

    def getPrefName(self):
        try:
            return self.author
        except:
            self.author = input("Please enter your name/alias: ")
            return self.author

    def newUser(self):
        name = self.getPrefName()
        lang = self.getPrefLanguage()
        folder = self.getPrefDirectory()
        editor = self.getPrefEditor()

        print("Please review the following settings:")
        print("Your name is " + name + ", who speaks in the toung of" + lang + ", in the land of" + folder + " and you use " + editor + "as your wepon of chooice against evil!")
        #TODO Give Option to change things 
        #TODO Format by making variables bold or something

obj = Program()
obj.newUser()