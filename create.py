def createLsystemFromFile( filename ):
    """ Create an L-system list by reading in the specified file """
    # assign to lsys the result of calling the function init()
    lsys = init()
    # assign to fp the result of opening the file (use open(filename, "r") )
    fp.write("new_file\ n")
    # assign to lines the result of calling fp.readlines()
    # close the file using the close method of the file object held in fp
    fp.close()

    # for each line in the list lines
        # assign to line the result of calling line.strip() 
        # assign to words the result of calling line.split(' ')
        # if the first item in words is equal to 'base'
            # use the setBase function passing in the second item in words as the new base string
        # else if the first item in words is equal to 'rule'
            # use the addRule function passing in all but the first item in words as the new rule
  # return the L-system list lsys
