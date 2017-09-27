base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
cont = 1
init = base
while cont < expoente:
	init = init * base
	cont += 1
print(init)

#print(base ** expoente)
