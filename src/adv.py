from room import Room

from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(input('Choose a name: '), room['outside'])

def whichWay():
	global direction 
	direction = input('Choose a compass direction: \n N = North, S = South, E = East, or W = West \n')

whichWay()

# Write a loop that:
while True: 
	if direction == 'n': 
		if player.currentRoom.n_to is not None:
			player.currentRoom = player.currentRoom.n_to
			print('Line 64: You are now in the ', player.currentRoom.name)
			whichWay()
		else: 
			print("Can not go North from here!")
			whichWay()
	if direction == 's':
		if player.currentRoom.s_to is not None:
			player.currentRoom = player.currentRoom.s_to
			print('Line 72: You are in the ', player.currentRoom.name)
			whichWay()
		else:
			print("Can not go South from here!")
			whichWay()
	if direction == 'e':
		if player.currentRoom.e_to is not None:
			player.currentRoom = player.currentRoom.e_to
			print('Line 80: You are in the ', player.currentRoom.name)
			whichWay()
		else:
			print("Can not go East from here!")
			whichWay()
	if direction == 'w':
		if player.currentRoom.w_to is not None:
			player.currentRoom = player.currentRoom.w_to
			print('Line 88: You are in the ', player.currentRoom.name)
			whichWay()
		else:
			print("Can not go West from here!")
			whichWay()
	else: 
		continue
			

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.