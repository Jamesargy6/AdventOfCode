import sys, re, operator


def format_room_string(s):
	retVal = ["","",0]
	m = re.search("\d", s)
	retVal[0] = s[:m.start()]
	 
	theRest = s[m.start():]
	retVal[1] = theRest.split("[")[0]

	theRest = theRest.split("[")[1]
	retVal[2] = theRest.split("]")[0]
	return retVal



def determine_most_common(s):
	mostCommonString = ""
	mostCommonDict = {}
	for char in s:
		if char in mostCommonDict:
			mostCommonDict[char] += 1
		else:
			mostCommonDict[char] = 0
	mostCommonDict = sorted(mostCommonDict.items(), key=operator.itemgetter(1), reverse=True)


	commonKeys = []
	commonValues = []
	for dictVal in mostCommonDict:
		commonKeys.append(dictVal[0])
		commonValues.append(dictVal[1])


	commonLetterGroupings = []
	commonLetterGroupings.append("")
	currentValue = commonValues[0]
	currentBigIndex = 0
	currentLittleIndex = 0
	for v in commonValues:
		if currentValue == v:
			commonLetterGroupings[currentBigIndex] += commonKeys[currentLittleIndex]
		else:
			currentValue = v
			currentBigIndex += 1
			commonLetterGroupings.append("")
			commonLetterGroupings[currentBigIndex] += commonKeys[currentLittleIndex] 
		currentLittleIndex += 1


	retString = ""
	for group in commonLetterGroupings:
		group = ''.join(sorted(group))
		for c in group:
			if len(retString) < 5:
				retString += c

	return retString









file = open("day4Input.txt", "r")
rooms = file.read().split("\n")

totalSectorIds = 0
decryptedRoomNames = []
currentIndex = 0
for r in rooms:

	roomParts = format_room_string(r)

	roomName = roomParts[0]
	sectorId = int(roomParts[1]) 
	checksum = roomParts[2]

	fiveMostCommon = determine_most_common(roomParts[0].replace("-",""))


	if(fiveMostCommon == checksum):
		decryptedRoomNames.append(["",0])
		for c in roomName:
			if c != "-":
				currentOrd = ord(c)
				intermediaryOrd = (sectorId % 26) + currentOrd
				if intermediaryOrd > 97+25:
					intermediaryOrd -= 26
			else:
				intermediaryOrd = ord(c)
			decryptedRoomNames[currentIndex][0] += chr(intermediaryOrd)
			decryptedRoomNames[currentIndex][1] = sectorId
		currentIndex += 1	

print(decryptedRoomNames)

for decryptedRoomName in decryptedRoomNames:
	if "north" in decryptedRoomName[0]:
		print(decryptedRoomName)




