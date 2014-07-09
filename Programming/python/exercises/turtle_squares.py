#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PURPOSE: Use the python package turtle to draw rectangles
AUTHOR: dylangregersen
DATE: Thu Jun 26 10:07:40 2014

To execute this file in Spyder, go to Run > Configure. In the configure window click "Execute in new dedicated Python interpreter". Then you can click the run button to execute the code

To execute this file on the command line, go the the directory with this file and type:
python turtle_squares.py

"""
# ########################################################################### #

# import modules 
from __future__ import print_function, division
import random
import time
try:
    import turtle
except ImportError as e:
    print(("Tried to import but failed. Need to check that the library `turtle` "
            "installed and working"))
    print(e)
    
# ########################################################################### #

# ======================= Methods for using turtle to draw
# These should be all you need

# move the cursor (turtle) without drawing
def move (t,x,y):
    """ Moves the turtle position without drawing
    
    Parameters
    ----------
    turtle : `turtle.Turtle`
    x : float
    y : float    
    
    """
    t.penup()
    t.goto(x,y)
    t.pendown()

# move the cursor while drawing
# t.goto(100,100)

# set color
# t.color("red")

# get color
# color = t.color()

# ======================= Functions


# ########################################################################### #


# ======================= create the turtle objects
t = turtle.Turtle()  

# ======================= define a list of colors  
colors = ["red","black","green","blue","purple","orange","brown","maroon"] 

# ======================= get the screen and modify properties
screen = t.screen
screen.bgcolor(0.9,0.9,0.9) # r,g,b
screen.title("Smile!")
# This accesses the hidden variable _root, inorder to make the screen appear infront of all others
screen._root.attributes("-topmost",True) 
size = screen.screensize()

# ======================= Create a rectangle

# TODO : implement functions and variables which a series of enclosing draw rectangles
    

    # draw a rectangle
    #   define a start x,y
    #   move the cursor (t) to that point, move(t,x,y)
    #   draw with the cursor to every corner. t.goto(x+?,y+?)
    
move(t,-250,-250)
t.write("Always look on the bright side of life!",move=True,font=('Arial',30))
    
# CHALLENGES:
#  * have the colors chosen randomly
#  * Manipulate the spacing of the rectangles
#  * Manipulate the width and height every time

turtle.done()
