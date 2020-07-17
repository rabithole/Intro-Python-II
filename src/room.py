# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
	def __init__(self, name, description, items = []):
		self.name = name
		self.description = description
		self.items = items
		self.n_to = None
		self.s_to = None
		self.w_to = None
		self.e_to = None

	def addItems(self, item):
		self.items.append(item)

	def roomItems(self):
		print(f'Items in foyer: {self.items}')

	# def __str__(self):
	# 	return f'{self.n_to}'

# print(Room)



# class Room:
# 	def __init__(self, name, description):
# 		self.name = foyer
# 		self.description = description of foyer
# 		self.n_to = room["overlook"]
# 		self.s_to = room["outside"]
# 		self.w_to = None
# 		self.e_to = room["narrow"]


# while True:
# 	if direction == "n":
# 		if player.currentRoom.n_to is not None:
# 			player.currentRoom = player.currentRoom.n_to
# 		else:
# 			print("go back")

