""" 
print a checkerboard
8 times. 
star space star space star space star space
space star space star space star space star
4 times each 

"""
n=int(input('Please enter a positive integer between 1 and 15: '))
for row in range(1,n+1):
    print *("{:3}".format(row*col) for col in range(1, n+1))