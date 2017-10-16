palindromo =input("Informe a palavra: ")
nome=''
nome2=''
for i in palindromo:
	if i != " ":
		nome+=i
j=-1
for i in range(len(nome)):
	if nome[i] != nome[j]:
		fim = "Não é Palindromo"
		break
	else:
		fim = "é Palindromo"
	j-=1
print(fim)

#Outra forma de fazer
#nome2 = nome[::-1]
#if nome == nome2:
#	print("É palindromo")
#else:
#	print("Não é  palindromo")
