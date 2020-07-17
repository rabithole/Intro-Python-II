from room import Room

from player import Player

#### REPL Read, eval, print, loop
# Read: take user input.
# Eval: evaluate the input.
# Print: shows the output to the user.
# Loop: repeat.


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
# print('Line 34: ', room.name)

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
print(f'Welcome {player.name}. You are currently in the {player.currentRoom}')

direction = input('Which direction would you like to go? \n Choose a compass direction: \n N = North, S = South, E = East, or W = West \n')
# print('Line 54: ', player.currentRoom.n_to)
# Write a loop that:
while True: 
	if direction == 'n': 
		if player.currentRoom is room['outside']:
			player.currentRoom.n_to 
			# player.currentRoom = room['foyer']
			print('You are now in the ', player.currentRoom.name)
			break
			# player.currentRoom = player.currentRoom.n_to

			
		else: 
			print('Line 65: ' ,player.currentRoom.n_to)
			break


		# room['outside'].n_to = room['foyer']
		 
			# player.currentRoom = player.room.n_to
			

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# print('Line 66:', wanda.currentRoom)

# room['foyer'].addItems('sword')
# room['foyer'].addItems('food')
# print(player.n_to)

# room['outside'].addItems('food')

# room['foyer'].roomItems()
# room['outside'].roomItems()


