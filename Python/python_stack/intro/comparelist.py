list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5]

def compare_list(list_one, list_two):

	if  len(list_one) != len(list_two):
		print "the lists are not the same"
	else:
		for i in range(0, len(list_one)):
			if list_one[i] != list_two[i]:
				print "the lists are not the same"
				return
			
		print "the lists are the same"

compare_list(list_one, list_two)



