# Caroline Ninganga
# 03/22/2021
# Project 7

import sys #import sys
import lsystem as ls #import lsystem
import turtle as t
import turtle_interpreter as ti #import turle_interpreter


def main( argv ):

    # check if there are enough arguement s
    if len ( argv ) < 4:
        print( "usage: %s < lsystem filename> < distance> < angle>" % ( argv[0]))
        exit()

    #create the lsystem from a file
    lsystem = ls.createLsystemFromFile( argv[1] )

    #build the lysytem from a file 
    lstring = ls.buildString( lsystem, 4)

    distance = float( argv[2] ) #distiance to be given by user in the command line 
    angle = float( argv[3] ) #angle to be given by user in the command line

    # setup and turn off tracing from turtle 
    t.setup(400, 400)
    t.tracer(False)

    #draw the lsystem to the shape is oriented up 
    t.left(90)
    t.up()
    t.goto(-200, 200)
    t.down()
    t.color( 'green' )
    t.width()

    it.drawString( lstring, distance, angle )

    #wait 
    it.hold()

if __name__ == "__main__":
    main( sys.argv )

# goto function
def goto(x, y):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

def abstract_image():

    # draw lysytem1 using createLsytemFromFile()
    #generate a string using buildString with 3 iterations
    #position the turtle at (-300, 100)
    #call draw string with the desired distance and angle

    mylsys = l.init()


    # empty lsystem has [" , and an empty list[]]
    # components of an L string are a base string and rule
    l.setBase( mylsys, "F * F")     # base has one string 
    l.addRule( mylsys, ['F', 'F--F--F']) # rule has two strings ( symbol and replacement )


# drawString function exercutes the turtle goto function and produces the picture
# representing an L-system 
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