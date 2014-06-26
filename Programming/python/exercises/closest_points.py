#!/usr/bin/env python

# PURPOSE: Create a function which finds the closest distance between two points
# AUTHOR: dylangregersen
# DATE: Thu Jun 26 12:39:01 2014

# ########################################################################### #

# import modules
import time
import random

# ########################################################################### #

# =======================  define a function for finding the closest points
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
    
    # TODO: implement a method to find the closest value
    
    return index1,index2
    
# ======================= create some fake data

# TODO: define variable num_pts as an integer

pts1 = []
pts2 = []
for i in range(num_pts):
    r = random.random()*num_pts
    pts1.append(r)    
    pts2.append(random.random()*num_pts)

# ======================= Use function to find the closest points
index1,index2 = find_closets_index(pts1,pts2)

# TODO : print out the result


# ======================= CHALLENGES : 
#    * Create a function which returns the value of the closest point in pts1
#    * Create a function to find the points furthest apart
#    * Create a function which returns the 5 (or #) closest numbers
#    * Change this code to use the library NumPy
