import sys

file = open("../nputs/day1input.txt", "r")
captcha = file.read()
captcha = captcha
capLength = len(captcha)
halfwayIndexModifier = capLength/2
print("Captcha: ", captcha)
print("Captcha length: ", capLength)
print("Halfway Index: ", halfwayIndexModifier)

result = 0

for x in range(0,int(halfwayIndexModifier)):
	halfwayIndex = int((x+halfwayIndexModifier)%capLength)
	if captcha[x] == captcha[halfwayIndex]:
		print("Matching sequence of ", captcha[x], "s at indexes: ", x, halfwayIndex)
		result += int(captcha[x])
		print("Index ", x, ", Running Total: ", result)

print("Result: ", result*2)