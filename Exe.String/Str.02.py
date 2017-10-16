nome = input("Informe o seu nome: ")
for i in range(len(nome)-1,-1,-1):
	print(str.upper(nome[i]),end='')
print()
