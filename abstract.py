# Caroline Ninganga
# 03/22/2021
# Project 7

import sys #import sys
import lsystem as ls #import lsystem
import turtle as t #import turtle
import turtle_interpreter as ti #import turle_interpreter



def main():

    # read and draw lysytem using createLsytemFromFile()
    lsystem1 = ls.createLsystemFromFile( 'systemA5.txt' )
    lsystem2 = ls.createLsystemFromFile( 'systemA5.txt' )
    lsystem3 = ls.createLsystemFromFile( 'systemA5.txt' )

    #build the lysytem from a file using 4 iterations  
    lstring1 = ls.buildString( lsystem1, 4)
    lstring2 = ls.buildString( lsystem2, 4)
    lstring3 = ls.buildString( lsystem3, 4)


    distance = float( 20 ) #distiance to be given by user in the command line 
    angle = float( 90 ) #angle to be given by user in the command line

    # setup and turn off tracing from turtle 
    t.setup(900, 900)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(200, 100)
    t.down()
    t.color( 'green' )
    t.width(1) # added a width of 

    ti.drawString( lstring1, distance, angle ) # draws the 1st lsystem


    distance = float( 20  ) #distiance 
    angle = float( 90 ) #angle 

    # setup and turn off tracing from turtle 
    t.setup(900, 900)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(100, -100)
    t.down()
    t.color( 'red' )
    t.width(2) # added a width of 2

    ti.drawString( lstring2, distance, angle ) # draws the 2nd lsystem

    distance = float( 20  ) #distiance 
    angle = float( 90 ) #angle 

    # setup and turn off tracing from turtle 
    t.setup(900, 900)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(150, 100)
    t.down()
    t.color( 'orange' )
    t.width(3) # added a width of 3

    ti.drawString( lstring3, distance, angle ) # draws the 3rd lsystem


    #wait 
    ti.hold()

if __name__ == "__main__":
    main()
