

# ask how many classes
num_of_classes = int(input("Enter the number of classes you are taking: "))
class_list = [] # create empty list to store class names

# for loop to ask for name of each class
for c in range(0, num_of_classes):
    class_name = input(f"Enter the name of class number {c + 1}: ")
    class_list.append(class_name)

# for loop to print each class in the list
print("Your class names are: ")
for c in range(len(class_list)):
    print(class_list[c])




