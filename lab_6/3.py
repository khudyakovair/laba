import sys

S = int(input('S: '))

if not S <= 10**9:
	sys.exit()

sum = 0
for i in range(1, S + 1):
	if S % i == 0 and i <= S // i:
		sum += 1
		print(i, S // i)
print('sum: ', sum)
