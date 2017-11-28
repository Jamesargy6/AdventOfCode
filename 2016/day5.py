import sys, re, operator, hashlib

input = "uqwqemis"
output =""
currentHash = ""
currentIndex = 0

while len(output) < 8:
	m = hashlib.md5()
	string =  input + str(currentIndex)
	m.update(string.encode('utf-8'))
	currentHash = m.hexdigest()
	if currentHash[:5] == "00000":
		output += currentHash[5]
		print("Current Index: ", currentIndex, ", Current Hash: ", currentHash)
	currentIndex += 1
	if currentIndex%100000 == 0:
		print(str(currentIndex) + "index passed")

print(output)