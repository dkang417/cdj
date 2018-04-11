# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}


def dict(x):
	myList = []
	for k, v in x.items():
		myList.append((k,v))
	print myList


dict(my_dict)