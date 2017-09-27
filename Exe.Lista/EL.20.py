salario = []
tot	  = 0
min = 0
maior = 0
print('Projeção de Gastos com Abono')
print('============================')
while True:
	num = float(input('Salario: '))
	if num == 0:
		break
	else:
		salario.append(num)
print()
for i in salario:
	abono = i*0.2
	print('Salario	- Abono')
	if abono < 100:
		abono = 100
	if abono == 100:
		min += 1
	if abono > maior:
		maior = abono
	print('R$ {:.2f}	- R$ {:.2f}'.format(i,abono))
	tot += abono
print()
print('Foram processados {} colaboradores'.format(len(salario)))
print('Total gasto com abonos: R$ {:.2f}'.format(tot))
print('Valor minimo pago a {} colaboradores'.format(min))
print('Maior valor de abono pago: R$ {}'.format(maior))
