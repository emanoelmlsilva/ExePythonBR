lista_perguntas = ['Telefonou para a vitima?','Esteve no local do crime?','Mora perto da vitima?','Devia para a vitima?','Já tabalhou com a vitima?']
cont =0
for index in  range(len(lista_perguntas)):
	v = input('{} '.format(lista_perguntas[index]))
	if v == 'sim':
		cont +=1
if cont <= 2:
	crime = 'Suspeito'
elif cont >= 3 or cont <4:
	crime = 'Cúmplice'
else:
	crime = 'Assassino'
print('Classificação da participação de {}'.format(crime))
