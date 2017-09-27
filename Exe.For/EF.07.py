maior = 0
for i in range(5):
	num = int(input('Digite o numero {}: '.format(i+1)))
	if num > maior:
		maior = num
print('O maio número é {} '.format(maior))
