ROOM
	Actions: 
		Add items to rooms
		Print out all items available in the room when the player is in the room. 
	Items:
		Hold items in rooms with a list. 


PLAYER
	Actions:
		- Directions: n, s, e, w
		- Add items to their inventory
	Attributes: 
		- name, current_room
	Item inventory: 
		- List of items
	

ITEM: item.py
	class Item
	Attributes: 
		- name, description


REPL: For player input 
	- choice of direction: N, S, E, W
	- print out error if a player tries to move where there is no room. 


player input functionality: 
	- Allow two words to be entered. 
	- Use .split() to check for two word commands. 
		- Ex. take coins or drop sword

	- Use the verb get to initiate picking up items. [get, item.name] is a command. 

	- If the item is in the room, remove it from the rooms contents and add it to the users inventory, if not, respond with a message. 
