#Guided practice
def tenQuiz():
    #This segment creates a list of the states
    #  and another list of the capitals.
    #For now you can ignore how this part works
    states = []
    capitals = []
    fin = open("capitals.csv","r")
    for state in fin:
        data = state.split(",")
        states.append(data[0])
        capitals.append(data[3])
    import random

    #keep asking until you get 10 of them correct
    correct = 0


    while correct<5:
        slotNumber = random.randint(1,len(states))
        index = slotNumber-1  #Scratch starts counting at 1.  Python starts at 0.
        guess = input("What is the capital of "+states[index]+"? ")
        if guess==capitals[index]:
            print("Great job.")
            correct=correct+1
        else:
            print("Sorry.")
            print("The correct answer is "+capitals[index])


def quitEarly():
    states = []
    capitals = []
    fin = open("capitals.csv","r")
    for state in fin:
        data = state.split(",")
        states.append(data[0])
        capitals.append(data[3])
    import random

    #keep asking until you get 10 of them correct
    #OR they ask to quit early
    correct = 0

    keepGoing=True
    while keepGoing:
        slotNumber = random.randint(1,len(states))
        index = slotNumber-1  #Scratch starts counting at 1.  Python starts at 0.
        guess = input("What is the capital of "+states[index]+"? ")

        if guess=="quit":
            keepGoing=False
        elif guess==capitals[index]:
            print("Great job.")
            correct=correct+1
        else:
            print("Sorry.")
            print("The correct answer is "+capitals[index])

        if correct==10:
            keepGoing=False



def squareRoot():
    import math
    number = float(input("Calculate the square root of what number? "))
    term1 = float(input("What is your first guess for the square root? "))
    accuracy = float(input("How accurate do you want me to be? "))

    term2 = number/term1

    difference = math.fabs(term1-term2)

    while (difference>accuracy):
        term1 = (term1+term2)/2
        term2 = number/term1
        difference = math.fabs(term1-term2)

    print("The approximate square root is "+str(term1))
    print(str(term1*term1))



#Homework
def guessingGameV1():
    print("I am thinking of a number between 1 and 100.")
    import random
    secret = random.randint(1,100)

    guess = int(input("What is your guess? "))
    while not (guess==secret):
        if guess>secret:
            print("Too high.")
        else:
            print("Too low.")
        guess= int(input("What is your guess? "))

    print("Correct.")
    print("I was thinking of "+str(secret))

def guessingGameV2():
    print("I am thinking of a number between 1 and 100.")
    import random
    secret = random.randint(1,100)

    keepGoing=True
    guesses=1
    while keepGoing:
        guess= (input("What is your guess? "))
        if guess=="quit":
            print("See you later you quitter.")
            keepGoing=False
        else:
            guess=int(guess)
            if guess<1 or guess>100:
                print("That's not between 1 and 100.")
            elif guess==secret:
                print("CORRECT!")
                keepGoing=False
                print("I was thinking of "+str(secret))
                print("You got it in "+str(guesses)+" guesses.")
            elif guess>secret:
                print("Too high.")
                guesses+=1
            else:
                print("Too low.")
                guesses+=1

#elevator
def elevator():
    rating = int(input("What is the rated load of the elevator? "))

    passenger = int(input("What is the weight of the next passenger? "))
    rating -= passenger


    while rating>=0:
        print("That person can get on.")
        passenger = int(input("What is the weight of the next passenger? "))
        rating -=passenger

    print("Time to quit.  This person will exceed the weight limit of the elevator.")


def randomWeights():
    import random
    lyst = []
    calc = 0
    for x in range(40):
        w = random.randint(150,500)
        lyst.append(w)
        calc += w
    print(lyst)
    print(calc)
    
#shipping container
def shipping():
    list1 = [271, 282, 336, 109, 127, 277, 69, 321, 320, 176, 229, 269, 193, 491, 427, 327, 262, 87, 192, 160, 201, 99, 298, 275, 493, 407, 454, 489, 353, 119, 238, 442, 89, 496, 474, 391, 210, 125, 288, 52]

    list2 = [278, 366, 219, 377, 283, 450, 283, 279, 195, 340, 262, 178, 316, 220, 157, 411, 401, 348, 416, 418, 431, 158, 305, 468, 261, 180, 252, 410, 405, 481, 169, 225, 151, 491, 341, 406, 233, 183, 467, 252]

    capacity = 8000
    index = 0
    keepGoing=True
    print(list1)
    while keepGoing:
        capacity -= list1[index]
        if capacity<0:
            keepGoing=False
        else:
            index+=1
    print("You can load the first "+str(index)+" items from this list.")
