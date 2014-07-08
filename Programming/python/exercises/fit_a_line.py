#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Fit a line to data for which you know the solution
AUTHOR: dylangregersen
DATE: Tue Jul  1 09:30:51 2014
"""
# ########################################################################### #

# import modules 

from __future__ import print_function, division
import numpy as np # for arrays
import pylab as plt # for plotting
import scipy.optimize # for optimization

# ########################################################################### #

def linear_model (params,xpts):
    """ This evaluates a linear function m*x+b
    
    Parameters
    ----------
    params : (float,float)
        m,b = params
    xpts : np.ndarray
        Numpy array where to evaluate points
    
    Returns
    -------
    yfit : np.ndarray
    
    """
    m,b = params
    return m*xpts+b

def error_function (params,xpts,ypts):
    """ The error function gives a quantitative value for how bad/good the 
    parameters are. 
    
    Parameters
    ----------
    params : (float,float)
        m,b = params
    xpts : np.ndarray, shape=(N,)
        Numpy array where to evaluate points
    ypts : np.ndarray, shape=(N,)    
    
    Returns
    -------
    red_chi2 : float
        Reduced chi2 value
    
    """
    yfit = linear_model(params,xpts)
    chi2 = np.sqrt(np.sum((ypts-yfit)**2))
    deg_freedom = (len(ypts)-2)
    return chi2/deg_freedom
    
def linear_fit (xpts,ypts):
    """ Produces the best m and b parameters from m*x+b 
    
    Parameters
    ----------
    xpts : np.ndarray, shape=(N,)
    ypts : np.ndarray, shape=(N,)    
      
    Returns
    -------
    params : (float,float)
        The best fit (m,b) values 
        
    """
    # TODO: use scipy.optimize.fmin to find the minimum parameters using
    #       the error_function
            
    return (3,2)

def plot_results (xpts,ypts,best_params):
    """ Creates a plot of showing the result
    
    Parameters
    ----------
    xpts : np.ndarray, shape=(N,)
    ypts : np.ndarray, shape=(N,)    
        
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xpts,ypts,color='b',label="data")    
    
    yfit = linear_model(best_params,xpts)
    
    # TODO: add fits points to plot, one line similar to adding the data above
    
    ax.set_title("best fit params {}".format(best_params))

    # TODO: add legend to plot, look at plt.legend
    
    # TODO: save plot to file using `fig.savefig`    
    plt.show()

pass 
# ########################################################################### #

np.random.seed(42) # fixes all the random numbers

# correct parameters
m = 3.00
b = 2.15

# get data    
xpts = np.linspace(-10,10,1000)
ypts = linear_model((m,b),xpts)
ypts += np.random.normal(0,0.7,len(xpts))

# Find minimum fit
best_params = linear_fit(xpts,ypts)

# TODO: print to screen the best parameters and the correct parameters. How
# close are they?

# visualize the results
plot_results(xpts,ypts,best_params)
      
# CHALLENGES :
#  * Add a parameter to the function `linear_fit` which gives the starting
#    value for scipy.optimize.fmin
#  * add another subplot to the figure which shows the residuals (yfit-ypts)
#  * Change this from a linear fit to a 2nd degree polynomial fit params = (c0,c1,c2) 
#  * How would you incorporate erros in y points 
#    yerr = np.random.normal(0,0.7,len(ypts))



