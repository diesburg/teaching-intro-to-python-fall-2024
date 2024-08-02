def topTenNames():
    fin = open('dogs_of_NYC.txt', 'r')

    nameDict = {}

    header = fin.readline()
    for line in fin:
        splitList = line.split("\t")
        name = splitList[0]

        if name not in nameDict:
            nameDict[name] = 1
        else:
            nameDict[name] += 1

    dogList = list(nameDict.items())
    dogList.sort(key=lambda x: x[1], reverse=True)
    for num in range(10):
        miniList = dogList[num]
        print(miniList[0],miniList[1])

    fin.close()

def topTenNamesGender(selectGender):
    fin = open('dogs_of_NYC.txt', 'r')

    nameDict = {}

    header = fin.readline()
    for line in fin:
        splitList = line.split("\t")
        name = splitList[0]
        dogGender = splitList[1]

        if dogGender == selectGender:
            if name not in nameDict:
                nameDict[name] = 1
            else:
                nameDict[name] += 1

    dogList = list(nameDict.items())
    dogList.sort(key=lambda x: x[1], reverse=True)
    if len(dogList) >= 10:
        for num in range(10):
            miniList = dogList[num]
            print(miniList[0],miniList[1])
    else:
        print("There were not 10 dogs with that gender.")

    fin.close()


def spayedDogs():
    fin = open('dogs_of_NYC.txt', 'r')

    spayedDict = {}
    breedDict = {}
    line_count = 0

    header = fin.readline()

    for line in fin:
        splitList = line.split("\t")
        dogType = splitList[2]
        spayed = splitList[7]

        if spayed == "Yes":

            if dogType not in spayedDict:
                spayedDict[dogType] = 1
            else:
                spayedDict[dogType] += 1

        #add total to breed dictionary
        if dogType not in breedDict:
            breedDict[dogType] = 1
        else:
            breedDict[dogType] += 1
        
            
    dogList = []

    for dogType in breedDict:
        if dogType in spayedDict:
            dogList.append([spayedDict[dogType]/breedDict[dogType]*100, dogType])


    dogList.sort()
    dogList.reverse()

    for num in range(10):
        miniList = dogList[num]
        print(miniList[0],miniList[1])


    fin.close()


            
