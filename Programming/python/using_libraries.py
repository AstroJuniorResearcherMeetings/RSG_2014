
# NAMESPACES
import this


# define names
name = 10

# =======================


# some names are pre-defined https://docs.python.org/2/library/functions.html

b = min(10,5)
b = bool("hello")

value = raw_input("type something : ")
print("you typed: {}".format(value))

# =======================

dir()
globals()

# what type is globals?

# =======================

# functions have a local name space
def func ():
    global new_name
    new_name = "defined locally "
    print(new_name)
    

new_name = "defined globally "





global new_name

# consequently func has been added to the name space

# =======================

# objects have a name space
my_list = range(5)

dir(my_list) 

# append isn't in global name space

# =======================

# library <=> package <=> modules

# libraries can be thought of as a collection of names

import numpy

import numpy as np
np = numpy

# spy my_module.py
# copy paste stuff from the other module

import my_module
from my_module import find_closest_index

# 


# ======================= PYTHONPATH

import sys
sys.path 

# put my_module in path

# now where-ever I am I can use it.
















# ########################################################################### #









name = "hello, world"
pi = 3.14159

def find_closet_index (pts1,pts2):
    """ Finds the index of the two values which are closest
    
    Parameters
    ----------
    pts1 : list of floats, len=N
    pts2 : list of floats, len=N
    
    Returns
    -------
    index1 : integer
        index of the closest point in pts1
    index2 : integer
        index of the closest point in pts2
    
    """
    index1,index2 = 0,0
    
    min_dist = 10000000000000
    for i in xrange(len(pts1)):
        for j in xrange(len(pts2)):
            dist = pts1[i]-pts2[j]
            if dist < min_dist:
                index1 = i
                index2 = j
                min_dist = dist        
    return index1,index2
    








