# Caroline Ninganga
# 03/22/2021
# Project 7

import turtle as t

def drawString(string, dist, angle ):
    """ Interpret the characters in string as a series of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the angle (in degrees) for each right 
    or left command. The list of turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save the turtle's heading and position
    ] : restore the turtle's heading and position 
    """

    # assign to stack the empty list
    stack = {}
    # for each character d in string 
    for c in string :
        # if d is equal to 'F'
        if c in string :
            # tell the turtle go forward by distance
            t.forward( dist )
        # else if d is equal to '-'
        # else if d is equal to '+'
        # else if d is equal '['
            # append to stack the position of the turtle (position method)
            stack.append(t.position())
            # append to stack the heading of the turtle (heading method)
            stack.append(t.heading())
        # else if c is  equal to ']'
        elif c == ']':
            # tell the turtle to pick up pen 
            t.up()
            # call the setheading method of the turtle and pass it the value popped off stack
            t.setheading( stack.pop())
            # call the goto method of the turtle and pass it the value popped of stack
            t.goto(stack.pop())
            # tell the turtlr to put down pen
            t.down()
    # call the turtle.update() (not in the for loop)
    t.update()



