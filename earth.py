import random
import fatherTime
import organism

class Earth(object):
	"""docstring for Earth"""
	def __init__(self, size):
		super(Earth, self).__init__()
		self.size = size
		self.area = []

	def inTheBeginning(self):
		b = []
		for j in range(0, self.size[0]):
			b.append('_')
		#Append the column to each row.
		for i in range(0, self.size[1]):
			self.area.append(b)

		return self.area

	def newOrganism(self, start):
		self.area[start[0]][start[1]] = 'o'

	def deadOrganism(self, start):
		self.area[start[0]][start[1]] = '_'

	def moveOrganism(self, start, end):
		self.area[start[0]][start[1]] = '_'
		self.area[end[0]][end[1]] = 'o'

	def eatFood(self, location):
		self.area[location[0]][location[1]] = '_'

	def eatFood(self, location):
		self.area[location[0]][location[1]] = '*'

if __name__ == '__main__':
	e = Earth((5, 5))
	print(e.inTheBeginning())