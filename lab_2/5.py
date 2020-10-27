import math
q = float (input ('Задайте точность \'q\': '))
x = float (input ('Наберите \'x\': '))

x = math.pi * x / 180 
j = 1
z = True 

# х
s1 = x
while True:
	# решает проблему со знаками
	if z == True:
		zn = -1
		z = False
	else:
		zn = 1
		z = True
	# степени и факториалы
	j += 2
	
	s2 = s1 + (zn * x ** j) / math.factorial(j)
	
	if abs(s1 - s2) <= q:
		break  
	else:
		s1 = s2
print (s1, s2)





