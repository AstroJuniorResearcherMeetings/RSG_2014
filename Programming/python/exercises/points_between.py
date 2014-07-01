#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PURPOSE: Find the points between two boundaries
# AUTHOR: dylangregersen
# DATE: Fri Jun 27 08:34:45 2014

# ########################################################################### #

# import modules
from __future__ import print_function, division
import time 

# ########################################################################### #

def between (array,lower_bound,upper_bound):
    """ Returns list of indices where the array elements are between the bounds
    
    Parameters
    ----------
    array : ordered data structure of elements
    lower_bound : float
    upper_bound : float
    
    Returns
    -------
    indices : array of integers
    """
    # TODO: implement
    
    # TODO: optional, add parameter which lets you decide if a the upper/lower 
    # bound should be inclusive (<=,>=) or exclusive (<,>)
    return 
    
def test_between_function ():
    """
    
    
    """
    # create test data
    array = [1,3,5,2,5,8,7,10,2,0]
    lower_bound = 4
    upper_bound = 8

    # figure out solution
    solution = [2,4,5,6]
    
    # run function to get the function's solution
    answer = between(array,lower_bound,upper_bound)
    
    if solution != answer:
        msg = "Did not recieve correct answer\n"
        msg += "answer={}  solution={}".format(answer,solution)
        raise Exception(msg)

# ########################################################################### #
if __name__ == "__main__":
    # This is called unit testing. A USEFUL paradigm in programming anything is
    # to write a function which tests the outputs of the function you want given
    # a set of specific parameters. Then when you write the code, you simply run
    # the test and you know you've done it correctly
    test_between_function()

# CHALLENGES:
#  * reimplement this function but try using numpy
#  * Try to make this as fast as possible. time.time() returns time in
#    seconds. 


