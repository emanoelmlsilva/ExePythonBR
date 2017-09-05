lista = list(range(10))
v1 = [] #list(range(10))
v2 = [] #list(range(10))
v3 = [] #list(range(10))
v4 = []

for i in range(len(lista)):
	num = int(input('Digite o {} valor: '.format(i+1)))
	v1.append(num)

for i in range(len(lista)):
	num2 = int(input('Digite o {} valor: '.format(i+1)))
	v2.append(num2)
for i in range(len(lista)):
	num3 = int(input('Digite o {} valor: '.format(i+1)))
	v3.append(num3)
v4 = v1+v2+v3
print(v4)
