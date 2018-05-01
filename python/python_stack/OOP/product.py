
class Product(object):
	def __init__(self, price, name, weight, brand):
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def tax(self):
		self.tax = .08 * self.price
		self.price = self.price + self.tax
		self.display()

	def Return(self,reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0
		elif reason == "inbox":
			self.status = "for sale"
		elif reason == "opened":
			self.status = "used"
			discount = self.price * .20 
			self.price = self.price - discount
		self.price = self.price - self.tax
		self.display()

	
	def display(self):
		print " Price: {}".format(self.price)
		print " Name: {}".format(self.name)
		print " Weight: {}".format(self.weight)
		print " Brand: {}".format(self.brand)
		print " Status: {}".format(self.status)

	
soap = Product(10,"dove body wash","5 pounds", "Dove")
soap.tax()

cereal = Product(6,"Lucky Charms", "3pounds", "General Mills")
cereal.tax()




