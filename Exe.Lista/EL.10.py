lista = list(range(10))
A = []
B = []
C = []
print('vetor A')
for i in range(len(lista)):
	num = int(input('Informe o valor: '))
	A.extend([num])

print('vetor B')
for i in range(len(lista)):
	num2 = int(input('Informat o valor: '))
	B.append(num2)

C = A+B
print(C)
