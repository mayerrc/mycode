#!/usr/bin/env python3
print("Get out")
print("Please only use the letter key from the scenario")
friend = input("Who is your best friend?")
rele = input("Name a close relative.")

print("Waking up handcuffed to a bed frame, 'I need to stop drinking'")

print("How am I going to get out?")
ans0 = input("a) Break the bed frame b) Check the nightstand for a key--->")
if ans0.lower().strip() == "a":
    print("The door flies open and a man with an ax comes in, and one slash your head slides off.")
    print("Game Over.")
    exit()
elif ans0.lower().strip() == "b":
    print("Finds key on the night stand and unlocks the handcuffs. You then find your clothes and put them on.")
    ans1 = input("Do I go c) out the window or d) try the door?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans1.lower().strip() == "c":
        print("You open the window and slip on the ledge falling and breaking your neck.")
        print("Game Over")
        exit()
elif ans1.lower().strip() =="d":
        print("You walk over to the door and turn the handle, it opens to a long hallway that goes to the left and right.")
        ans2 = input("Do you go e) left or f) right?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans2.lower().strip() == "f":
    print("You start walking and a board creaks, you look around and see no one. The next step you take you fall through the floor and into the basement. Breaking both femurs and severing your femoral arteries")
    print("Game Over.")
    exit()
elif ans2.lower().strip() == "e":
    print("You hear a noise. Almost like a child crying in the room on your left.")
    ans3 = input("Do you go g) in the room or h) down the hall more?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans3.lower().strip() == "g":
    print("You open the door and step in, the door slams shut and locks. Then you look at the walls as they start to close in and you see pencils come out to impale you. The last thing you hear is do you want to see a magic trick as a pencil disappears into your head.")
    print("Game Over.")
    exit()
elif ans3.lower().strip() == "h":
    print("You step down the hall saying I'm just going to mind my own business. You come to the end of the hall and see a stairwell that goes down and up then a door to what looks like it goes outside. But you hear " + friend +" scream upstairs")
    ans4 = input("Do i) you leave or j) go check on " + friend +"?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans4.lower().strip() == "i":
    print("You look at the door and start walking down the stairs, you get to the door and turn the handle. You pull and hear a click as a blowtorch ignites blasting you with a column of fire.")
    print("Game Over.")
    exit()
elif ans4.lower().strip() == "j":
    print("As you step up the stairs you hear the screams get louder and louder. You come to a door and quietly open it. To see "+ friend + " sitting in a chair tied up. You look and see a man in the corner smashing his head against the wall.")
    ans5 = input("Do you k) go help " + friend +" or l) go deal with the man in the corner?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans5.lower().strip() == "k":
    print("You go to untie "+ friend +", you get one hand free as you are grabbed from behind. Then picked up and strangled.")
    print("Game Over.")
    exit()
elif ans5.lower().strip() =="l":
    ans6 = input("You see m) dental floss or n) a pistol.")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans6.lower().strip() == "m":
    print("Really? REALLY? You just picked dental floss? Like really? Well ok then.")
    print("You walk up behind with the dental floss wrapped around your hand, he then turns around and heel kicks you in the face.")
    print("Game Over.")
    exit()
elif ans6.lower().strip() =="n":
    print("You pick up the pistol and chamber a round. The safety clicks off and you pull the trigger. The man slumps in the corner. You drop the gun in horror of what you just did.")
    ans7 = input("As you untie "+ friend +" you tell them to stay quite. You walk down the stairs and see the door from earlier is boarded up. Do you o) go to the room on the left or p) remove the boards?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans7.lower().strip() =="p":
    print("You and "+ friend +" start ripping the boards off. After you grab the second board you feel a hammer hit you in the back of the head. Then the second time you feel it hit the world goes black.")
    print("Game Over.")
    exit()
elif ans7.lower().strip() =="o":
    print("You round the corner to an open living room with bars on the windows. In the middle of the room is "+ rele +" passed out and badly beaten. They are alive but you need to get them out. You smell smoke and see it coming from the next room.")
    ans8 = input("Your friend wants to split up and look for an exit. Do you go to q) the room with the smoke or r) the dark basement?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans8.lower().strip() == "r":
    print("As your foot reaches for the first step there is nothing but air as you fall hitting your head on a nail a few steps down.")
    print("Game Over.")
    exit()
elif  ans8.lower().strip() == "q":
    print("You walk into the room where the smoke is from and see it's a kitchen with a pot on the stove. You grab the handle to move it and look just soon enough to see "+ friend +"  grab a knife and come at you.")
    ans9 = input("s)throw the pot at them t) try to move?")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans9.lower().strip() == "t":
    print("You jerk to your right slipping and and then pouring the contents of the pot on yourself.")
    print("Game Over.")
    exit()
elif ans9.lower().strip() =="s":
    print("You yeet the pot at them hitting him in the head spilling the contents on them. As they crumple to the ground.")
    ans10 = input("Do you go check on u) "+ rele +" or v) "+ friend +"? ")
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
if ans10.lower().strip() =="v":
    print("Really?")
    print("Game Over. You are a clown.")
    exit()
elif ans10.lower().strip() =="u":
    print("You walk in the room to check on "+ rele +" and find them coming around. You assist them to the kitchen window and help them out the window. You follow them out. You're safe.")
    print("Congratulations. You Won.")
    exit()
else:
    print("Wrong key that sucks. Please only use the characters listed in the scenario.")
    exit()
