def evenOrOdd():
    number = int(input("Please enter a number: "))

    if number % 2 == 0:
        print("The number is even")

    if number % 2 == 1:
        print("The number is odd")

def tipper():
    cost = float(input("What did the meal cost? "))

    tip = cost * .2

    if tip < 2.50:
        tip = 2.50

    #convert to rounded $
    tip = '{:,.2f}'.format(tip)

    print("The tip is $"+tip)



def vowel():
    letter = input("Please enter the letter: ")

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("It is a vowel.")
    else:
        print("It is not a vowel.")


def calculateBMI():

    pounds = float(input("Please enter your weight in pounds: "))
    
    inches = float(input("Please enter your height in inches: "))

    bmi = pounds * 703 / (inches * inches)

    print("Your bmi is", bmi)

    if bmi<18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

#NOTE - move marines up to guided practice for flags
def marines():
    citizen = input("Are you a US citizen or green card holder? (yes/no): ")
    health = input("Are you in good health? (yes/no): ")
    school = input("Do you have a high school diploma or GED? (yes/no): ")
    age = int(input("Please enter your age: "))
    score = int(input("Please enter your AFQT score: "))
    flag = False


    if citizen=="yes" and health=="yes" and school=="yes":
        if age>=17 and age<=29:
            if score >= 31:
                flag=True

    if flag:
        print("You qualify for entry into the Marines.")
    else:
        print("You do not currently qualify for entry into the Marines.")


##Homework problems

def betterOvertime():
    hours = float(input("How many hours did you work? "))

    pay = float(input("What is your base pay? "))

    if hours <= 40:
        total = hours*pay
    else:
        overtime = hours - 40
        total = (40*pay) + (overtime*(pay*1.5))

    total = '{:,.2f}'.format(total)

    print("The total pay is $"+total)

def secretPass():
    secret = "l3tme1n!"
    password = input("Please enter the secret password: ")

    if password == secret:
        print("Welcome!")
    else:
        print("Password doesn't match.")


def height():
    gender = input("What gender should we test? ")
    height = float(input("What is the height we should test in inches? "))

    if gender == "M":
        if height < (69.5-3) or height > (69.5+3):
            print("Not within average.")
        else:
            print("Within average.")

    if gender == "F":
        if height < (64-2.5) or height > (64+2.5):
            print("Not within average.")
        else:
            print("Within average.")





def weather():
    clouds = float(input("What percentage of the sky has clouds? "))

    if clouds <= 30:
        print("Clear")
    elif clouds <=70:
        print("Partly cloudy")
    elif clouds <=99:
        print("Cloudy")
    else:
        print("Overcast")
        

def leapYear():
    year = int(input("Please enter the year: "))

    if (year % 4==0):
        if (year % 100) == 0 and (year % 400) != 0:
            print("Not a leap year")
        else:
            print("Is a leap year")
    else:
        print("Not a leap year")




def ipersQualify():
    age = int(input("Please enter your age: "))
    service = int(input("Please enter your years of service: "))
    flag = False

    #Only one condition must be True
    if age+service >= 88:
        flag = True
    elif age>=62 and service >=20:
        flag = True
    elif age>=65:
        flag = True

    if flag:
        print("You qualify for drawing IPERS retirement.")
    else:
        print("You do not yet qualify for drawing IPERS retirement.")

#don't do this one
def triangle():
    side1 = int(input("Enter the length of side 1: "))
    side2 = int(input("Enter the length of side 2: "))
    side3 = int(input("Enter the length of side 3: "))
    

    #check for not a triangle
    if (side1+side2)<=side3 or (side1+side3)<=side2 or (side2+side3)<=side1:
        print("Not a triangle.")
    elif side1==side2 and side1==side3:
        print("Equilateral triangle.")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Isosceles.")
    else:
        print("Scalene.")
        
        
        
        
