# Functions - a block of code that can either perform a task or return a value

def greet(name): # paramater which takes in arguments 
    print(f"hi {name}")

greet("chris")

def greet1(first_name, second_name, age):
    print(f"{first_name} {second_name} is {age}")

greet1("john", "smith", 10)

# Better to use return as we can store in a variable, 
# send to file and print outside of the function. 
# print inside - limits the reusability of the function.
# Avoid input() - or anything that uses the command line. 

def greeter(name):
    return(f"hello {name}")

x = greeter("chris")

print(x)

# Defualt args

def greet3(name, age=10): # defualt args must come as last arguments.
    return(f"{name} is {age}")

print(greet3("john"))
print(greet3("john", 20))

# Exercise: make a calc that just does addition of 2 numbers - using a function.

def add_calc(num1, num2):
    x = num1 + num2
    return x

print(add_calc(5,5))

# *args
# If you do not know how many arguments will be passed into your funcion - 
# add a * before the param name
# it will recieve a tuple of arguments

def fruit_list(*fruits):
    print("the fruits are: ")
    for fruit in fruits:
        print(fruit)

fruit_list("apple", "orange", "pear")

def numbers_list(*numbers):
    for i in numbers:
        print(i)
    
numbers_list(1, 2, 3, 4, 5, 6)

# Keyword arguemnts - kwargs
# send arguments as key-value pairs therefore order does not matter
# We define the value when we pass the argument

def fruit_list1(fruit1, fruit2, fruit3):
    print(f"fav = {fruit1}")
    print(f"2nd fav = {fruit2}")
    print(f"3rd fav = {fruit3}")

fruit_list1(fruit1 = "apple", fruit3 = "pear", fruit2 = "orange")

# We also have **kwargs
# If we dont know how many keyword arguemnts there will be.

def fav_food(**food):
    print("fav food is", food["fruit"], "not", food["dairy"])

fav_food(dessert = "ice-cream", fruit = "blueberries", dairy = "cheese")

# Passing a list as an argument

def my_function(food):
    for x in food:
        print(x)

list1 = ["apple", "banana", "cherry"]

my_function(list1)

# format example - using {} as a placeholder

name = "john"
age = 20
height = 1.7

print("my name is {}, i am {}, my height is {} metres".format(name, age, height))

# Also with a variable

x = "my name is {}, i am {}, my height is {} metres"

print(x.format(name , age, height))