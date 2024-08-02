def greenFlag():
    answer = input("How many quizzes did you take? ")
    totalQuizzes = int(answer)

    if totalQuizzes<=0:
        print("Please enter a positive integer answer.")
    else:
        totalEarned = 0

    for quiz in range(totalQuizzes):
        number = quiz +1
        answer = input("What did you get on quiz #"+str(number)+"? ")
        totalEarned = totalEarned + float(answer)

    answer = input("How many total points were possible? ")
    totalPossible = float(answer)

    percentage = totalEarned/totalPossible

    grade = getLetterGrade(percentage)

    print("Your final percentage was "+str(percentage*100))
    print("That means you earned "+grade)


def getLetterGrade(percentage):
    if percentage>=0.9:
        grade="an A"
    elif percentage>=0.8:
        grade="a B"
    elif percentage>=0.7:
        grade="a C"
    elif percentage>=0.6:
        grade="a D"
    else:
        grade="an F"

    return grade

greenFlag()
