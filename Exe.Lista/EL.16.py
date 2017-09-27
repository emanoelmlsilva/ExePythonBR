cont = 0
salario = [[200,299],[300,399],[400,499],[500,599],[600,699],[700,799],[800,899],[900,999],[1000]]
vendas = float(input('Digite o valor da venda: '))
fila = [0,0,0,0,0,0,0,0,0]
while vendas != 0:
	x = (vendas * 0.09) + 200
	if x < 1000:
		for i in range(0,len(salario)):
			if x >= salario[i][0] and x <= salario[i][1]:
				fila[i] += 1
	else:
		fila[8]+=1
	vendas = float(input('Digite o valor da venda: '))
for i in range(9):
	if i < 8:
		print('valores entre {} e {}'.format(salario[i][0],salario[i][1]))
		print('Quantidade de vendedores é de {}'.format(fila[i]))
	else:
		print('Valores acima de {}'.format(salario[8]))
		print('Quantidade de vendedores é de {}'.format(fila[8]))
