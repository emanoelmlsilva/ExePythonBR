soma = 0
for i in range(5):
	num = float(input('Digite o {} número: '.format(i+1)))
	soma += num
med = soma / 5
print('A soma dos números são {} e a media deles é {} '.format(soma,med))
