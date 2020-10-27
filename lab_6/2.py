import random


n1 = int(input('Колличество строк: '))
n2 = int(input('Колличество столбцов: '))

fo = open('in.txt', 'w')
fo.write('5\n')
for i in range(n1):
	for j in range(n2):
		if j == n2-1:
			fo.write(str(random.randint(0, 1)))
		else:
			fo.write(str(random.randint(0, 1)) + ' ')
	fo.write('\n')
fo.close()

fi = open('in.txt', 'r')
txt = fi.read()
fi.close()

N = int(txt.split('\n')[0])
lines = [line for line in txt.split('\n')[1::] if len(line) > 0]

s0 = s1 = 0
for i in range(len(lines)):
	line = lines[i].split(' ')
	for n in line:
		if n == '1':
			if i == 0:
				s0 += 1
			else:
				s1 += 1
	if not i == 0:
		if not (s1 == 0):
			s0 *= s1
			print(i + 1, s0, s1)
			s1 = 0
		else:
			pass
		
print(s0)



#print(s0, s1)
#print(s)
#print(N)
