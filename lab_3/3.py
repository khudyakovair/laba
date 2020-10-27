import sys

n = int(input('n: '))
if not (n >= 1 and n <= 10):
	sys.exit()

def func0(n):
	print('X'*n)
def func1(n):
	i = 0
	while i < n:
		print('X'*n)
		i = i + 1
def func2(n):
	i = 0
	while i < n:
		if i % 2 == 0:
			print('X'*n)
		else:
			print('-'*n)
		i += 1
def func3(n):
	str0 = 'X-X-X-X-X-'
	i = 0
	while i < n:
		print(str0[:n])
		i += 1
def func4(n):
	str0 = '-'*n
	i = 0
	while i < n:
		print(str0[:i:] + 'X' + str0[i+1::])
		i += 1
def func5(n):
	str0 = '-'*n
	i = 0
	while i < n:
		print(str0[:-i-1:] + 'X' + str0[:i:])
		i += 1
def func6(n):
	str0 = 'X-X-X-X-X-X'
	i = 0
	while i < n:
		if i % 2 == 0:
			print(str0[:n:])
		else:
			print(str0[1:n+1:])
		i += 1
def func7(n):
	i = 0
	str0 = ''
	while i < n:
		str0 += str(i + 1) + ' '
		print(str0)
		i += 1
def func8(n):
	str0 = ''
	for i in range(1, (n**2)+1):
		str0 += str(i) + '\t'
		if i % n == 0:
			print(str0)
			str0 = ''
def func9(n):
	str0 = ''
	boo = True
	for i in range(1, (n**2)+1):
		str0 += str(i) + '\t'
		if i % n == 0:
			if boo:
				print(str0)
				str0 = ''
				boo = False
			else:
				dots = '\t'
				str1 = dots.join(str0.split('\t')[-2::-1])
				print(str1)
				str0 = ''
				boo = True
def func10(n):
	i = j = 1; str0 = ''
	while i <= n:
		while j <= n:
			str0 += '%+4s' % str(i*j) 
			j += 1
		print(str0)
		str0 = ''
		j = 1
		i += 1

print('f0')
func0(n)
print('f1')
func1(n)
print('f2')
func2(n)
print('f3')
func3(n)
print('f4')
func4(n)
print('f5')
func5(n)
print('f6')
func6(n)
print('f7')
func7(n)
print('f8')
func8(n)
print('f9')
func9(n)
print('f10')
func10(n)
