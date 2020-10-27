import math

n = int(input("Число: "))

i = 0

# while True:
# 	if math.pow(2, i) == n:
# 		print("Yes")
# 		break
# 	elif math.pow(2, i) > n:
# 		print("No")
# 		break
# 	else:
# 		i += 1
if math.log2(n) == int(math.log2(n)):
	print('Yes')
else:
	print('No')




