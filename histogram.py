from random import randint

def randomNumber():
	return randint(0,10)
def asterisk(number):
	astring =""
	for i in range(number):
		astring += "*"
	return astring
tlist=[]

userinput = int(raw_input("How many random values do you want there to be generated?"))
for n in range(0,userinput):
	tlist.append(randomNumber())

count = {"0": 0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0, "10":0}
for key in count:
	for i in range(0, len(tlist)):
		if key == str(tlist[i]):
			count[key] += 1
histogram = {"0": "", "1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"", "10":""}

for key in histogram:
	histogram[key] = asterisk(count[key])

for key in histogram:
	print key + " ", count[key], " "+ histogram[key]

