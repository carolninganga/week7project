# Caroline Ninganga
# Project 7 L-Systems 
# Version 1

# An L-system requires two pieces of information:

# the base string, and
# the list of rules

def __init__(): #The init function creates an empty L-system and returns it. Using the list representation, an empty L-system is a list with two elements: the empty string and an empty list. 
    lsys = ['',[]]
    return lsys

#The getBase function takes in just one argument--the L-system list. 
#It returns the base string, which is the first item in the L-system list.
def getBase( lsys ):
    return lsys[0]

#The setBase function takes in two arguments, an L-system list and a base string. 
#It assigns to the base string field of the L-system list the new string provided in the base parameter.
def setBase( lsys, base ):
    lsys[0] = base

#The addRule function takes in two arguments: an L-system list and a rule. 
#It should append the rule to the list of rules, which is the second item in the L-system list.
def addRule( lsys, rule ):
    lsys[1].append( rule )

#The getRule functions takes in two argument--the L-system and the index of the rule to retrieve. 
#It returns the rule at position index of the L-systems's list of rules.
def getRule( lsys, index):
    return lsys[1][index]


