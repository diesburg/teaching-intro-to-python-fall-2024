"""
File: qb_rating.py
Author: CS 1510
Description:
Time: Early
"""

qbFileOpen = open("qb_data_2016.csv", 'r')
qbFileWrite = open("qb_passer_ratings_2016.csv", 'w')

qbFileOpen.readline()

for line in qbFileOpen:
    if line.split(',')[0] != 'PLAYER':
        pName, team, complete, attempt,yards,long,touchD,intercept,sack = line.split(',');
        complete = int(complete)
        attempt = int(attempt)
        yards = int(yards)
        touchD = int(touchD)
        intercept = int(intercept)
        
        compStatA = ((((complete/attempt) * 100) - 30) / 20)   
        yardsStatB = (((yards/attempt) -3) /4)
        tdStatC = ((touchD / attempt) * 20)
        interceptStatD = (2.375 - ((intercept / attempt) * 25))

        if compStatA > 2.375:
            compStatA = 2.375
        elif compStatA < 0:
            compStatA = 0

        if yardsStatB > 2.375:
            yardsStatB = 2.375
        elif yardsStatB < 0:
            yardsStatB = 0  

        if tdStatC > 2.375:
            tdStatC = 2.375
        elif tdStatC < 0:
            tdStatC = 0
        
        if interceptStatD > 2.375:
            interceptStatD = 2.375
        elif interceptStatD < 0:
            interceptStatD = 0

        passerScore = (((compStatA + yardsStatB + tdStatC + interceptStatD) / 6) * 100)

        if passerScore <= 85:
            passerRate = 'BAD'
        elif passerScore <=90:
            passerRate = 'MEDIOCRE'
        elif passerScore <= 95:
            passerRate = 'GOOD'
        else:
            passerRate = 'GREAT'

        stringWrite = pName + ',' + team + ',' + str(passerScore) + ',' + passerRate + '\n'
        qbFileWrite.write(stringWrite)
   
qbFileWrite.close()
