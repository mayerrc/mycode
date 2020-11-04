#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showstatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if "desc" in rooms[currentRoom]:
        print(rooms[currentRoom]['desc'])

    print("---------------------------")


# an inventory, which is initially empty
inventory = []


def title():
    # print title
    print('Get Out\n'
          'Controls:\n'
          'go [up, down, north, south, east, west]\n'
          'search\n'
          'get\n')


# Dictionary for the rooms
rooms = {"Landing": {'desc': "You step on to the Landing, and see a Bathroom to the (west)."
                             " Chris's Bedroom to the (north), to the (south) the Nursery and (down) "
                             "the stairs to the Entry Way.", 'south': "Nursery", 'west': "Bathroom",
                     'north': "Chris's Bedroom", 'down': "Entry Way"},
         "Bathroom": {'desc': "You walk in the Bathroom and the smell is awful, with the Landing to your (east).",
                      'east': "Landing"},
         "Chris's Bedroom": {'desc': "You're in Chris's bedroom. To the (south) is a Landing. There is also a ladder"
                                     "leading (up) to the Attic.", 'south': "Landing", 'up': "Attic"},
         "Nursery": {'desc': "You're in the Nursery to the (north) is the Landing.", 'north': "Landing"},
         "Attic": {'desc': "You're in the Attic (down) the ladder is Chris's Bedroom.", 'down': "Chris's Bedroom"},
         "Entry Way": {'desc': "You're in the Entry Way. There are stairs leading (up) to the landing, to the ("
                               "south) is the Living Room and (west) through a door is the Study.", 'up': "Landing",
                       'south': "Living Room", 'west': "Study"},
         "Living Room": {'desc': "You step onto the carpet of the living room. To the (north) is the Entry Way, "
                                 "the (west) you see a dinning room, and a stair well that goes (down) to the "
                                 "Basement. To the (east) is a Hallway with two doors.", 'north': "Entry way",
                         'west': "Dinning Room", 'east': "Hallway", 'down': "Basement"},
         "Study": {'desc': "As you step into the Study you see a desk and the shelves of books behind it. To the (east)"
                           " is the Entry Way.", 'east': "Entry Way"},
         "Dinning Room": {'desc': "You step into a well lit Dinning Room, with a Kitchen to the (west) and the Living "
                                  "Room in the (east).", 'east': "Living Room", 'west': "Kitchen"},
         "Hallway": {'desc': "You step into the Hallway, to the (west) is the Living Room, looks like a Coat Closet "
                             "to the (south) and Master Bedroom to the (north).", 'west': "Living Room",
                     'south': "Coat Closet", 'north': "Master Bedroom"},
         "Coat Closet": {'desc': "You open the door to the Coat Closet and (north) of you is the hall way.",
                         'north': "Hallway"},
         "Master Bedroom": {'desc': "You step through the door into the Master Bedroom, (west) is the Hallway. To  "
                                    "the (east) is the Master Closet and (south) to the Master "
                                    "Bathroom.", 'east': "Master Closet", 'south': "Master Bathroom",
                                    'west': "Hallway"},
         "Master Bathroom": {'desc': "You go from the Master Bedroom which is (north) to the Master Bathroom.",
                             'north': "Master Bedroom"},
         "Master Closet": {'desc': "You open the door and see a huge closet full of clothing, to the (west) is the "
                                   "Master Bedroom.", 'west': "Master Bedroom"},
         "Kitchen": {'desc': "You step into the the Kitchen, the Dinning Room to the (east), you look (north) and "
                             "see the Laundry Room.", 'east': "Dinning Room", 'north': "Laundry Room"},
         "Laundry Room": {'desc': "You step into a Laundry Room. To the (north) is the Garage, "
                                  "(south) is the Kitchen.", 'south': "Kitchen", 'north': "Garage"},
         "Garage": {'desc': "You walk into the Garage. To the (south) is the Laundry Room, (north) is the Drive Way.",
                    'south': "Laundry Room", 'north': "Drive Way"},
         "Back Deck": {'desc': "You step onto the back deck, (down) the stairs is the Side Yard. (north) is the "
                               "Dinning room.", 'north': "Dinning Room", 'down': "Side Yard"},
         "Side Yard": {'desc': "You step onto the Side Yard. (up) a set of stairs is the Back Deck and (east) is the "
                               "Drive Way.", 'up': "Back Deck", 'east': "Drive Way"},
         "Drive Way": {'desc': "On the drive way, the Garage is (south), (west) is the Side Yard, and (east) you see "
                               "the Front Yard.", 'west': "Side Yard", 'east': "Front Yard", 'south': "Garage"},
         "Front Yard": {'desc': "As you come to the Front Yard, (west) is the drive, and (south) is the Entry way.",
                        'west': "Drive Way", 'south': "Entry Way"},
         "Basement": {'desc': "The Basement is dark. (up) the stairs is the Living Room, (west) is the Storage Room, "
                              "and (north) is the Panic Room.", 'up': "Living Room", 'west': "Storage Room",
                      'north': "Panic Room"},
         "Storage Room": {'desc': "You open the door to the Storage Room and see a power panel. The door to the "
                                  "Basement is (east).", 'east': "Basement"},
         "Panic Room": {'desc': "You open the heavy door to see a concrete room with a desk and a few items. (south) "
                                "is the Basement.", 'south': "Basement"}}

currentRoom = "Chris's Bedroom"

title()

# loop forever
while True:

    showstatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('>')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

