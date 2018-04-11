"""
integer filter 

"""

num = input('type a number ')

if num >= 100:
	print "That's a big number!"
elif num < 100:
	print "That's a small number!"

"""
string filter 

"""

sentence = input('type a sentence ')

if len(sentence) >= 50:
	print "Long sentence"
elif len(sentence) < 50:
	print "That's a short sentence"


listinput = input('write a longlist here')

if len(listinput) >= 10:
    print "Big list!"
else: 
    print "Short list."  


