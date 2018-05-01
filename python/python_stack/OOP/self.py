class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayinfo(self):
		print "bike costs {} and the max speed is {} and it has {} miles".format(self.price, self.max_speed, self.miles)

	def ride(self):
		self.miles = self.miles + 10
		print "bike now has {} miles on it".format(self.miles)
	def reverse(self):
		if self.miles>= 5:
			self.miles = self.miles-5 
		print "bike now has {} miles on it".format(self.miles)

bike1 = Bike(100, "30mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayinfo()

