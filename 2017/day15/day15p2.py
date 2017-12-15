import sys

aStart = 277
bStart = 349

aFactor = 16807
bFactor = 48271
MODULO = 2147483647

aCurrent = aStart*1
bCurrent = bStart*1

result = 0
for x in range(0,5000000):
	if x%100000 == 0:
		print(x)
	aCurrent = (aCurrent*aFactor)%MODULO
	while aCurrent % 4 != 0:
		aCurrent = (aCurrent*aFactor)%MODULO
	bCurrent = (bCurrent*bFactor)%MODULO
	while bCurrent % 8 != 0:		
		bCurrent = (bCurrent*bFactor)%MODULO

	aBinRep = bin(aCurrent)[2:]
	while len(aBinRep) < 32:
		aBinRep = "0" + aBinRep
	bBinRep = bin(bCurrent)[2:]
	while len(bBinRep) < 32:
		bBinRep = "0" + bBinRep

	if aBinRep[16:] == bBinRep[16:]:
		result += 1

print(result)