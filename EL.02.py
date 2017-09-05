
v=[]
quant = int(input('Informe a quantidade de numeros: '))
for c in range(quant):
        num = int(input('Digite o {} valor: '.format(c+1)))
        v.append(num) #l1+=[num] #l1.extend([num])

cont = len(v)
print('Ordem Inversa')
while 0 < cont:
	print(v[cont-1])
	cont -= 1

