"""
The size of a car tire in the United States is 
represented with three numbers like this: 205/60R15. 
The first number is the width of the tire in millimeters. 
The second number is the aspect ratio. The third number is 
the diameter in inches of the wheel that the tire fits.

"""
import math

width_tire = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ration of the tire (ex 60): "))
diameter_wheel = float(input("Enter the diameter of the wheel in inches (ex 15): "))

print()

volume_tire = math.pi * width_tire ** 2 * aspect_ratio * (2540 * diameter_wheel + width_tire * aspect_ratio)
volume_tire1 = volume_tire / 10000000000

volume_tire = round(volume_tire1, 2)

print (f"The approxiamte volume is {volume_tire1:.2f} liters.")