# Caroline Ninganga
# 03/22/2021
# Project 7

import sys #import sys
import lsystem as ls #import lsystem
import turtle as t
import turtle_interpreter as ti #import turle_interpreter



def main( argv ):

    # check if there are enough arguement s
    # if len ( argv ) < 4:
    #     print( "usage: %s < lsystem filename> < distance> < angle>" % ( argv[0]))
    #     exit()

    #create the lsystem from a file
    # draw lysytem using createLsytemFromFile()
    lsystem1 = ls.createLsystemFromFile( 'systemA3.txt' )
    lsystem2 = ls.createLsystemFromFile( 'systemA4.txt' )


    #build the lysytem from a file using 4 iterations  
    lstring = ls.buildString( lsystem1, 4)

    distance = float( 20 ) #distiance to be given by user in the command line 
    angle = float( 90 ) #angle to be given by user in the command line

    # setup and turn off tracing from turtle 
    t.setup(600, 600)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(-200, 100)
    t.down()
    t.color( 'green' )
    t.width()

    ti.drawString( lstring, distance, angle )
    # ti.drawString( lstring, distance, angle )

    lstring2 = ls.buildString( lsystem2, 4)

    distance = float( 50  ) #distiance to be given by user in the command line 
    angle = float( 90 ) #angle to be given by user in the command line

    # setup and turn off tracing from turtle 
    t.setup(600, 600)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(200, -100)
    t.down()
    t.color( 'red' )
    t.width()

    ti.drawString( lstring2, distance, angle )


    #wait 
    ti.hold()

if __name__ == "__main__":
    main( sys.argv )

# # goto function
# def goto(x, y):
#     turtle.up()
#     turtle.goto(x, y)
#     turtle.down()

# def abstract_image():

#     #position the turtle at (-300, 100)
#     #call draw string with the desired distance and angle

#     mylsys = l.init()


#     # empty lsystem has [" , and an empty list[]]
#     # components of an L string are a base string and rule
#     l.setBase( mylsys, "F * F")     # base has one string 
#     l.addRule( mylsys, ['F', 'F--F--F']) # rule has two strings ( symbol and replacement )


# # drawString function exercutes the turtle goto function and produces the picture
# # representing an L-system 
# opne the file
# Read all the lines of the file into a list of strings 
# chose the file
# Make an empty L-system 

#Loop over the lines 
    #strip the white space from the line 
    #split the line on spaces into words 
    #if the first word is equal to "base"
        #set the base string of the L-system to the second word 
    #else if the first word is equal to 'rule'
        #add a rule to the L-system the is the list with the remaining words 