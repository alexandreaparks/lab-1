print("Hello capstone!")

# variables

school = "Minneapolis College"
gpa = 4.0
students_in_class = 22

# if-elif-else

if gpa == 4:
    print("WOW!")
elif gpa > 3:
    print("Awesome!")
else:
    print("Cool!")

# lists

schools = ["MCTC", "DCTC", "North Hennepin Technical College"]

schools.sort()
print(schools)
schools.append("Century College")
print(schools)

schools.reverse()  # returns None
print(schools)

# in operator
# can be used with lists, strings, and dictionary keys

if "MCTC" in schools:
    print("MCTC is one of the schools in the list")

# strings

class_name = "Software Development Capstone"
print(class_name.upper())
print(len(class_name))
print(class_name.split())
print(class_name.split("o"))

if "Capstone" in class_name:  # case sensitive
    print("This must be the capstone")

# loops - for loops over range

for x in range(10):
    print(x)

# loops - for loops over sequence

for s in schools:
    print(s.upper())

for letter in school:
    print(letter * 10)  # repeats each letter 10 times

data = [0] * 10  # creates a list with 10 zeros in it
print(data)

more_data = [None] * 10  # none = no data/value
print(more_data)

# while loops

# name = input("Enter your name: ")
#
# # can also use while not name:
# # because empty strings are considered as False
# while len(name) == 0:
#     print("Please enter at least one character")
#     name = input("Enter your name: ")

# True and False and None

start_of_semester = True
winter = False

if winter:  # don't need to use == False
    print("Brr!")
else:
    print("It is not winter!")

# dictionaries - key/value pairs - keys must be unique

class_codes = {2905: "Capstone", 2560: "Web", 2545: "Java"}

print(class_codes[2560])

for code in class_codes:  # loops over keys
    print(code)  # prints keys
    print(class_codes[code])  # prints values

for code, name in class_codes.items():
    print("The class code is " + str(code) + " and he name is " + name)

# format string
for code, name in class_codes.items():
    print(f"The class code is {code} and he name is {name}")

# slicing strings, lists

schools = ["MCTC", "DCTC", "North Hennepin Technical College"]

# first number included, second number not included
first_two = schools[0:2]  # 0 & 2 = where to start and end
print(first_two)

last_school = schools[-1]  # gets last item in list
print(last_school)
last_two_schools = schools[-2:]
print(last_two_schools)

school_name = "Minneapolis Community and Technical College"
city = school_name[:11]
print(city)

# file IO

with open("data.txt") as f:
    print(f.read())  # reads file

with open("schools.txt", "w") as f:
    f.writelines(schools)  # writes to file

# functions


def get_name():
    print("Hello, please enter your name!")
    name = input("Your name is: ")
    return name


name = get_name()
print(name)