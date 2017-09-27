num = 1
cont=[0]*23
soma=0
per=[]
while num != 0:
	s=0
	num = int(input('Número do jogador  (0=fim): '))
	if num > 23:
		print('Informe um valor entre 1 e 23 ou 0 para sair!')
	elif num > 0:
		lista = list(range(1,24,1))
#		lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
		for i in lista:
			if num == i:
				cont[i-1]+=1
#				soma+=cont[i-1]
				soma+=1
				break

print('================================================================')
#print('Número dos jogadores {}'.format(lista))
#print('Quantidade de votos de cada jogador {}'.format(cont))
print('Total de votos computados {}'.format(soma))
for i in lista:
	if cont[i-1] > 0:
		print('número do jogador {}, votos recebido por ele {}'.format(i,cont[i-1]))
		per.append(cont[i-1]/soma)

x=0
maior = 0
for i in lista:
	if cont[i-1] > 0:
		print('Percentual do número {} é {:.2f}'.format(i,per[x]*100))
		if cont[i-1] > maior:
			maior = cont[i-1]
			nome = i
			percent = per[x]*100
		x+=1
print('Melhor jogador foi o número {}, quantidade  de votos {} e o seu percentual {:.2f}'.format(nome,maior,percent))
