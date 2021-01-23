# import earth
# import fatherTime

class Organism(object):
	"""docstring for Organism"""


	max_age = 75

	def __init__(self, gender, location):
		super(Organism, self).__init__()
		self.gender = gender
		self.age = 0
		self.location = location
		self.isAlive = True
		self.health = 100

	def eat(self):
		self.health = self.health + 1
		return self.health

	def get_location(self):
		return self.location

	def move(self, new_location):
		self.location = new_location
		self.health = self.health - 1
		return self.location

	def age_organism(self):
		self.age = self.age + 1
		return self.age

	def get_gender(self):
		return self.gender

	def isAliveOrDead(self):
		if self.age >= self.max_age:
			self.isAlive = False
		return self.isAlive

# if __name__ == '__main__':
# 	org1 = Organism('M', (0,0))
# 	f = fatherTime.time()
# 	for i in range(100):
# 		org1.move((i,0))
# 		print(org1.get_location())
# 		print(org1.isAliveOrDead())
# 		print(org1.age_organism())
# 		print(f.epochElapsed())		

		