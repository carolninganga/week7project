# Caroline Ninganga
# Spring 2021 
# CS 5001 
# Grid file for project 7

# import the packages turtle, sys, lsystem and turtle_interpreter
import turtle as t
import sys 
import lsystem as ls
import turtle_interpreter as ti

#default goto function to be used by the for loop
def goto(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def main():

    lsys = ls.createLsystemFromFile( 'systemB.txt' ) # calls the lsystem file to read from 
    t.tracer(False) # used to turn turtle animation on or off and set a delay for update drawings.



    #lsystem is built and ready to be drawn

    x = - 300
    listOfAngles = [ 22, 46, 60 ]
    
    for row in range(3): # iterates through the row and draw from index 0 to 2 producing 3 tress
        x = x + 150 # space between the trees in the rows
        y = 150 #starting distance at the y axis
        for col in range(1,4): #iterates between 1 and 4 
            goto(x,y)
            if col % 3 == 0: # added some color to the first two columns
                t.color('green')
            elif col % 1 == 0: # added some color to the other rows
                t.color('brown')
            lstring = ls.buildString( lsys, col ) #buildString takes in two arguements the lsys and how many times it should iterate given by the value in the inner loop of col
            t.setheading(90) # makes the trees face upwards
            ti.drawString(lstring, 5, listOfAngles[row] ) #draws the strings iterating through the different angles given in the list variable declared above listOfAngles
            y = y - 150 # space between the colomns


    #wait
    ti.hold()

if __name__ == "__main__":
    main()



