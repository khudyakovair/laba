h = int(input('Высота пирамидки: '))

str0 = 'X'
str1 = ''
for i in range(h):
	for j in range(h*2-1):
		if j == h:
			str1 += str0
		elif j < h - i - 1:
			str1 += ' '
	str1 += '\n'
	str0 += 'XX'
print(str1, end = '') 
