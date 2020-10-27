import math

n = int(input("Десятичное целое число: "))
n0 = n
str1 = ""
str2 = ""
while n0 > 0:
	str1 += str(n0 % 8)
	n0 //= 8
str2 = str1[::-1]
print(str2)
for i in range(len(str1)):
	str2 += str1[len(str1) - 1 - i]
print("Восьмиричное число: ", str2)
