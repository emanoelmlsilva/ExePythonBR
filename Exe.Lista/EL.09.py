lista = list(range(10))
A = lista
soma = 0

for i in range(len(lista)):
	A[i] = int(input('Digite o número {}: '.format(i+1)))
	soma += A[i]**2
print('Soma dos quadrados dos números {} '.format(soma))
