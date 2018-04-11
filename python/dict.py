me = {
	"name" : "david",
	"age" : 32,
	"country of bith" : "USA",
	"favorite language" : "Python"
}

def print_dict(dic):
	for k, v in dic.items():
		print "My {} is {}".format(k,v)

print_dict(me)


