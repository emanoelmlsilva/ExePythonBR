lista = list(range(20))
v = []
vPar = []
vImpar = []
for i in range(len(lista)):
	num = int(input('Informar o {} valor: '.format(i+1)))
	v.extend([num])
	if num % 2 == 0:
		vPar.append(num)
	else:
		vImpar.extend([num])
print('vetor: {}'.format(v))
print('Vetor Par: {}'.format(vPar))
print('Vetor Impar: {}'.format(vImpar))
