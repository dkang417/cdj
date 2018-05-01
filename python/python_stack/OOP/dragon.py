
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
		print " Health is at: {}".format(self.health)
		
class Dog(Animal):
	def __init__(self, name, health):
		super().__init__(name,health) 
		self.health = 150

	def pet(self):
		self.health += 5
		return self


poodle = Dog("wishbone",150)
monkey= Animal("Curious George", 100)
monkey.walk().walk().walk().run().run().displayHealth()

# dog = Dog("jon")
# dog.walk()
# dog.walk()
# dog.walk()
# dog.run()
# dog.run()
# dog.pet()
# dog.displayHealth()


