import sys


file = open("day1input.txt", "r")
captcha = file.read()
captcha = captcha + captcha[0]
print("Captcha: ", captcha)

result = 0
prevDigit = -1
currentDigit = -1
index = 0

for digit in captcha:
	prevDigit = currentDigit
	currentDigit = digit
	if prevDigit == currentDigit:
		print("Matching sequence of ", currentDigit, "s at index ", index)
		result += int(digit)
		print("Index ", index, ", Running Total: ", result)
	index += 1


print("Result: ", result)