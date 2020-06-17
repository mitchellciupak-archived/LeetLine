#CreatedBy: Mitchell Ciupak
#Created On: 20200616

# Import
import os
import platform
import sys

class Program: 

    def __del__(self):
        #Trigger Deconstructor by: del obj
        #TODO Set Some Values to null before pickiling
        #Pickle it!
        print("Self Destructing .....")

    #
    def getOS:
        print("Under Construction")
        return 0

    # Method creates the template to implament and slove a problem
    def getDateTime(self): 
        return creation_date(path_to_file)


    def getPrefName:
        print("Under Construction")
        return 0

    def getPrefDirectory:
        print("Under Construction")
        return 0

    def getPrefLanguage:
        print("Under Construction")
        return 0

    def getPrefEditor:
        print("Under Construction")
        return 0


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime

    
#TODO Debug
obj = Problem()
del obj