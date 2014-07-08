#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Create a function which finds the closest distance between two points
AUTHOR: dylangregersen
DATE: Tue Jul  8 13:51:49 MDT 2014


To execute this script:
* Method 1 : from command line

    python closest_points.py

* Method 2 : 
    
    python
    
    >>> execfile("closest_points.py")
    
"""
# ########################################################################### #

# import modules
from __future__ import print_function, division

# ########################################################################### #

# =======================  define a function for finding the closest points
def find_closest_distance (pts1,pts2):
    """ Finds the index of the two values which are closest
    
    Parameters
    ----------
    pts1 : list of floats, len=N
    pts2 : list of floats, len=N
    
    Returns
    -------
    min_dist : float
        minimum distance between points in pts1 and pts2
    
    """
    
    # TODO: (3) Take the todo (1) and paste it here to use as a function
    # and return the minimum distance
    return 
    
# ======================= create some fake data
pts1 = [10.0, 11.0, 13.1, 5.0, 1.1, -10.2]
pts2 = [30.0,  5.1, 20.3, 3.2, -1.2]

# ======================= Find minimum distance

dist = pts1[0] - pts2[0]

# TODO: (1) implement a method which calculates the distance bewteen every pair
# of points between pts1 and pts2 and finds the minimum

# ======================= Display the result

# TODO : (2) print out the result

# ======================= CHALLENGES : 
#    * Create a function which returns the distance between two points in arrays lists
#    * Re-write so that it returns the furthest distance between the two arrays

# ======================= UBER-CHALLENGES : 
#    * Create the function so that it returns the index of both pts1 and pts2 
#      where the points are the closest
#    * Create a function which returns the 5 (or #) closest numbers
