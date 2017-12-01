import sys


file = open("day1input.txt", "r")
captcha = file.read()
captcha = captcha + captcha[0]
capLength = len(captcha)-1
halfwayIndexModifier = capLength/2
print("Captcha: ", captcha)
print("Captcha length: ", capLength)
print("Halfway Index: ", halfwayIndexModifier)


result = 0
currentDigit = -1
compareDigit = -1

for x in range(0,capLength):
	halfwayIndex = int((x+halfwayIndexModifier)%capLength)
	currentDigit = captcha[x]
	compareDigit = captcha[halfwayIndex]
	if currentDigit == compareDigit:
		print("Matching sequence of ", currentDigit, "s at indexes: ", x, halfwayIndex)
		result += int(currentDigit)
		print("Index ", x, ", Running Total: ", result)


print("Result: ", result)