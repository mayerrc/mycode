#!/usr/bin/env python3
#q = exit()
def q1():
    print("I just saw someone I know, do I say Hi? Do you remeber the person's name?")
    ans= input("YES or NO   ").lower().strip()

    if ans == "yes":
        q5()

    elif ans == "no":
        q2()

    elif ans == "q":
        exit()

    else:
        q1

def q2():
    print("Do you remeber the person's name?")
    ans= input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Run for it.")

    elif ans == "no":
        q3()

    elif ans == "q":
        exit()

    else:
        q2

def q3():
    print("Can you pretend to get a call on your cell?")
    ans= input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Hello, doctor. What are my test results?")

    elif ans == "no":
        q4()

    elif ans == "q":
        exit()

    else:
        q3()

def q4():
    print("Are you wearing sunglasses")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Keep walking")

    elif ans == "no":
        print("Address the person using an amussing nickname such as Sarge, Slugger or Master Blaster.")

    elif ans == "q":
        exit()

    else:
        q4()

def q5():
    print("Is it an EX?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        q6()

    elif ans == "no":
        q9()

    elif ans == "q":
        exit()

    else:
        q5()

def q6():
    print("Are you drunk?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        q7()

    elif ans == "no":
        q8()

    elif ans == "q":
        exit()

    else:
        q6()

def q7():
    print("Do you want to rekindle and/or give'em the what for speech?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Say Hi")

    elif ans == "no":
        print("Don't say hi you deserve better anyway king/queen.")

    elif ans == "q":
        exit()

    else:
        q7()

def q8():
    print("Are you in a convertible with Brad Pitt and/or Rihanna?")
    ans= input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Say Hi")

    elif ans == "no":
        print("Don't say hi you deserve better anyway king/queen.")

    elif ans == "q":
        exit()

    else:
        q8()

def q9():
    print("A friends EX?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Don't say hi, Bro code article 1/Girl code article 1")

    elif ans == "no":
        q10()

    elif ans == "q":
        exit()

    else:
        q9()

def q10():
    print("Are you drunk?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        q8()

    elif ans == "no":
        q11()

    elif ans == "q":
        exit()

    else:
        q10()

def q11():
    print("Are you robbing a bank?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("Sure, say hi. It won't blow the whole thing. That's a joke. Don't say hi, grab the money we got to go.")

    elif ans == "no":
        q12()

    elif ans == "q":
        exit()

    else:
        q11()

def q12():
    print("Are you in a bathrobe?")
    ans = input("YES or NO   ").lower().strip()

    if ans == "yes":
        print("No, go get clothes you clown.")

    elif ans == "no":
        print("Say Hi.")

    elif ans == "q":
        exit()

    else:
        q12()

if __name__ == "__main__":
    q1()
