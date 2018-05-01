
class Store(object):
	def __init__(self, products, location,owner):
		self.products = products
		self.location = location
		self.owner = owner
		self.display()

	def add_product(self, item):
		self.products.append(item)
		self.display()
	
	def display(self):
		print " Products: {}".format(self.products)
		print " location: {}".format(self.location)
		print " Owner: {}".format(self.owner)
	
	def inventory(self):
		print self.products

	def remove_product(self,item):
		self.products.remove(item)
		print self.products

	
costco = Store(['soap','bananas','cereal','steak','cheese'],"3264 long island city, NY"," Sal Ramons")

costco.add_product('salami')
costco.add_product('rice')
costco.add_product('beans')
costco.inventory()
costco.remove_product('cereal')




