"""
Alexandrea Parks
hello_birthday_month.py
1/10/2024
Description:
"""

# import datetime
from datetime import datetime

today_datetime = datetime.now()

current_month_text = today_datetime.strftime("%B")
print(f"Current month: {current_month_text}")


name = input("Please enter your name: ")
birthday_month = input("Please enter the month you were born: ")

print(f"Hello {name}!")

letters_in_name = len(name)

print(f"Your name {name} has {letters_in_name} letters.")

if birthday_month.lower() == current_month_text.lower():
    print("Happy birthday month!")
else:
    print("Your birthday is not this month!")
