x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def stars(x):
	for i in x:
		if isinstance(i,int):
			print "*" * i 
		elif isinstance(i,str):
			length = len(i)
			letter = i[0].lower()
			print letter * length 

stars(x)