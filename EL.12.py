lista = list(range(3))
idade = list(range(3))
altura = list(range(3))
soma =  0

for i in range(len(lista)):
	idade[i] = int(input('Digite a idade do {} aluno: '.format(i+1)))
	altura[i] = float(input('Digite a altura do {} aluno: '.format(i+1)))
	soma += altura[i]
med = soma / len(lista)

cont = 0
for c in range(len(lista)):
	if idade[c] > 13 and altura[c] < med:
		cont += 1
print('Quantidade de aluno com idade maior que 13 e altura menor que a media: {}'.format(cont))
