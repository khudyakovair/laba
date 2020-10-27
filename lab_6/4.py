import sys
print('Результаты охоты')
string = str(input('String: '))

string = list(string)
for i in range(len(string)):
	for j in range(len(string)):
		if int(string[i]) > int(string[j]) and i < j:
			tmp = string[i]
			string[i] = string[j]
			string[j] = tmp

sum = 1
sp = []
sp1 = []
boo = False
for i in range(len(string)):
	if boo == False:
		old = string[i]
		sp1.append(old)
		boo = True
	else:
		if old == string[i]:
			sum += 1
		else: 
			sp.append(sum)
			sum = 1
			old = string[i]
			sp1.append(old)
		if i == len(string) - 1:
			sp.append(sum)
print('Массив с колличеством одинаковых элементов: ', sp)
print('Массив с каждым из представителей списка: ', sp1)
string = ''
for i in range(len(sp)):
	string += str(sp[i]) + sp1[i]

print(string)









