# List of keyword which are given by the python

import keyword
print(keyword.kwlist)
print(keyword.iskeyword('Nonee'))

a = 5
b = 6

name = "Priyanshu" # str
age = 23 # int
salary = 5000.0 # float
email = "priyanshu@example.com" # str
comNum = 3 + 5j # complex
isAdult = True # bool
my_list = [2, 3.4, True, "Hello"] # list
my_tuple = (2, 3, 4, False) # tuple
my_set = {34, 5, 2, True, 3 + 5j} # set
my_dict = {
    "name" : "Rishi",
    "age" : 23,
    "courses" : ["SQL", "Python", "AI", "Automation"]
} # dict

name = "Smita"

# Let's print the value and data type of each variable
print("Name is ",name, type(name))
print("Age is ", age, type(age))
print("Salary is ", salary, type(salary))
print("Email is ", email, type(email))
print("Complex number is ", comNum, type(comNum))
print("Is adult? ", isAdult, type(isAdult))
print("My list is ", my_list, type(my_list))
print("My tuple id ", my_tuple, type(my_tuple))
print("My set is ", my_set, type(my_set))
print("My dictionary is ", my_dict, type (my_dict))

PI = 3.14
COMPANY_NAME = "SEED Infotech"

# Implicit type casting
x = 10
y = 32.5
z = x + y
print(z, type(z)) # 42.5 float



name = "Hemant"
age = 36

msg = "My name is " + name + " and age is " + str(age)
print(msg)

# We have some function to convert the value from one type to another type
# int(x) --> convert x into integer
# float(x) --> convert x into float
# str(x) --> convert x into str
# bool(x) --> convert x to boolean 
# complex(x) --> convert x to complex 
# list(x) --> convert x to list
# set(x) --> convert x to set 
# tuple(x) --> convert x to tuple 
# dict(x) --> convert x to dictionary