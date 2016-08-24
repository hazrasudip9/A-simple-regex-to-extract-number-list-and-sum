import re

hand = open('regex_sum_311141.txt')
numlist = list()

for line in hand:
	line = line.rstrip()
	stuff =  re.findall('\d+', line)
	
	if len(stuff) ==0: continue
	for i in stuff:
		i = int(i)
		numlist.append(i)
print numlist
numsum = sum(list(numlist))
print numsum





