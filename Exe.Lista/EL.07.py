lista = list(range(5))
v = []
soma = 0
mult = 1
for i in range(len(lista)):
	num = int(input('Digite um valor: '))
	v.append(num)
	soma += num
	mult *= num
print('números {}'.format(v))
print('soma: {}'.format(soma))
print('Multiplicação: {}'.format(mult))
