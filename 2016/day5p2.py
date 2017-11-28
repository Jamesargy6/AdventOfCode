import sys, re, operator, hashlib

input = "uqwqemis"
output = ['','','','','','','','']
currentHash = ""
hashesFound = 0
currentIndex = 0

while hashesFound < 8:
	m = hashlib.md5()
	string =  input + str(currentIndex)
	m.update(string.encode('utf-8'))
	currentHash = m.hexdigest()
	
	if currentHash[:5] == "00000":
		try:
			if 0 <= int(currentHash[5]) < 8 and output[int(currentHash[5])] == '':
				output[int(currentHash[5])] = currentHash[6]
				print("Current Index: ", currentIndex, ", Current Hash: ", currentHash, ", Output: ", output)
				hashesFound += 1
		except ValueError:
			print("Continue")
	currentIndex += 1
	if currentIndex%100000 == 0:
		print(str(currentIndex) + "index passed")

print(output)