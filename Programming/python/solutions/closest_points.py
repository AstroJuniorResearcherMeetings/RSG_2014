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
    min_dist = float('inf')
    for p1 in pts1:
        for p2 in pts2:
            dist = abs(p1-p2)
            if dist < min_dist:
                min_dist = dist        
    return min_dist

def find_furthest_distance (pts1,pts2):
    """ Finds the index of the two values which are furthest
    
    Parameters
    ----------
    pts1 : list of floats, len=N
    pts2 : list of floats, len=N
    
    Returns
    -------
    min_dist : float
        minimum distance between points in pts1 and pts2
    
    """
    distances = []
    for i in xrange(len(pts1)):
        for j in xrange(len(pts2)):
            distances.append(abs(pts1[i]-pts2[j]))
    return max(distances)
    
def find_closest_index (pts1,pts2):
    """ Finds the index of the two values which are closest
    
    Parameters
    ----------
    pts1 : list of floats, len=N
    pts2 : list of floats, len=N
    
    Returns
    -------
    index1 : int
    index2 : int
    
    """
    index1,index2 = 0,0
    min_dist = float('inf')
    for i in xrange(len(pts1)):
        for j in xrange(len(pts2)):                
            dist = abs(pts1[i]-pts2[j])
            if dist < min_dist:
                min_dist = dist
                index1 = i
                index2 = j                    
    return index1, index2
    
# ======================= create some fake data
pts1 = [10.0, 11.0, 13.1, 5.0, 1.1, -10.2]
pts2 = [30.0,  5.1, 20.3, 3.2, -1.2]

# ======================= Find minimum distance

min_dist = find_closest_distance(pts1,pts2)
max_dist = find_furthest_distance(pts1,pts2)
index1,index2 = find_closest_index(pts1,pts2)


# ======================= Display the result

print("the maximum distance is {}".format(max_dist))
print("the minimum distance is {}".format(min_dist))
dist = abs(pts1[index1]-pts2[index2])
print("minimum distance is abs(pts1[{}] - pts2[{}]) = {}".format(index1,index2,dist))

# ======================= CHALLENGES : 
#    * Create a function which returns the distance between two points in arrays lists
#    * Re-write so that it returns the furthest distance between the two arrays

# ======================= UBER-CHALLENGES : 
#    * Create the function so that it returns the index of both pts1 and pts2 
#      where the points are the closest
#    * Create a function which returns the 5 (or #) closest numbers

def closest_points (pts1,pts2,num=5):
    """ return the first `num` closest points"""
    # calc all the distances like in find_furthest_points
    distances = []
    for i in xrange(len(pts1)):
        for j in xrange(len(pts2)):
            distances.append(abs(pts1[i]-pts2[j]))
    
    # sort from min to max
    distances = sorted(distances)
    
    # get the number of points you want, can't be more than the number of distances
    num = int(min(num,len(distances)))
    close = []
    for i in range(num):
        close.append(distances[i])
        
    # TODO: check out list comprehensions
    #  e.g. close = [distances[i] for i in range(num)]
    
    return close


