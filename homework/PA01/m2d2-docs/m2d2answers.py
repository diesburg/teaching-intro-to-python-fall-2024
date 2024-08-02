import math

#These are part of Guided Practice

def fahrenheitToCelsius():
    fahrenheitInput = input("Please enter the temperature in Fahrenheit: ")
    fahrenheit = float(fahrenheitInput)
    
    celsius = (fahrenheit - 32) * (5/9)

    print("That is "+str(celsius)+" degrees Celsius.")

def minutes():
    minutes = int(input("Please enter the number of minutes: "))

    hours = minutes // 60
    rem = minutes % 60

    print("That is "+str(hours)+" hours and "+str(rem)+" minutes.")


def cookout():

    peopleInput = input("Enter the number of people attending the cookout: ")
    people = float(peopleInput)

    dogsInput = input("How many hot dogs per person? ")
    dogsPerPerson = float(dogsInput)

    numDogs = people*dogsPerPerson

    numDogPackages = numDogs/8
    numDogPackages = math.ceil(numDogPackages)

    numBunPackages = numDogs/12
    numBunPackages = math.ceil(numBunPackages)


    print("We will need to buy "+str(numDogPackages)+" hot dog packages" \
          " and "+str(numBunPackages)+" bun packages.")
    

def peeps():

    ageThreeInput = input("How many age 3 peeps are there? ")
    ageThree = int(ageThreeInput)

    ageFourInput = input("How many age 4 peeps are there? ")
    ageFour = int(ageFourInput)

    pairsThree = ageThree // 2

    pairsFour = ageFour // 2

    newborns = (pairsThree * 3) + (pairsFour * 4)

    print("There are "+str(newborns)+" newborn peeps.")


def pilesOfCorn():

    diameter = float(input("What is the diameter of the circular base in feet? "))

    wallHeight = float(input("What is the height of the wall in feet? "))

    peakHeight = float(input("What is the height of the peak starting from the ground? "))

    #Get the cone height
    coneHeight = peakHeight-wallHeight
    radius = diameter/2

    #Get the volume of the right cylinder (Google "volume of a cylinder")
    cylinderVol = math.pi * radius**2 * wallHeight

    #Get the volume of a cone (Google "volume of cone")
    coneVol = 1/3 * math.pi * radius**2 * coneHeight

    #Total cubic feet
    totalVol = cylinderVol + coneVol

    #Find number of bushels
    bushels = 2.5/totalVol

    print("We can store "+str(bushels)+" bushels of corn in this pile.")

    


#These are part of your homework

def calculateBMI():

    pounds = float(input("Please enter your weight in pounds: "))
    
    inches = float(input("Please enter your height in inches: "))

    bmi = pounds * 703 / (inches * inches)

    print("Your bmi is", bmi)


def findPercentOff():

    original = float(input("Please enter the original price: $"))

    sale = float(input("Please enter the sale price: $"))

    percent = 100 - sale/original*100

    percentRounded = round(percent,0)

    print("That is "+str(percentRounded)+"%")


#team numbers start at 1
def assignTeamNumber():
    personNum = int(input("What number were you assigned? "))

    numberOfTeams = int(input("How many teams do we have? "))

    team = personNum % numberOfTeams

    print("You belong to team", team)

def overtimePay():
    hours = float(input("Please enter the number of hours you've worked >=40: "))

    payRate = float(input("What is the non-overtime rate of pay per hour? "))

    totalPay = round((40*payRate) + ((hours-40)*(payRate*1.5)),2)

    print("Your weekly pay is $"+str(totalPay))
    


def insulation():
    wallLength = float(input("What is the total length of the walls in inches? "))

    bags = math.ceil(wallLength/16/11)

    print("You will need", bags, "bags of insulation.")

def gpa():
    gpaFirst = float(input("What is the GPA earned at the first school? "))
    creditsFirst = float(input("How many credits did the student earn at the first school? "))

    gpaSecond = float(input("What is the GPA earned at the second school? "))
    creditsSecond = float(input("How many credits did the student earn at the second school? "))

    creditsTotal = creditsFirst + creditsSecond

    firstWeight = creditsFirst/creditsTotal
    secondWeight = creditsSecond/creditsTotal

    combinedGPA = gpaFirst*firstWeight + gpaSecond*secondWeight

    print("The combined gpa is", combinedGPA)

def parkingGarage():

    charge = float(input("What is the parking charge in multiples of 25 cents? "))

    payment = float(input("What is the total payment in multiples of quarters, $1, $5, or $10? " ))

    changeReturned = payment - charge

    dollarsReturned = changeReturned//1
    quartersReturned = changeReturned % 1 / .25

    print(dollarsReturned,"$1 bills and",quartersReturned,"quarters were returned.")

#length in feet
# equation found here: https://www.windpowerengineering.com/mechanical/blades/calculate-blade-tip-speed/
# rpm = 15, blade length = 50 meters
# 164 feet is roughly 50 meters
def windGenerator():
    rpm = float(input("What is the rpm rotation of the blade? "))

    length = float(input("What is the length of the blade in feet? "))

    lengthMeters = length * 0.3048

    speed = math.pi * (lengthMeters*2) * rpm * 0.0372

    print("The speed at the tip is:",speed,"mph.")
    







