# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

# Call the weekday() method to get the day of the
# week from the current_date_and_time object.
day_of_week = current_date_and_time.weekday()

# Print the day of the week for the user to see.
print(day_of_week) 
#After the computer executes line 8 in the above code,
#  the current_date_and_time variable will hold the current date and time. 
# After the computer executes line 12, the day_of_week variable will hold 0 if today is Monday, 
# 1 if today is Tuesday, and so on to 6 if today is Sunday.
subtotal = 0

#amount = float(input('Please enter the subtotal: '))

print('Please enter the amount of items as well as the cost of such items.')
#So now we need to ask them what the cost of the amount of items
#they are buying
cost = 1
while cost != 0:
    cost = float(input('What is the cost:'))
    if cost != 0:
        quantity = float(input('Please enter the quantity: '))
        subtotal += cost * quantity

print(f'Subtotal: {subtotal:.2f}') 


if day_of_week == 1 or 2 and subtotal >= 50.00:
    discount = subtotal * .10
    subtotal = subtotal - discount 
    sales_tax = subtotal * .06
    total = subtotal + sales_tax

    # sales_tax = discount * .06
    # subtotal = amount - discount + sales_tax
    print(f'Discount amount: {discount:.2f}')
    print(f'Sales tax amount: {sales_tax:.2f}')
    print(f'Subtotal: ${subtotal:.2f}')
    

else:
    sales_tax = subtotal * .06
    subtotal = subtotal + sales_tax
    print(f'Sales tax amount: {sales_tax:.2f}')
    print(f'Total: {subtotal:.2f}')
    