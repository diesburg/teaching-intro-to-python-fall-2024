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


#Keep asking until I get 10 correct
score = 0
keepGoing=True

while keepGoing:
    slotNumber = random.randint(1,len(states))
    index = slotNumber-1  #Scratch starts counting at 1.  Python starts at 0.
    guess = input("What is the capital of "+states[index]+"? ")
    if guess=="quit":
        keepGoing=False
    elif guess==capitals[index]:
        print("Great job.")
        score = score + 1
        if score==10:
            keepGoing=False
    else:
        print("Sorry.")
        print("The correct answer is "+capitals[index])
print("Thank you for playing.")












