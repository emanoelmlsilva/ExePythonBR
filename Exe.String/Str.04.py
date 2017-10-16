nome = input("Informe o seu nome: ")
for i in range(len(nome)):
	print(nome[:i+1:]) # ou nome[0:i+1:1]
"""	for x in range(i+1):
		print(nome[x],end='')
	print()"""
