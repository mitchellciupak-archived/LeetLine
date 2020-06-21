#CreatedBy: Mitchell Ciupak
#Created On: 20200621

import pickle
from program import Program

#Load Problem Objects into Dictionary and List
def getProbList():
    #TODO Pull one and add to dict for x in cars
    prog = Program()
    probs = []

    for x in prog.probCount:
        try:
            pickle_in = open("flats/program" + x.str() + ".pickle","rb")
        except: 
            print("Loading Problem " + x.str() + " has failed.")
        else:
            inprob = pickle.load(pickle_in)
            pickle_in.close 
            probs.append(inprob) 

       

