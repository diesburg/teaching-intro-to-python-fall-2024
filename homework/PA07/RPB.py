"""
File: RPB.py
Author: [Your name]	
Description: This program reads poem files and creates three new versions
of the poems.  Please run this program by pressing F5 and typing:

main()

in the shell.  You can also run each function individually in the shell.
Be sure to test your functions using the different poem files included in
the assignment, not just "maryPoem.txt".
"""


# Function: main
# Inputs: Nothing
# Outputs: Returns None, but creates 3 output files that
#          change the poemFileName
def main():
    """Runs all the functions that change the poem"""
    
    poemFileName = "maryPoem.txt" #can also change to "LostGeneration.txt"
    
    print ("")  # blank line
    
    #(1) 
    print ("(1) Starting Reading Lines Backwards ...\n")
    readingLinesBackwards( poemFileName )
    
    #(2)
    print ("(2) Starting Odd Lines ...\n")
    oddLines( poemFileName )
    
    #(3)
    print ("(3) Starting Reading Words Backwards ...\n")
    readingWordsBackwards( poemFileName )
    
    print ("\nDone.\n")



# Function: readingLinesBackwards
# Inputs: poemFileName (must be a text file in the same
#         directory as this program
# Outputs: function returns None, but an output file is
#          written that is backwards with "backwards_"
#          prepended to the file name.

def readingLinesBackwards( poemFileName ):
    """Creates a new file with poemFileName written backwards"""

    print("\tThis function is almost done. To finish this function,\n" +\
          "\tplease write line numbers at the beginning of each\n" +\
          "\tline.  Then delete this print statement.\n")
    
    inputFile = open(poemFileName, 'r')
    
    newFileName = "linesBackwards_" + poemFileName
    outputFile = open(newFileName, 'w')

    # make an empty list to hold all the lines of a poem
    allLines = []

    # skip the title and author lines  
    inputFile.readline()
    inputFile.readline()
    
    # skip blank line after the author name
    inputFile.readline()
    
    # now read each line of the poem and store the lines in a list
    for nextLine in inputFile:
        allLines.append(nextLine)

    
    # close the input (original) file
    inputFile.close()
    
    # now reverse the lines in the list
    allLines.reverse()
      
    # write the lines in the list to the file, one at a time.   
    for line in allLines:
        outputFile.write(line)
    # end of for loop

    print("\t" + newFileName +" created.\n")

    outputFile.close()
    return None


    
# Function: oddLines
# Inputs: [You write this]
# Outputs: [You write this]
def oddLines( poemFileName ):
    """You need to write the docstring"""
    
    inputFile = open(poemFileName, 'r')
    newFileName = "oddLines_" + poemFileName
    outputFile = open(newFileName, 'w')
    
    print ("\t You have to write the oddLines function. \n")
    #Put your new code here.  Hint: You might want to reuse
    #some of the code from the previous function.
    
    inputFile.close()
    outputFile.close()
    return None
    
    

# Function: readingWordsBackwards
# Inputs: [You write this]
# Outputs: [You write tis]

def readingWordsBackwards( poemFileName ):
    """You need to write the docstring"""    
    inputFile = open(poemFileName, 'r') 
    newFileName = "wordsBackwards_" + poemFileName
    outputFile = open(newFileName, 'w')
    
    print ("\t You have to write the readingWordsBackwards function. \n")
    #Put your new code here.  Hint: Read each line in the file and reverse
    #the list of lines (like the first function).  Next, go through each line
    #in your list, then use .split() to get a list of words out of each line. 
    #Next, you can reverse the list of words before you write them to the output
    #file.

    #This function will be challenging.  You will get most of the points
    #even if you can't figure out how to remove the punctuation, but you will
    #get all the points if you can figure it out based on the tools
    #we've already gone over in class.

    inputFile.close()
    outputFile.close()
    return None
    

 




    
