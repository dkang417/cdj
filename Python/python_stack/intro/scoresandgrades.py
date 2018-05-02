def grade():
	import random
	
	
	print "Scores and Grades"

	for i in range(0,10):
		score = random.randint(60,100)
		
		if score >= 60 and score <= 69:
			print "score: ", score, ";", "Your grade is D"
		elif score >= 70 and score <= 79:
			print "score: ", score, ";", "Your grade is C"
		elif score >= 80 and score <= 89:
			print "score: ", score, ";", "Your grade is B"
		else:
			print "score: ", score, ";", "Your grade is A" 
	print "End of the program. Bye!"


grade()





