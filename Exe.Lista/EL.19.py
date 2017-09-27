#lista = list(range(1,7)) 
lista = [0]*6
soma = 0
while True:
	print("Qual o melhor sistema operacional para uso em servidores?")
	print("As principais respostas são:")
	print("1- Windowns Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro")
	opçao=int(input(": ") )
	if opçao == 0:
		break
	elif opçao == 1:
		lista[opçao-1] += 1
	elif opçao == 2:
		lista[opçao-1] += 1
	elif opçao == 3:
		lista[opçao-1] += 1
	elif opçao == 4:
		lista[opçao-1] += 1
	elif opçao == 5:
		lista[opçao-1] += 1
	elif opçao == 6:
		lista[opçao-1] += 1
	else:
		print('Invalido, Tente novamente!')
#	soma += lista[opçao-1]
	soma += 1

if lista[0] > 0:
        med0 = lista[0]/soma
        med0 *= 100
else:
	med0 = 0

if lista[1] > 0:
        med1 = lista[1]/soma
        med1 *= 100
else:
        med1 = 0

if lista[2] > 0:
        med2 = lista[2]/soma
        med2 *=100
else:
        med2 = 0

if lista[3] > 0:
        med3 = lista[3]/soma
        med3 *= 100
else:
        med3 = 0

if lista[4] > 0:
        med4 = lista[4]/soma
        med4 *= 100
else:
        med4 = 0

if lista[5] > 0:
        med5 = lista[5]/soma
        med5 *= 100
else:
        med5 = 0

print('Sistema Operacional	Votos	%')
print('------------------      ------  ---')
print('Windowns Server		{}	{:.2f}'.format(lista[0],med0))
print('Unix			{}	{:.2f}'.format(lista[1],med1))
print('Linux			{}	{:.2f}'.format(lista[2],med2))
print('Netware			{}	{:.2f}'.format(lista[3],med3))
print('Mac OS			{}	{:.2f}'.format(lista[4],med4))
print('Outro			{}	{:.2f}'.format(lista[5],med5))
print('------------------		--')
print('Total			{}'.format(soma))

