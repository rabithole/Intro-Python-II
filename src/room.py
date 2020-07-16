# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
	def __init__(self, name, description, items = []):
		self.name = name
		self.description = description
		self.items = items		

	def addItems(self, item):
		self.items.append(item)

	def roomItems(self):
		print(f'Items in foyer: {self.items}')

	def __str__(self):
		return f'Where: {self.name}: {self.description} Items: {self.items}'

