import math

n = int(input("Число: "))
summ = 0

while n > 0:
	summ += n % 10
	n //= 10
print(summ)
