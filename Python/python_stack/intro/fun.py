
def odd_even():
	for num in range(1,20):
		if num % 2 == 1:
			print "Number is", num, ".", "This is an odd number"
		if num % 2 == 0:
			print  "Number is", num, ".", "This is an even number"

odd_even()

"""
multiply function 

"""

def mult(arr,b):
	fives = []
	for num in arr:
		fives.append(num * b)
	print fives

mult([1,2,3],5)

"""
hacker challenge 

"""


def layered_mult(arr):
	print arr

	new_array = []
	for x in arr:
		val_arr = []
		for i in range(0,x):
			val_arr.append(1)
		new_array.append(val_arr)
	return new_array

x = layered_mult(mult([2,4,5],3))
print x
"""
6, 12,15
"""











