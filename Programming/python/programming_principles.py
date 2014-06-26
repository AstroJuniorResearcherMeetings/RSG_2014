#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PURPOSE: Intro for Python using Principles of Programming
# AUTHOR: dylangregersen
# DATE: Wed Jun 25 22:29:43 2014




# ########################################################################### #


# General notes about this script. You can run it by opening the python interpreter and typing in (or copying each line)
# python
# >> variable = 1
# >> print(variable)

# you can also use the function "execfile" to execute the script
# python
# >> execfile("programming_principles.py")


# the basic elements for any programming language fall into the following
# categories:

# Variables
# Expressions
# Control Structures
# Data Structures

# Pay attention to the SYNTAX tags which note things about syntax

# ======================= Variables

# python variables are dynamically typed, so unlike c/c++ you don't need to declare the type of a variable. Notice in this example I'm just changing the value of the same variable name.

variable = 1 # integer
variable = 2.3 # float
variable = True # boolean
variable = "Hello" # string
variable = 'world' # string
variable = """ how are you """ # string

# SYNTAX: Note that unlike c/c++ you don't need ';' at the end of each line

# in the interpreter you can check out the value of a variable just by typing it
variable
# or by using the print function
print(variable)

# ======================= Expressions

result = 1+1 # addition
result = 2-1 # subtraction
result = 4*2 # multiplication
result = 4/2 # division, note 5/2 != 5.0/2.0
result = 2**3 # powers

result += 2 # add in place to result
result *= 1.5 # multiply in place
# also /= -= &= 

# bitwise operations also supported, < << | so on

# Because python is dynamically typed, expressions are flexible with type
result = "blah "*10
print('result of "blah "*10 is {}'.format(result))

# ======================= Control Structures

# ----------- Control Structures : Conditionals 
# check the state of a value
variable = 10.5
v2 = "hello"
v3 = 4
result = variable > 10 # True
result = variable <= 9 # False
result = (variable < 10) | (v2 == "hello") # True
result = (variable < 10) & (v2 == "hello") # False
result = ~(variable < 10) & (v2 == "hello") # True, 1
result = v3 != 3 # True

# Conditionals can be put into if statements
if v2 == "hello":
    print("this is True")
    
# SYNTAX: Python works on indentation blocks. Here, for example, the if statement starts with the statement `if <conditional>:`, everything to execute if true is indented by 4 spaces. Then end of the if statement is given by returning to the original indentation. 
variable = "hello"

if variable == "world":
    print("I thought you == 'hello'")
elif variable == "star": # check another conditional
    print("No, really, I thought you == 'hello'")
elif variable == "hello":
    print("that's correct!")
# ... add more elif
else:
    print("variable didn't equal anything I checked for")



# ----------- Control Structures : Loops

# need to create something to loop over, more on this object in Data Structures
names = ["Tim","Jon","Jack","Brian"]
for name in names:
    if (name == "Tim"):
        print("I found Tim!")

# SYNTAX: Notice again the indentation blocks which specify the loop code and the if statement code.


# here is a while loop doing a similar action. Note: the function `len` returns the length of an iterable (e.g. len(names) => 4)
i = 0
while (i < len(names)):
    print("name = {}".format(names[i]))
    i += 1


# ======================= Data Structures

# The basic data structures in python are lists and dictionaries

# ----------- Lists
# ordered structure of elements
my_list = [0,1,2,3] # creates a list
my_list = [] # empty list
my_list = list((1.3,2.3,4.5)) # using the list function
my_list = [3.0,2,"hello",['another','list',True]] # lists don't care what types are in them

my_list[0] # access the 0-th element (aka the first)
print(my_list[3])
print(my_list[-1]) # can index backwards, -1 is the last element 

for element in my_list:
    print(element)
    
# lists are python objects and have methods. 

# add element to the end
my_list.append("new_element")
print(my_list)

# remove an element by it's value
my_list.remove(3.0)
    
# remove an element by index
my_list.pop(1)
    
# check if element is in list
if "hello" in my_list:
    print("hello to you too!")

# ----------- Dictionaries/Hashmap
# map keys to values
my_dict = {} # empty
my_dict = {'key1':'value1','key2':2.3,'hello':'world'} # declare with values
my_dict = dict(key1="value1",key2=2.3,hello="world") # use dict function

# add new elements
my_dict[2] = 4
my_dict["new_key"] = ["yes","a","new","key"]

# access elements by the key
my_dict['key1'] # -> "value1"
my_dict['hello'] # -> 'world'
my_dict[2] # -> 4

# check out all the keys as a list
my_dict.keys()

# check out all the values as a list
my_dict.values()

# check if dictionary has key
if "hello" in my_dict:
    print("has this key!")


# ----------- Tuples
# like lists, only you can't change the values after you set them
my_tuple = (1,"hello",4.5)
# explore more if you feel like by using the internet

# ----------- Sets
# like mathematical sets. Have only unique values and you can do operations like finding the intersection
my_set1 = {2,3,4}
my_set2 = {4,6,5}
my_set1.intersection(myset2)

# explore more if you feel like by using the internet

# ----------- Arrays
# VERY useful in science. Arrays have a single type and have fast operations.

import numpy as np # using this library
my_array = np.array([1,2,3])
my_array[0] # -> 1
my_array *= 3
print(my_array)

# ########################################################################### #

# FUNCTIONS

# The basic declaration of functions, or blocks of code to reuse

def my_function ():
    print("hello")
my_function()
    
def my_function (name):
    print("hello {}".format(name))
my_function("Dylan")

def my_function (name,age=25):
    print("hello {}, age {}".format(name,age))
    return age # returns the value age
age = my_function("Dylan")    
age = my_function("Dylan",age=10)    

def other_function (func,arg1):
    # you can pass functions as any other argument
    return func(arg1) # the result of arg1

age = other_function(my_function,"Tom")

# Advanced:

def my_function (*args):
    # args is a list 
    for element in args:
        print(element)
    return arg[0],arg[1] # return the first two arguments
arg1,arg2 = my_function("hello","my","name","is","al") #splits up the return into two variables

def my_function (**kwargs):
    # kwargs is a dict
    for key in kwargs.keys():
        print("{} = {} ".format(key,kwargs[key]))
        
my_function("hello","my","name","is","al")

# ########################################################################### #

# Libraries/packages/modules

import os
pwd = os.path.abspath(".")
print(pwd)

import sys
for path in sys.path:
    print("look here: {}".format(path))

# ########################################################################### #
# you can get help on any object
help(range)





    

