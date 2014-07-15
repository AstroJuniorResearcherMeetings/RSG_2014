#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Reading and plotting simple ascii data 
AUTHOR: dylangregersen
DATE: Tue Jul  8 13:59:37 2014
"""
# ########################################################################### #

# import modules

from __future__ import print_function, division
import numpy as np
import matplotlib.pylab as plt

# ########################################################################### #

def read_data_set1 (filepath):
    """ This reads in the data from data set 1
    
    With some simple modifications it could become a more general file reader
     
    Parameters
    ----------
    filepath : string
    
    """
    if not os.path.isfile(filepath):
        raise ValueError("file does not exist")

    # open the file
    f = open(filepath,'r')
    # read the lines
    lines = f.readlines()
    # close the file
    f.close()
    
    # get the data
    xpts = []
    ypts = []
    
    for line in lines:
        line = line.rstrip() # remove the return character
        
        # ignore blank lines
        if len(line) == 0: 
            continue
        
        # split on white space
        columns = line.split() 
        x = columns[0]
        y = columns[1]
        
        # store the data
        xpts.append(float(x))
        ypts.append(float(y))
    
    # convert from lists to arrays
    xpts = np.array(xpts)
    ypts = np.array(ypts)

    return xpts,ypts

# ########################################################################### #

# ======================= get data    
xpts,ypts = np.genfromtxt("../example_data/data_set1.txt",usecols=[0,1],unpack=True)

# TODO: use the read function to read in the data instead of genfromtxt

# ======================= create a mask for the data

mask = (xpts > 0)

# TODO: what is mask? take a look. Do you understand?

# TODO: create a mask for all the points greater than 5 and less than -5

# ======================= Plot the result

# create the figure
fig = plt.figure()

# create an axis on the figure
ax = plt.subplot(1,1,1)

# add all the data to the plot in blue
ax.scatter(xpts,ypts,c='b')

# add the masked data in red
ax.scatter(xpts[mask],ypts[mask],c='r') 

# TODO: look at the help for ax.scatter, how would you add a label

ax.set_xlabel("Time")

# TODO: add ylabel which says "Flux"

# add legend, if you have labels on your data points
# plt.legend()

# TODO: add a horizontal line where 0 is

# show the plot
plt.show()

# TODO: with the plot open try zooming and panning

# TODO: check out http://matplotlib.org/gallery.html, look at the plots and their
#   source code and try out one or two tricks you find there

# ======================= Challenges
# *  change the mask to be mask all data points for -5 < xpts < 5
# *  From points_between.py import your between function. Use that to create 
#    indicies and use them like the mask. 
#    import points_between
#    mask = points_between.between(xpts,-5,5)
#







