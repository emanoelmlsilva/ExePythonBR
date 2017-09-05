lista = list(range(12))
v = []
soma = 0

for i in range(len(lista)):
	if (i+1 == 1):
		mes = 'Janeiro'
	elif i+1 == 2:
		mes = 'Feveriro'
	elif i+1 == 3:
		mes = 'Março'
	elif i+1 == 4:
		mes = 'Abril'
	elif i+1 == 5:
		mes = 'Maio'
	elif i+1 == 6:
		mes = 'Junho'
	elif i+1 == 7:
		mes = 'Julho'
	elif i+1 == 8:
		mes = 'Agosto'
	elif i+1 == 9:
		mes = 'Setembro'
	elif i+1 == 10:
		mes = 'Outubro'
	elif i+1 == 11:
		mes = 'Novembro'
	elif i+1 == 12:
		mes = 'Dezembro'
	temp = float(input('Informe a temperatura do {} mes: '.format(mes)))
	v.append(temp)
	soma += temp
med = soma/len(lista)

print('Temperatuda media anual: {:.2f}'.format(med))

for c in range(len(v)):
	if v[c] > med:
		print('=====')
		print('{} Grau'.format(v[c]))
		if (c+1 == 1):
			mes = 'Janeiro'
		elif c+1 == 2:
			mes = 'Feveriro'
		elif c+1 == 3:
                        mes = 'Março'
		elif c+1 == 4:
                        mes = 'Abril'
		elif c+1 == 5:
                        mes = 'Maio'
		elif c+1 == 6:
                        mes = 'Junho'
		elif c+1 == 7:
                        mes = 'Julho'
		elif c+1 == 8:
                        mes = 'Agosto'
		elif c+1 == 9:
                        mes = 'Setembro'
		elif c+1 == 10:
                        mes = 'Outubro'
		elif c+1 == 11:
                        mes = 'Novembro'
		elif c+1 == 12:
			mes = 'Dezembro'
		print('mes {}'.format(mes))
