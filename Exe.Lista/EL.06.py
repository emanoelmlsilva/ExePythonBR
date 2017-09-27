lista = range(10)
v = []
m = []
soma = 0
cont = 0

for i in range(len(lista)):
	soma = 0
	print('Notas do {} aluno'.format(i+1))
	for c in range(4):
		num = int(input('Digite a {} nota: '.format(c+1)))
		soma += num
	med = soma / (c+1)
	m.append(med)
	if med >= 7:
		cont += 1
print('Quantidade de alunos com media maior ou iqual a 7: {}'.format(cont))
print('Medias Totais: {}'.format(m))
