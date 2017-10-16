nome = input("informe o seu nome: ")
for i in range(len(nome),0,-1):
	print(nome[0:i:1])

"""for i in range(len(nome),0,-1):
	for x in range(i):
		print(nome[x],end='')
	print()"""
