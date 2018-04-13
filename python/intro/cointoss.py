
x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1

import random

def tossCoin(num): 
	for i in range(0,num):
		toss = random.randint(0,10)
		attempt = 1
		heads = 0
		tails = 0
		if toss >= 5:
			heads = heads+1
			print "throwing a coin..It's a head!..Got",heads,"head(s) so far and",tails,"tail(s) so far"
		else:
			tails = tails+1
			print "throwing a coin..It's a tail!..Got",tails,"tails(s) so far and",heads,"head(s) so far"
		attempt = attempt + 1


tossCoin(10)
		




