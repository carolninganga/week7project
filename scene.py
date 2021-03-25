# Caroline Ninganga
# Spring 2021 
# CS 5001 
# Grid file for project 7

# import the packages turtle, sys, lsystem and turtle_interpreter
import turtle as t
import sys 
import lsystem as ls
import turtle_interpreter as ti


# define a main function
def main():

    # read and draw lysytem using createLsytemFromFile()
    lsystem1 = ls.createLsystemFromFile( 'systemA3.txt' )
    lsystem2 = ls.createLsystemFromFile( 'systemA4.txt' )

    #build the lysytem from a file using 4 iterations  
    lstring1 = ls.buildString( lsystem1, 4)
    lstring2 = ls.buildString( lsystem2, 4)


    distance = float( 3 ) #distiance 
    angle = float( 90 ) #angle 

    # setup and turn off tracing from turtle 
    t.setup(900, 900)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(-200, 100)
    t.down()
    t.color( 'blue' ) # add color to the tree from (ABOP)
    t.width(1) # added a width of 

    ti.drawString( lstring1, distance, angle ) # draws the 1st lsystem


    distance = float( 3  ) #distiance 
    angle = float( 90 ) #angle 

    # setup and turn off tracing from turtle 
    t.setup(900, 900)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(100, -100)
    t.down()
    t.color( 'purple' )
    t.width(2) # added a width of 2

    ti.drawString( lstring2, distance, angle ) # draws the 2nd lsystem


    #wait 
    ti.hold()

if __name__ == "__main__":
    main()
