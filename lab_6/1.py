import sys

sum = 0
n = int(input('n: '))
if not n <= abs(10**4):
	sys.exit()
for i in range(1, abs(n)+1):
	sum += abs(i)
if n >= 1:
	print(sum)
else:
	print(1 - sum)
