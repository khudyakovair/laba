import sys


n = int(input('Введите нечётный день: '))
n = 2*n - 1

if n % 2 == 0:
	sys.exit()

arr = []
for i in range(n):
	arr.append(list(' ' * n))

s = 0
for i in range(n):
	for j in range(n):
		if i % 2 == 0:
			# строит верхнюю пирамидку
			if i <= j and j <= n - 1 - i:
				arr[i][j] = 'X'
			# строит ниижнюю пирамидку
			if i >= j and j >= n - 1 - i:
				arr[i][j] = 'X'
		
		if j % 2 == 0:
			# строит левую пирамидку
			if i > j and j < n - 1 - i:
				arr[i][j] = 'X'
			# строит правую пирамидку
			if i < j and j > n - 1 - i:
				arr[i][j] = 'X'
		
for i in range(len(arr)):
	print(*arr[i])

