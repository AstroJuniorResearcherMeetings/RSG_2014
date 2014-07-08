#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE:  the points between two boundaries
AUTHOR: dylangregersen
DATE: Tue Jul  8 13:51:49 MDT 2014


To execute this script:
* Method 1 : from command line

    python closest_points.py

* Method 2 : 
    
    python
    
    >>> execfile("closest_points.py")
    
"""
# PURPOSE: 
# AUTHOR: dylangregersen
# DATE: Fri Jun 27 08:34:45 2014

# ########################################################################### #

# import modules
from __future__ import print_function, division

# import numpy as np

# ########################################################################### #

# -----------------------  create test data
array = [1.1,3.0,5.3,2.2,5.3,8.4,7.1,10.1,2.0,0.1]
lower_bound = 4.1
upper_bound = 8.5

# =======================  find indices of points between

# TODO 1 : write code which checkes array and returns a list of index points where
# the array values are between the lower_bound and upper_bound

# NOTE : you should thing about whether the bound should be 
#       inclusive (<=,>=) or exclusive (<,>). Perhaps add a variable which 
#      tells the program which to use.

solution = [2,4,5,6]

# ======================= retrieve the values from the array which are between

# TODO 2 : write code which retrieves all the elements in `array` which have 
# the given indicies

solution = [ 5.3,  5.3,  8.4,  7.1]

# ======================= 

# CHALLENGES:
#  * make the code with finds the index points a function
#  * re-implement these using the numpy library
#     specifically look at np.where


