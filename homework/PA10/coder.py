from random import randint

def skip(c):
    #lowercase
    if "a"<=c<="z":
        offset = ord(c)-90

    #uppercase
    elif "A"<=c<="Z":
        offset = ord(c)-60

    #number
    elif "0"<=c<="9":
        offset = ord(c)-40

    #anything else
    else:
            if ord(c)%2==1:
                offset = 1
            else:
                offset = 2
    return offset
    

def encode(inputFile, outputFile):
    f1 = open("hamlet.txt","r")
    ham = f1.read()
    hamlist = []
    for c in ham:
        hamlist.append(c)
    shuffle(hamlist)

    f2 = open(inputFile,"r", encoding="ascii")
    stud = f2.read()

    out = open(outputFile,"w", encoding="ascii")

    for c in stud:
        out.write(c)
        offset = skip(c)
        
        #write junk characters
        for i in range(offset-1):
            index = randint(0,len(hamlist)-1)
            out.write(hamlist[index])
            
    out.close()

def shuffle(myList):
    for i1 in range(0,len(myList)-1):
        i2 = randint(i1,len(myList)-1)
        myList[i1],myList[i2]=myList[i2],myList[i1]


def decode(inputFile, outputFile):
    f1 = open(inputFile,"r")
    ham = f1.read()
    out = open(outputFile,"w")

    index=0
    while index<len(ham):
        c=ham[index]
        #print(c)
        out.write(c)
        index += skip(c)
 
    out.close()
