guess = int(input("Enter a number from 1 to 10. "))
while guess>10 or guess<1:
    print("I asked for a number from 1 to 10.  Try again.")
    guess = int(input("Enter a number from 1 to 10. "))


color = input("Name one of the three colors on the US flag. ")
while not (color=="red" or color=="white" or color=="blue"):
    print("That is not a color on the US Flag.  Try again.")
    color = input("Name one of the three primary colors. ")


primary = ["red", "white", "blue"]
color = input("Name one of the three colors on the US flag. ")
while not (color in primary):
    print("That is not a color on the US Flag.  Try again.")
    color = input("Name one of the three primary colors. ")
   

