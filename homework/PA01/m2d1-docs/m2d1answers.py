import random

#These are part of Guided Practice
def sayHello():
    name = input("What is your name? ")
    message = "Hello, "+name+", it's nice to meet you."
    print(message)

def celsiusToFahrenheit():
    celsiusInput = input("Please enter the temperature in celsius: ")
    celsius = int(celsiusInput)

    fahrenheit = celsius * 9/5 + 32

    print("The temperature is "+str(fahrenheit)+" in fahrenheit.")
    
def calculatePay():
    hoursInput = input("How many hours did you work? ")
    hours = int(hoursInput)

    payInput = input("What is your pay rate per hour? ")
    pay = float(payInput)

    total = hours * pay

    totalRounded = round(total,2)

    print("You have earned $"+str(totalRounded))

def additionGenerator():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    print(str(number1)+" + "+str(number2)+" = ?")

    input("Press enter to see the result.")

    total = number1+number2

    print(total)



#These are part of your homework

def discountPrice():
    originalInput = input("Please enter the original price: ")
    original = float(originalInput)

    percentInput = input("Please enter the percentage off: ")
    percent = float(percentInput)

    sale = original * (100-percent)/100

    roundedSale = round(sale,2)

    print("The sale price is $"+str(roundedSale))

    
def cornStorage():
    storageVolumeInput = input("Please enter the corn storage volume in cubic feet: ")
    volume = int(storageVolumeInput)

    bushels = volume/2.5

    print("We can hold "+str(bushels)+" bushels in "+storageVolumeInput+ " cubic feet.")
 

def KronesToUSD():
    kronesInput = input("Please enter the number of Norweigen Krones to convert to USD: ")
    krones = float(kronesInput)

    USD = krones * 0.12

    USDRounded = round(USD,2)

    print("That is $"+str(USDRounded))
    

def subtractionGenerator():
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    total = number1 + number2

    print(str(total)+" - "+str(number2)+" = ?")

    input("Press enter to see the result.")

    print(number1)

def timeToDestination():
    speedInput = input("Please enter the speed you will be traveling in MPH: ")
    speed = float(speedInput)

    distanceInput = input("Please enter the distance you will be traveling: ")
    distance = float(distanceInput)

    minutes = distance * 60 / speed

    print("That will take",minutes,"minutes.")

#def convertMPG():
mpgInput = input("What is your mpg? ")
mpg = int(mpgInput)

literPer100km = 235.21 / mpg

print("Your L/100km is "+str(literPer100km))

def fuelSavings():
    milesPerYear = float(input("Please enter the miles you drive per year: "))
    currentMPG = float(input("Please enter your current car's MPG: "))
    newMPG = float(input("Please enter the MPG of the new car: "))
    gasCost = float(input("Please enter the current cost of gas per gallon: "))

    #fuel cost for old car
    costCurrent = milesPerYear/currentMPG * gasCost

    #fuel cost for new car
    costNew = milesPerYear/newMPG * gasCost
    
    #savings or loss
    savings = costCurrent - costNew

    print("Fuel cost for your current car is $"+str(round(costCurrent,2)))
    print("Fuel cost for the new car is $"+str(round(costNew,2)))
    print("Savings (or loss) is $"+str(round(savings,2)))

def story():
    total = 30000 + 2000 + 500 + 1000
    equalDivision = total/4

    siblingC = equalDivision 

    print("Sibling C gets $"+str(siblingC)+" in cash.")


 
    





###This is where we automatically run code.  
#def tester():

    #Guided Practice Functions
#    sayHello()

#    celsiusToFahrenheit()
  
#    calculatePay()

#    additionGenerator()


    #Homework Functions
        
#    discountPrice()

#    cornStorage()

#    KronesToUSD()

#    subtractionGenerator()

#    timeToDestination()

#    convertMPG()

#    fuelSavings()

#    story()
    
#This code will run our tester function, which tests all
#of our functions.
##if __name__ == "__main__":    
##    tester()
