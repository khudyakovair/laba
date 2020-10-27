import os

fi = open('input.txt', 'r')
text = fi.read()
fi.close()
# lines = text.split('\n')[:-1:]

# lines = [line for line in text.split('\n') if len(line) > 0]


line = '1 22 3 -9 79'
lst = list(map(int, line.split()))
print(','.join(list(map(str, lst))))

lines = list(filter(lambda line : len(line)>0, text.split('\n')))

print('#1')
for line in lines:
	print(line)

print('#2')
for i in range(len(lines)):
	if i % 2 == 0:
		print(lines[i])

print('#3')
fo = open('output.txt', 'w')
for i in range(len(lines)):
	fo.write(str(i+1) + ' ' + lines[i] + '\n')
fo.close()
os.system('cat output.txt')
print('#4') ; sum = 0
for i in range(len(lines)):
	line = lines[i].split(' ')
	for n in line:
		sum += int(n)
print('sum: ',sum)

from functools import reduce
www = [1,2,3,4,5]
print(reduce(lambda acc, x : acc+x, www))

print('#5') ; sum = 0
#obj = []
for i in range(len(lines)):
	line = lines[i].split(' ')
	
	line = [int(n) for n in line]
	
	for n in line:
		sum += n
	
	if i == 0:
		old = sum
		#obj.append(i) # записываем индекс первой строки
	elif old < sum:
		old = sum
		str0 = lines[i]
		#obj = []
		#obj.append(i) # очистка и новое добавление 
	elif old == sum:
		pass
		#obj.append(i) # добавление идентичных 
	sum = 0
#print('sum: ',old)
print('string: ',str0)
#print('index:',obj)

print('#6')
sum1 = sum2 = 0
for i in range(len(lines)):
	line = lines[i].split(' ')
	for j in range(len(line)):
		if i == j:
			sum1 += int(line[j])
		if j == len(line) - i - 1:
			sum2 += int(line[j])
print('Главная: ',sum1)
print('Побочная: ',sum2)

print('#7')
for i in range(len(lines)):
	line = lines[i].split(' ')
	lines[i] = line
for i in range(len(lines)):
	for j in range(len(line)):
		print(lines[j][i] + ' ', end = '')
	print()

print('#8')

n = int(input('n: '))

fo = open('output.txt', 'w')
for i in range(1, n + 1):
	for j in range(1, n + 1):
		fo.write('%+4s' % str(i*j))
	fo.write('\n')
fo.close()
os.system('cat output.txt')

print('#9')
import random
n = int(input('n: '))
m = int(input('m: '))
fo = open('output.txt', 'w')
for i in range(n):
	for j in range(n):
		fo.write('%+4s' % str(random.randint(0, abs(m))))
	fo.write('\n')
fo.close()
os.system('cat output.txt')











