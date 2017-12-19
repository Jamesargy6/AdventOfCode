import sys

pInput = 312


index = 0
res = 0
#iterate 50,000,000
for x in range(50000000):
	#if the next iteration would go in the first position in the array, recorcd that value
	index = ((index+pInput)%(x+1)+1)
	if index == 1:
		res = x+1
#return the current value of the item that would be at position [1]
print(res)