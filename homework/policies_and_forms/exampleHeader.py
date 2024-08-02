"""
File: sphere.py
Author: Sarah Diesburg 
Description: A program to calculate the circumference of a
            sphere given it's radius.
"""

import math 

radiusString = input("Enter the radius of your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * (radiusInteger ** 2)

print("The cirumference is:",circumference)
print("The area is:",area)

