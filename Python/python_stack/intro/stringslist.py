
words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
words = words.replace("day","month")
print words


 x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x = ["hello",2,54,-2,7,12,98,"world"]
first = x[0]
print first 
last = x[-1]
print last 
newArr = [first,last]


x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
firtlist = x[:len(x)/2]
secondlist = x[len(x)/2:]
secondlist.insert(0,firstlist)
print secondlist