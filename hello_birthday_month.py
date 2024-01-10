"""
Alexandrea Parks
hello_birthday_month.py
1/10/2024
This program asks the user for their name and birth month and tells the user a greeting with their name, the length of
their name, and if it's currently their birth month or not.
"""

# import datetime module
from datetime import datetime


# main function to call other functions
def main():
    # call inputs function to get name and birthday month
    name, birthday_month = inputs()
    # call processing function with name as argument to get count of letters in name and the current month
    letters_in_name, current_month_text = processing(name)
    # call outputs function with all necessary arguments to output data to user
    outputs(name, birthday_month, letters_in_name, current_month_text)


# function to get user input for name and birthday month
def inputs():
    # get user input
    name = input("Please enter your name: ")
    birthday_month = input("Please enter the month you were born: ")
    return name, birthday_month  # return to main function


# function to get current month and length of name
def processing(name):
    # call method to get current month
    current_month_text = get_current_month()

    # use len() function to get length of name
    letters_in_name = len(name)

    return letters_in_name, current_month_text  # return to main function


# function to get the current month as a string
def get_current_month():
    # create a datetime object with current date and time
    today_datetime = datetime.now()

    # use .strftime() method to convert date object to string with directive for month
    current_month_text = today_datetime.strftime("%B")  # %B is the directive for month

    return current_month_text  # return to main function


# function to output data
def outputs(name, birthday_month, letters_in_name, current_month_text):
    # print greeting with name
    print(f"Hello {name}!")

    # print length of name
    print(f"Your name {name} has {letters_in_name} letters.")

    # use if else logic to determine if it's the user's birth month or not
    if birthday_month.lower() == current_month_text.lower():  # change both to lower so it's case-insensitive
        print("Happy birthday month!")  # print if it's their birth month
    else:
        print("Your birthday is not this month!")  # print if it's NOT their birth month


main()  # call main function to start program







