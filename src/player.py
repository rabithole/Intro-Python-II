# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
	def __init__(self, name, currentRoom, inventory = []):
		self.name = name
		self.currentRoom = currentRoom
		self.inventory = inventory

	def __str__(self):
		return f'{self.currentRoom}, {self.inventory}'

	def pickUpItem(self, item):
		self.item = item
		self.inventory.append(item)
		