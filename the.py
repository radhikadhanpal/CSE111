# To get current date and time we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
# The now function returns current date and time as a datetime object

# You must convert he datetime object to a string
# before you can concatenate it to another string
# print ("Today is:" + str(current_date))

# Print only the date part of the current date and time.
print (f"{current_date: %Y-%m-%d}")

import math

width_tire = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ration of the tire (ex 60): "))
diameter_wheel = float(input("Enter the diameter of the wheel in inches (ex 15): "))

print()

volume_tire = math.pi * width_tire ** 2 * aspect_ratio * (2540 * diameter_wheel + width_tire * aspect_ratio)
volume_tire1 = volume_tire / 10000000000

volume_tire = round(volume_tire1, 2)

print (f"The approxiamte volume is {volume_tire1:.2f} liters.")


with open ("volume.txt", "at") as volume:

    print(f"{current_date: %Y-%m-%d},{width_tire},{aspect_ratio},{diameter_wheel},{volume_tire1:.2f}", file = volume)
