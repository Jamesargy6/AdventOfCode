import sys

pInput = 312

buf = [0]
index = 0

#iterate 2017 steps
for x in range(2017):
	#pass through the list and add the next "x"
	for y in range(pInput):
		index = (index+1)%len(buf)
	index += 1
	buf.insert(index, x+1)
#return the value of the next item in the array
print(buf[index+1])