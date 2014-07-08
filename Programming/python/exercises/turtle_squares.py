#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PURPOSE: Use the python package turtle to draw rectangles
# AUTHOR: dylangregersen
# DATE: Thu Jun 26 10:07:40 2014

# ########################################################################### #

# import modules 
from __future__ import print_function, division
import random
try:
    from turtle import Turtle
except ImportError as e:
    print(("Tried to import but failed. Need to check that the library `turtle` "
            "installed and working"))
    print(e)
    
# ########################################################################### #

# ======================= Methods for using turtle to draw
# These should be all you need

# move the cursor (turtle) without drawing
def move (turtle,x,y):
    """ Moves the turtle position without drawing
    
    Parameters
    ----------
    turtle : `turtle.Turtle`
    x : float
    y : float    
    
    """
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

# move the cursor while drawing
# turtle.goto(100,100)

# set color
# turtle.color("red")

# get color
# color = turtle.color()

# ======================= Functions


# ########################################################################### #


# ======================= create the turtle objects
turtle = Turtle()  

# ======================= define a list of colors  
colors = ["red","black","green","blue","purple","orange","brown","maroon"] 

# ======================= get the screen and modify properties
screen = turtle.screen
screen.bgcolor(0.9,0.9,0.9) # r,g,b
screen.title("Smile!")
size = screen.screensize()

# ======================= Create a rectangle

# TODO : implement functions and variables which a series of enclosing draw rectangles
    
    # draw a rectangle
    #   define a start x,y
    #   move the cursor (turtle) to that point, move(turtle,x,y)
    #   draw with the cursor to every corner. turtle.goto(x+?,y+?)
    
move(turtle,-250,-250)
turtle.write("Always Look on the bright side of life",move=True,font=('Arial',30))
    
# CHALLENGES:
#  * have the colors chosen randomly
#  * Manipulate the spacing of the rectangles
#  * Manipulate the width and height every time

