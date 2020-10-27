import sys

pos = input('Ваш ход: ')
if not len(pos) == 5:
	sys.exit()

al = 'abcdefgh'
s = list(pos)
for i in range(5):
	for j in range(len(al)):
		if s[i] == al[j]:
			s[i] = str(j)
			break

#print(s)
x0 = int(s[0])
y0 = int(s[1])
x1 = int(s[3])
y1 = int(s[4])

#print(x0, y0, x1, y1)

if ( (abs(x0 - x1) == 1) and (abs(y0 - y1) == 2) ) ^ ( (abs(x0 - x1) == 2) and (abs(y0 - y1) == 1) ):
	print('yes')
else:
	print('no')










