"""
File: <Put the file name here>
Author: <Your name> 
Description: <A description of this code>
"""

import math 

radiusString = input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print("The cirumference is:",circumference)
print("The area is:",area)

