#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Using matplotlib to look at data files
AUTHOR: Dylan Gregersen
DATE: Mon Jul 14 21:33:13 2014
"""
# ########################################################################### #

# import modules 

from __future__ import print_function, division
import os
import numpy as np 
import matplotlib.pylab as plt

# ########################################################################### #

# specify the directory for the data
data_dir = "example_data"

# specify the file you want to plot
filepath = os.path.join(data_dir,"Sun.dat")

# read the data in using numpy
data = np.genfromtxt(filepath,unpack=True)

# ======================= 
# make basic plot of the data
fig = plt.figure()

ax = plt.subplot(1,1,1)

ax.scatter(data[0],data[1])

plt.show()

# ======================= 
# make basic plot of the data
fig = plt.figure()

ax = plt.subplot(1,1,1)

ax.plot(data[0],data[1])

ax.set_xlim(500,25000)

plt.show()

# ======================= 
# change the color of the plot
fig = plt.figure()

ax = plt.subplot(1,1,1)

ax.plot(data[0],data[1],color='r',linewidth=0.5,marker='*')

ax.set_xlim(500,25000)

plt.show()

# ======================= 
# Creating masks of the data
mask = (data[0] < 5000)

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.plot(data[0],data[1],color='k')
ax.plot(data[0][mask],data[1][mask],color='b',marker='*')
ax.set_xlim(500,25000)
plt.show()

# ======================= 
mask = (data[0] > 5000) & (data[0] <= 25000)
fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.plot(data[0][mask],data[1][mask],color='k')
plt.show()

# ======================= 
mask = (data[0] > 5000) & (data[0] <= 25000)

coefficients = np.polyfit(data[0][mask],data[1][mask],3)
yfit = np.polyval(coefficients,data[0][mask])

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.plot(data[0][mask],data[1][mask],color='k')
ax.plot(data[0][mask],yfit,color='r')
plt.show()

# ======================= 
mask = (data[0] > 5000) & (data[0] <= 25000)

coefficients = np.polyfit(data[0][mask],data[1][mask],3)
yfit = np.polyval(coefficients,data[0][mask])

def plot_fit_result (xpts,ypts,yfit):
    fig = plt.figure()
    ax = plt.subplot(1,1,1)
    ax.plot(xpts,ypts,color='k',label="data")
    ax.plot(xpts,yfit,color='r',label="fit")
    plt.legend()

plot_fit_result(data[0][mask],data[1][mask],yfit)
plt.show()


# ======================= 
mask = (data[0] > 5000) & (data[0] <= 25000)

coefficients = np.polyfit(data[0][mask],data[1][mask],3)
yfit = np.polyval(coefficients,data[0][mask])

def plot_fit_result (xpts,ypts,yfit):
    fig = plt.figure()
    # create top plot with the data
    ax = plt.subplot(2,1,1)
    ax.plot(xpts,ypts,color='k',label="data")
    ax.plot(xpts,yfit,color='r',label="fit")
    ax.set_ylabel("flux")
    plt.legend()
    
    # create bottom plot with the residuals
    ax = plt.subplot(2,1,2,sharex=ax)
    ax.plot(xpts,ypts-yfit,color='k')
    ax.axhline(0,color='r')
    ax.set_xlabel("wavelength")
    ax.set_ylabel("residuals")
    
    return ax
    
plot_fit_result(data[0][mask],data[1][mask],yfit)
plt.show()


# ======================= 
mask = (data[0] > 5000) & (data[0] <= 25000)

coefficients = np.polyfit(data[0][mask],data[1][mask],3)
yfit = np.polyval(coefficients,data[0][mask])

diff = data[1][mask] - yfit

plt.figure()
plt.hist(diff,bins=30)
plt.show()


# ======================= 
def blackbody (xpts,temp,norm=True):
    """ 
    Parameters
    xpts : np.ndarray
        In Angstroms 
    temp : float
        Temperature in Kelvin
    
    """
    # constants    
    h = 6.62606957e-34 # J*s
    c = 299792458.0 # m/s
    kb = 1.3806488e-23 # J/K
    
    # convert angstroms to meters
    xpts_meters = xpts*1e-10
    
    # Plank Equation
    A = 2.0*h*c**2/((xpts_meters)**5)
    B = np.exp(h*c/(xpts_meters*kb*temp))-1
    yfit = A/B

    if norm:
        # normalize by the maximum intensity
        ymax = 4.09567e-6*temp**5
        yfit /= ymax
        
    return yfit

xpts = np.arange(1,10000) # in Angstroms
ypts = blackbody(xpts,9000) # blackbody

fig = plt.figure()
ax = plt.subplot(1,1,1)
ax.plot(xpts,ypts)
plt.show()

# ======================= 
xpts = np.arange(1,40000) # in Angstroms

temps = [3000,4000,5000,6000]

fig = plt.figure()
ax = plt.subplot(1,1,1)
for t in temps:
    ypts = blackbody(xpts,t,norm=False) # blackbody
    ax.plot(xpts,ypts,label=str(t))
    
plt.legend()    
plt.show()



# ======================= 
mask = (500 < data[0] ) & (data[0] <= 35000)
xpts = data[0][mask]
ypts = data[1][mask]

temp = 6000
yfit = blackbody(temp,xpts)

ax = plot_fit_result(xpts,ypts,yfit)
ax = plt.subplot(2,1,1)
ax.set_title("temperature = {}".format(temp))
ax.set_xlim(500,25000)
plt.show()


# ======================= 
def chi2_difference (params,xpts,ypts):
    temp = params[0]
    yfit = blackbody(temp,xpts)
    return ypts-yfit

mask = (500 < data[0]) & (data[0] <= 20000.0)
xpts = data[0][mask]
ypts = data[1][mask]

import scipy.optimize
params = scipy.optimize.leastsq(chi2_difference,[6000],args=(xpts,ypts))
temp = params[0]
yfit = blackbody(temp,xpts)

ax = plot_fit_result(xpts,ypts,yfit)
ax = plt.subplot(2,1,1)
ax.set_title("temperature = {}".format(temp))
ax.set_xlim(500,25000)
plt.show()





