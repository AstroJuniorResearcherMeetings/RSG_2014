#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Load data and fit your own model to it. 
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

def model (params,xpts):
    """ This evaluates a function yfit = f(xpts) 
    
    Parameters
    ----------
    params : list of floats
    xpts : np.ndarray
        Numpy array where to evaluate points
    
    Returns
    -------
    yfit : np.ndarray
    
    """
    # TODO: put in best idea of a functional form for the data,
    # To figure this you you may first want to plot the data
    return 
    
def error_function (params,model_func,xpts,ypts):
    """ The error function gives a quantitative value for how bad/good the 
    parameters are. 
    
    Parameters
    ----------
    params : list of floats
    xpts : np.ndarray, shape=(N,)
    ypts : np.ndarray, shape=(N,)    
    
    Returns
    -------
    red_chi2 : float
        Reduced chi2 value
    
    """
    yfit = model_func(params,xpts)
    chi2 = np.sqrt(np.sum((ypts-yfit)**2))
    deg_freedom = (len(ypts)-2)
    return chi2/deg_freedom
    
def fit_model_to_data (xpts,ypts,params0,model_func=model):
    """ Produces the best m and b parameters from m*x+b 
    
    Parameters
    ----------
    xpts : np.ndarray, shape=(N,)
    ypts : np.ndarray, shape=(N,)    
    params0 : list of floats
        Initial parameters to pass to model_func
    model_func : callable function  
        yfit = model_func(params,xpts)  
    
    Returns
    -------
    params : (float,float)
        The best fit (m,b) values 
        
    """    
    # TODO: use scipy.optimize.fmin to find the minimum parameters using
    #       the error_function
    #       
    return params0

def plot_results (xpts,ypts,params,model_func=model):
    """ Creates a plot of showing the result
    
    Parameters
    ----------
    xpts : np.ndarray, shape=(N,)
    ypts : np.ndarray, shape=(N,)    
        
    """
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # TODO: add data to plot
    
    # TODO: add model to plot
    
    # TODO: show/save figure
    

pass 
# ########################################################################### #
if __name__ == "__main__":
    # get data    
    xpts,ypts = np.genfromtxt("../example_data/data_set1.txt",usecols=[0,1],unpack=True)

    # intial parameters for model
    params0 = [1,2,3]
    
    # Find minimum fit
    best_params = fit_model_to_data (xpts,ypts,params0,model_func=model)
    
    # visualize the results
    plot_results(xpts,ypts,best_params,model)

