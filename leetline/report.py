#CreatedBy: Mitchell Ciupak
#Created On: 20200621

import os
import sys
# import numpy as np
# import matplotlib.pyplot as plt
import pickle
from program import Program

#Load Problem Objects into Dictionary and List
def getProbList():
    #TODO Pull one and add to dict for x in cars
    prog = Program()
    probs = []

    for x in prog.probCount:
        try:
            pickle_in = open("flats/program" + str(x) + ".pickle","rb")
        except: 
            print("Loading Problem " + str(x) + " has failed.")
        else:
            inprob = pickle.load(pickle_in)
            pickle_in.close 
            probs.append(inprob)

       
def getData():
    #TODO Adapt to other uses (Right now it is just for qucik sort)
    path = input("Please enter the full path of the output: ")
    with open(path) as f:
        lines = f.readlines()
    n_size = []
    cpu_ticks = []
    for line in lines:
        line = line.split()
        n_size.append(float(line[0]))
        cpu_ticks.append(float(line[1]))
    plt.xticks(np.arange(0, 1000000, step=200000))
    plt.yticks(np.arange(0, 500000, step=25000))
    plt.plot(n_size, cpu_ticks)
    plt.xlabel("Number of longs to sort (N)")
    plt.ylabel("CPU clock ticks required to sort array")
    plt.title("Size of Array vs Time to Sort")
    #plt.show()
    plt.savefig('plots/quick_sort_01.png')

