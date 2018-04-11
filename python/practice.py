def newchar(arr, char):
	newlist = []
	for i in range(0,len(arr)):
		if arr[i].find(char) != -1:
			newlist.append(arr[i])
	print newlist

newchar(['hello','world','my','name','is','Anna'], 'o')


