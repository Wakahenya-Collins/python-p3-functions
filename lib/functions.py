#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    

greet_programmer()

def greet(name):
    print(f"Hello, {name}")

greet('Maurice')
#     pass

def greet_with_default(name="Christinna"):
    print(f"Hello there, {name}!!!")
greet_with_default()
#     pass

def add(num1, num2):
    return num1 + num2

num1 = 200000
num2 = 900000
result = add(num1, num2)
print(result)

#     pass

def halve(number):
    if not isinstance(number, (int, float)):
        return None

    return number / 2

number = 67000 
result = halve(number)
print(result)


#     pass
