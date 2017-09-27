med = [] # lista vazia para receber as medias
nome = [] # lista vazia para receber os nomes
s = list(range(5)) # lista de tamanho 5 para as variaveis de saltos
salt = [] # lista vazia para quarda os valores de s
t = [] # lista para quarda as listas de salt
while True:
	salt = [] # lista vazia para quardar os valores de s
	soma = 0
	n = input('Informe o nome: ')
	if n == '':
		break
	nome.append(n)
	for x in range(5):
		s[x] = float(input('{}ª Salto: '.format(x+1)))
		salt.append(s[x])
		soma += s[x]
	t.append(salt)
	med.append(soma/5)

print('Resultado Final')
for i in range(0,len(nome)):
	print('Atleta: {}'.format(nome[i]))
	print('Saltos: ',end='')
	print('{}'.format(t[i]),end= ' ')
	print('\nMedia dos saltos: {:.2f} m'.format(med[i]))
