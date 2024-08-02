for set in range(3):
    knock()
    knock()
    knock()
    print("Penny")

for set in range(3):
    for time in range(3):
        knock()
    print("Penny")


answerYet = "no"
while answerYet=="no":
    for time in range(3):
        knock()
    print("Penny")
    answerYet = input("Did Penny answer the door?")
