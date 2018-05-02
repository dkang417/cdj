

"""
Multiples- print odd from 1 - 1000
print mult of 5 from 5 1000000
"""

for num in range(1,1000):
	if num % 2 == 1:
		print num

for num in range(5,100):
	if num % 5 == 0:
		print num

"""
sum of all the values: a = [1, 2, 5, 10, 255, 3]
"""
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

"""
average of the values in the list: a = [1, 2, 5, 10, 255, 3]
"""
a = [1, 2, 5, 10, 255, 3]
b = sum(a)/len(a)
print b



