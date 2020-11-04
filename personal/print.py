#!/usr/bin/env python3

def title():
    # print title
    print('Get Out\n'
          'Controls:\n'
          'go [up, down, north, south, east, west]\n'
          'search\n'
          'get\n')


# Dictionary for the rooms
Rooms = {"Landing": {'south': "Nursery", 'west': "Bathroom", 'north': "Chris's Bedroom", 'down': "Entry Way"},
         "Bathroom": {'west' "Landing"},
         "Chris's Bedroom": {'south': "Landing", 'up': "Attic"},
         "Nursery": {'north': "Landing"},
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

