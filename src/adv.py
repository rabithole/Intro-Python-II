from room import Room
from player import Player
from item import Item


sword = Item('Sword', 'Samurai sword with magical powers')
potion = Item('Potion', 'Potion with unknown properties')
staff = Item('Staff', 'Wood staff made of 5000 year old wood. It compounds your striking force')
food = Item('Food', 'Fill your belly')
key = Item('Key', 'It opens a door')
shielf = Item('Shield', 'The shield of luck. It will protect you when you are at your weekest')

print('')
print(sword.name, sword.description)
print('')
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
room['outside'].addItems(Item('sword', 'hahaha'))

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Write a loop that:
print('')
playerName = input(f'Choose a name: ')
print('')
player = Player(playerName, room['outside'])
print(f'Welcome {player.name}, \n Your current location is: {player.currentRoom.name} \n You have these items in your inventory: {player.inventory}')

action = input(f'\n What would you like to do? \n D = Choose a direction? \n C = Check what items are around you? \n P = Pick up an item? \n ')

# def whichWay():
# 	global direction 
# 	global roomItems
# 	global inventory
# 	# input(f'Choose an action!')

# 	# if direction:
# 	direction = input(f'Choose a compass direction: \n N = North, S = South, E = East, or W = West \n')

# whichWay()

# Write a loop that:
def whichWay():
	while True: 
		direction = input(f'Choose a compass direction: \n N = North, S = South, E = East, or W = West \n')
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
				player.currentRoom = player.curbobrentRoom.e_to
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
		if direction == 'q':
			break
		else: 
			continue



if action == 'd':
	print('action')
	whichWay()
if action == 'c':
	print('Check Items')
if action == 'p':
	print('Pick up items')


#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
