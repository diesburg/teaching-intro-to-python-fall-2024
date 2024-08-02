'''
File: letterCount.py
Author: CS 1510
Description: Prints a table of the counts of each letter in a string.
'''

import string

#Function letterCount
#Inputs: inputStr (string)
#Outputs: None
#Description: Prints a table of the letters of the alphabet (in
#   alphabetical order) together with the number of times each letter
#   occurs in inputStr.

def letterCount(inputStr):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    #Let's make our input string lowercase
    lowerStr = inputStr.lower()

    #create the letter dictionary
    letterDict={}

    #Go through our sentence, adding one to our dictionary for
    #each letter we find
    for char in lowerStr:

        #If we have a lowercase letter, add it to the dictionary
        if char in alphabet:

            #If it ISN'T in the dictionary already, put it in with
            #a count of 1
            if char not in letterDict:
                letterDict[char] = 1

            #If it IS in the dictionary, just add 1 to the value
            else:
                letterDict[char] += 1

    #Make a list of keys in the dictionary
    keyList=[]

    for char in letterDict:
        keyList.append(char)

    #Sort the list of keys
    keyList.sort()

    #Use the list of keys to print things out in order
    for char in keyList:
        print(char, letterDict[char])

    #Print the dictionary
    #for char in letterDict:
    #    print(char, letterDict[char])

    
    return None
