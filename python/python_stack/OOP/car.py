
class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12 
		self.displayinfo()

	def displayinfo(self):
		print " Price:  {}".format(self.price)
		print " Speed: {}".format(self.speed)
		print " Fuel: {}".format(self.fuel)
		print " Mileage: {}".format(self.mileage)
		print " Tax: {}".format(self.tax)

Car1 = Car(2000,"35mph","Full", "15mpg")
Car2 =Car(2000, "5mph", "Not Full", "105mpg")
Car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
Car4 = Car(2000, "25mph", " Full", "25mpg")
Car5 = Car(2000, "45mph", "Empty", "25mpg")
Car6 = Car(200000000, "35mph", "Empty", "15mpg")
