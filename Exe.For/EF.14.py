contp = 0
conti = 0
for i in range(10):
	num = int(input('Digite o {} número: '.format(i+1)))
	if num % 2 == 0:
		contp += 1
	else:
		conti += 1
print('Quantidade de números pares são {} e de impares são {}'.format(contp,conti))
