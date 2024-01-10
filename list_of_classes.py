"""
Alexandrea Parks
list_of_classes.py
1/10/2024
This program asks the user how many classes they are taking and the name of each of their classes. The class names are
stored in a list and then printed with each class name on a separate line.
"""


# main function to call other functions
def main():
    # call inputs function to get the list of classes
    class_list = inputs()

    # call outputs with the class list as an argument to output the list of classes
    outputs(class_list)


# function to get user input
def inputs():
    # ask how many classes user is taking
    num_of_classes = int(input("Enter the number of classes you are taking: "))
    class_list = []  # create empty list to store class names

    # for loop to ask for name of each class
    for c in range(0, num_of_classes):  # start at 0, count up to but don't include the num_of_classes value
        class_name = input(f"Enter the name of class #{c + 1}: ") # add 1 so counter starts at 1 instead of 0
        class_list.append(class_name)

    return class_list  # return to main function


# function to output data
def outputs(class_list):
    # for loop to print each class in the list
    print("Your class names are: ")
    for c in range(len(class_list)):  # 0 up to but not including length of class_list value
        print(class_list[c])  # use index number (c) to get items from list and print them


main()  # call main function to start program



