import math

#sum0 = 2.0 работает без цикла
sum0 = 0
n = int(input("Введите номер члена последовательности: "))

i = 1

#if n == 1:
#	print(sum0)
#elif n % 2 != 0:
#	sum0 += n - 1
#else:
#	sum0 += n - 2 + (n / (n + 1))

while i <= n:
	if n == 1: 
		print(2)
	elif i % 2 == 0:
		sum0 += (i / (i + 1))
	else:
		sum0 += ((i + 1) / i) 
	i += 1
print('%.20f' % (sum0))


