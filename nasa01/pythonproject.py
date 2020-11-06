#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  if "desc" in rooms[currentRoom]:
    print(rooms[currentRoom]['desc'])


  print("---------------------------")

#an inventory, which is initially empty
inventory = []
def title():
    # print title
    print('Get Out\n'
          'Controls:\n'
          'go [up, down, north, south, east, west]\n'
          'search\n'
          'get\n')


# Dictionary for the rooms
rooms = {"Landing": {'south': "Nursery", 'west': "Bathroom", 'north': "Chris's Bedroom", 'down': "Entry Way"},
         "Bathroom": {'west' "Landing"},
         "Chris's Bedroom": {'desc':"You're in Chris's bedroom. To the (south) is a Landing. There is also a ladder leading (up) to the Attic.",'south': "Landing", 'up': "Attic"},
         "Nursery": {'desc': "You are in the Nursery to the (north) is the Landing"'north': "Landing"},
         "Attic": {'down': "Chris's Bedroom"},
         "Entry Way": {'up': "Landing", 'south': "Living Room", 'west': "Study"},
         "Living Room": {'north': "Entry way", 'west': "Dinning Room", 'east': "Hallway", 'down': "Basement"},
         "Study": {'east': "Entry Way"},
         "Dinning Room": {'east': "Living Room"},
         "Hallway": {'west': "Living Room", 'south': "Coat Closet", 'north': "Master Bedroom"},
         "Coat Closet": {'north': "Hallway"},
         "Master Bedroom": {'east': "Master Closet", 'south': "Master Bathroom"},
         "Master Bathroom": {'north': "Master Bedroom"},
         "Master Closet": {'east': "Master Bedroom"},
         "Kitchen": {'east': "Dinning Room", 'north': "Laundry Room"},
         "Laundry Room": {'south': "Kitchen", 'north': "Garage"},
         "Garage": {'south': "Laundry Room", 'north': "Drive Way"},
         "Back Deck": {'north': "Dinning Room", 'down': "Side Yard"},
         "Side Yard": {'up': "Back Deck", 'east': "Drive Way"},
         "Drive Way": {'west': "Side Yard", 'east': "Front Yard", 'south': "Garage"},
         "Front Yard": {'west': "Drive Way", 'south': "Entry Way"},
         "Basement": {'up': "Living Room", 'west': "Storage Room", 'north': "Panic Room"},
         "Storage Room": {'east': "Basement"},
         "Panic Room": {'south': "Basement"}}

currentRoom = "Chris's Bedroom"

title()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
