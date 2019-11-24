import hashlib 

input = "iwrupvqb"
found = False
i = 0
while not found:
	m = hashlib.md5()
	string = (input + str(i))
	encodedStr = string.encode()
	m.update(encodedStr)
	hash = m.hexdigest()
	if hash[:5] == "00000":
		print(encodedStr)
		print(hash)
		found = True
	else:
		i += 1
print(str(i))