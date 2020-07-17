# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
	def __init__(self, name, currentRoom, inventory = []):
		self.name = name
		self.currentRoom = currentRoom
		self.inventory = inventory



	# def move(self):
	# 	if self.currentRoom 

	def __str__(self):
		return f'{self.name} {self.currentRoom.name} {self.inventory}'
