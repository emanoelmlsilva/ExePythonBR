num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))
soma = 0
for i in range(num1+1,num2):
	print(i,end=' ')
	soma += i
print('\nSoma dos números {} '.format(soma))
