# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 18:33:00 2019

@author: 1354034
"""

#Python programming to draw pentagon in turtle programming
import turtle
import math

t = turtle.Turtle()
r=100
def f(n):
    angle=2*math.pi/n
    angle1=360/n
    l=2*r*math.sin(angle/2)
    t.right(angle1/2)
    for i in range(n):
       t.forward(l) #Assuming the side of a pentagon is 100 units
       t.right(angle1) #Turning the turtle by 72 degree
    t.left(angle1/2)

t.left(90)
t.forward(r)
t.right(90)
for n in range(3,50):
    f(n)
