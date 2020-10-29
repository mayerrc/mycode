#!/usr/bin/env python

while True:
    try:
        num1= float(input("Choose a number"))
        break
    except:
        print("That's not a number!")

while True:
    try:
        fun= input("What function do you want to use? +, -, *, / ") 
        break
            #if fun != "+", "-", "/", "*"
    except:
        print("That's not a function!")
while True:
    try:
        num2= float(input("Choose a second number"))
        break
    except:
        print("That's not a number!")
#num1= float(input("Choose a number"))
#fun= input("What function do you want to use? +, -, *, / ")
#num2= float(input("Choose a second number"))
# the error was actually here... missing a ). Python tries to nail what line the error is on but it doesn't always get it quite right.
def add(num1,num2):
    print(num1+num2)
def subtract(num1,num2):
        print(num1-num2)
def multiply(num1,num2):
        print(num1*num2)
def devide(num1,num2):
        print(num1/num2)
if fun.strip() == "+":
    add(num1,num2)
elif fun.strip() == "-":
    subtract(num1,num2)
elif fun.strip() == "*":
    multiply(num1,num2)
elif fun.strip() == "/":
    devide(num1,num2)
