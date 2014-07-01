#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PURPOSE: Use the python package turtle to draw rectangles
# AUTHOR: dylangregersen
# DATE: Thu Jun 26 10:07:40 2014

# ########################################################################### #

# import modules 
from __future__ import print_function, division
import random
from turtle import Turtle

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
if __name__ == "__main__":
    # create the turtle object
    turtle = Turtle()  
    
    # define a list of colors  
    colors = ["red","black","green","blue","purple","orange","brown","maroon"] 
    
    # get the screen and modify properties
    screen = turtle.screen
    screen.bgcolor(0.9,0.9,0.9) # r,g,b
    screen.title("Smile!")
    size = screen.screensize()
    
    # TODO : implement functions and variables which a series of enclosing draw rectangles
        
    # draw a rectangle
    #   define a start x,y
    #   move the cursor (turtle) to that point
    #   move the cursor to every corner of the rectangle in turn
    
    # for every x starting point
    #    decide every y starting point
    #    pick a color
    #    draw a rectangle starting there
    #
    
    move(turtle,-250,-250)
    turtle.write("Always Look on the bright side of life",,move=True,font=('Arial',30))
    
# CHALLENGES:
#  * have the colors chosen randomly
#  * Manipulate the spacing of the rectangles
#  * Manipulate the width and height every time

