import sys, re, operator


def format_room_string(s):
	retVal = ["","",0]
	m = re.search("\d", s)
	retVal[0] = s[:m.start()].replace("-","")
	 
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
for r in rooms:

	roomParts = format_room_string(r)

	roomName = roomParts[0]
	sectorId = int(roomParts[1]) 
	checksum = roomParts[2]

	fiveMostCommon = determine_most_common(roomName)

	print("Five Most Common: ", fiveMostCommon, ", Checksum: ", checksum)

	if(fiveMostCommon == checksum):
		totalSectorIds += sectorId

print(totalSectorIds)




