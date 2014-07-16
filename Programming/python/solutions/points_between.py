#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PURPOSE: Find the points between two boundaries
# AUTHOR: dylangregersen
# DATE: Fri Jun 27 08:34:45 2014

# ########################################################################### #

# import modules
from __future__ import print_function, division
import time 
import numpy as np

# ########################################################################### #

def between (array,lower_bound,upper_bound,inclusion="neither"):
    """ Returns list of indices where the array elements are between the bounds
    
    Parameters
    ----------
    array : ordered data structure of elements
    lower_bound : float
    upper_bound : float
    inclusion : string
        "both" : lower <= value <= upper
        "upper" : lower < value <= upper
        "lower" : lower <= value < upper
        "neither" (default) : lower < value < upper
    
    Returns
    -------
    indices : array of integers
    """
    # possibly convert array to numpy.ndarray
    array = np.asarray(array)
    
    if inclusion == "both":
        mask = (lower_bound <= array) & (array <= upper_bound)    
    elif inclusion == "upper":
        mask = (lower_bound <  array) & (array <= upper_bound)        
    elif inclusion == "lower":
        mask = (lower_bound <= array) & (array <  upper_bound)        
    else: # "neither"
        mask = (lower_bound <  array) & (array <  upper_bound)                    
    
    # NOTE: I could also return mask and then use it for the numpy array
    # array[mask]  would give me all the elements which are appropriate
    
    return np.where(mask)[0].reshape(-1).astype(int)

# ########################################################################### #

# -----------------------  create test data
array = np.array([1.1,3.0,5.3,2.2,5.3,8.4,7.1,10.1,2.0,0.1])
lower_bound = 4.1
upper_bound = 8.5

# =======================  find indices of points between

# implement in pure python
index_by_python = []
for i in xrange(len(array)):
    if lower_bound < array[i] and array[i] < upper_bound:
        index_by_python.append(i)
  
# create a function which uses NumPy to determine between
index_by_numpy = between(array,lower_bound,upper_bound)
  
solution = [2,4,5,6]      
print("Solution : {}".format(solution))
print("Python Only : {}".format(index_by_python))
print("With Numpy : {}".format(index_by_numpy))

# NOTE : you should thing about whether the bound should be 
#       inclusive (<=,>=) or exclusive (<,>). Perhaps add a variable which 
#      tells the program which to use.

# ======================= retrieve the values from the array which are between

# pure python version
values_by_python = []
for i in index_by_python:
    values_by_python.append(array[i])
# TODO: for fun try to put this into one line using list comprehensions

values_by_numpy = array[index_by_numpy]

solution = [ 5.3,  5.3,  8.4,  7.1]
print("Solution : {}".format(solution))
print("Python Only : {}".format(values_by_python))
print("With Numpy : {}".format(values_by_numpy))

# ======================= 

# CHALLENGES:
#  * make the code with finds the index points a function
#  * re-implement these using the numpy library
#     specifically look at np.where