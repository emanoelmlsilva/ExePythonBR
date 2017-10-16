import random
lista = []
for i in range(6):
	nome = input("Nome do funcionario: ")
	while len(nome) != 15:
		if len(nome) <= 15:
			cal = 15 - len(nome)
			nome += " "*cal
		else:
			print("Tamanho Invalida!, tente novamente")
			nome = input("Nome do funcionario: ")
	byte = int(input("Informe o valor do espaço em byte: "))
	lista.append([nome,byte])

#Função converçao de byte para megabyte
def converçao(lista):
	conv=[]
	for i in lista:
		i[1]=round(i[1]/1000000,2)
	return lista
convert = converçao(lista)
#Função percentual
soma=0
def percentual(lista):
	global soma
	resul=[]
	for i in lista:
		soma+=i[1]
	for x in convert:
		resul.append(round(x[1]/soma*100,2))
	return resul
percen = percentual(lista)
#Programa principal
print("ACME Inc.		Uso do espaço em disco pelos usuários ")
print("----------------------------------------------------------------------")
print("Nr.	Usuário		Espaço utilizado	% do uso")
for x,i in enumerate(lista):
	print("{}	{}	 {} MB		  {}%".format(x+1,i[0],i[1],percen[x]))
medio = soma/len(lista)
print("Espaço total ocupado: {:.2f}".format(soma))
print("Espaço médio ocupado: {:.2f}".format(medio))

