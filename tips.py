import math

def input_float(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except:
            print("Please enter a valid number.")

def compute_tip(total, percentage):
    return total * percentage

def prompt_percentage():
    percentage = input("What percentage would you like to tip?")
    return percentage

print(compute_tip(5,0.2))