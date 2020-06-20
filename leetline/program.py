#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import platform
import sys
import pickle

#TODO Need the falttening to act as constants when instatiating this class multiple times

# This class holds all important system information and user data
class Program: 
    def __init__(self): 
        # Check for New User / Previously Instantiated Class
        try:
            pickle_in = open("flats/program.pickle","rb")
        except: 
            print("Program Pickel Failed (User Data Currupted)")
        else:
            self = pickle.load(pickle_in)
            pickle_in.close
            print(self.test)

    def __del__(self):
        self.test = "test1"
        #TODO Set Some Values to null before pickiling
        #Pickle it!
        pickle_out = open("flats/program.pickle","wb")
        pickle.dump(self,pickle_out)
        pickle_out.close()
        print("Self Destructing Program .....")

    # Pull Operating System ("Windows,"Linux","Darwin")
    def getOS(self):
        self.os = platform.system()
        return self.os

    # Pull Current DateTime (yyyyMMdd_hhmmssss)
    def getDateTime(self): 
        #TODO Have not decided best format yet
        print ("Date Time Under Construction")
        self.dateTime = "17760704_00000000"
        return self.dateTime

    # Prompts user to update directory information
    def getPrefDirectory(self):
        self.dir = input("Please enter your folder path: ") 
        while not (os.path.isdir(self.dir)):
            print("This folder was not found. Please Create and Try Again")
            self.dir = input("Please enter your folder path: ") 
        return self.dir

    def getPrefEditor(self):
        self.editor = "VS Code"
        #TODO Havent Decided best way to open the developmet environemnt
        print ("GetPrefEditor is Under Construction")
        return self.editor

    def getPrefLanguage(self):
        self.lang = input("Please enter your programming language: ") 
        while not(self.lang == "Python" or self.lang == "C/C++"):
            print("I'm sorry, we are currently only supporting 'Python' or 'C/C++.'")
            self.lang = input("Please enter your programming language: ") 
        return self.lang

    def getPrefName(self):
        self.author = input("Please enter your name/alias: ")
        return self.author

    def newUser(self):
        name = self.getPrefName()
        lang = self.getPrefLanguage()
        folder = self.getPrefDirectory()
        editor = self.getPrefEditor()

        print("Please review the following settings:")
        print("Your name is " + name + ", who speaks in the toung of " + lang + ", in the land of " + folder + " and you use " + editor + " as your wepon of choice against evil!\n")
        confirmation = input("Press enter to continue or type 'I have a small penis' to change your settings: ")
        if(confirmation != ''):
            self.newUser()
        #TODO Production
        #print("Great! Remember you can chage your settings anytime by using the command 'leetline.exe changeUser'")
