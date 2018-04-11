""" 
print a checkerboard
8 times. 
star space star space star space star space
space star space star space star space star
4 times each 

"""
def rowOne():
	print "* * * * "  

def rowTwo():
	print " * * * *"

def checker():
	num = 4
	while num > 0:
		rowOne()
		rowTwo()
		num = num - 1

checker()