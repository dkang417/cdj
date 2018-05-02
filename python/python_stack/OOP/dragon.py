
class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
			
	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self
		
	def displayHealth(self):
		print " {}'s health is at: {}".format(self.name,self.health)
		
class Dog(Animal):
	def __init__(self, name, health):
		super(Animal, self).__init__() 
		self.health = 150
		self.name = name
		# self.favFood = "roastbeef"
		# self.bedtime = "9pm"
	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self,name,health):
		super(Animal, self).__init__()
		self.health = 170
		self.name = name

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()

flyingDragon = Dragon("Puff", 170)
flyingDragon.fly().displayHealth()

poodle = Dog("Wishbone",150)
poodle.walk().walk().walk().displayHealth()


monkey= Animal("Curious George", 100)
monkey.walk().walk().walk().run().run().displayHealth()


