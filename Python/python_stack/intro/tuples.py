
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tup(dict):
	myList=[]
	for k, v in dict.items():
		myList.append((k,v))
	print myList


tup(my_dict)


