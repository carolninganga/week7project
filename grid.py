# Caroline Ninganga
# Spring 2021 
# CS 5001 
# Grid file for project 7


import turtle as t
import sys 
import lsystem as ls
import turtle_interpreter as ti

# draw two l-systems strings given an (x, y) anchor, scale and angle 
def pair( lstring, x, y, scale, angle ):
    previousheading = t.heading()

    t.up()
    t.goto(x, y ) 
    t.down()
    t.right(300)
    t.color( 0.7, 0.5, 0.9 )
    t.width( 4 )
    ti.drawString( lstring, scale*0.55, angle )