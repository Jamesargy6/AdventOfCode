import sys


file = open("day1input.txt", "r")
captcha = file.read()
captcha = captcha
capLength = len(captcha)
print("Captcha: ", captcha)
print("Captcha length: ", capLength)

result = 0
index = 0

for x in range(0,capLength):
	#since captcha[-1] is the same as captcha[len(captcha)-1], we can take care of the wrap-around case in the first step
	if captcha[x] == captcha[x-1]:
		print("Matching sequence of ", captcha[x], "s at index ", index)
		result += int(captcha[x])
		print("Index ", index, ", Running Total: ", result)
	index += 1


print("Result: ", result)