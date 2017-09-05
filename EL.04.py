v = [0,0,0,0] #,0,0,0,0,0,0]
c = [0,0,0,0] #,0,0,0,0,0,0]
x = 0
soma = 0
for i in range(len(v)):
	num = str.lower(input('Infromer o caractere: '))
	v.append(num)
	cont = 0
	while cont < len(num):
		if(num[cont] == 'a' or num[cont] == 'e' or num[cont] == 'i' or num[cont] == 'o' or num[cont] == 'u'):
			x += 1
			c.append(num[cont])
		cont+=1
#for i in range(0,len(c)):
print('Consoantes: {}'.format(c))
print('Total de consoantes lidas:  {}'.format(x))
