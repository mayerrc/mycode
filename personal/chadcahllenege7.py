#!/usr/bin/env python


while True:
    try:
        num1= float(input("Choose a number"))
        break
    except:
        print("That's not a number!")
    
    #if num1 != float then go back to begining? don't know hot to make it do that
    # so the idea is that if we don't want the user to proceed further down the script until they successfully enter a number, we'll have to trap them in a while loop. AND we need try/except for if they type in something that can't convert into a float (error out)

# the error was actually here... missing a ). Python tries to nail what line the error is on but it doesn't always get it quite right.
fun= input("What function do you want to use? +, -, *, / ")
num2= float(input("Choose a second number"))

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
    multiply(num1,num2) #oops! there was a * instead of a ,

elif fun.strip() == "/":
    devide(num1,num2) # oops! / instead of a ,


