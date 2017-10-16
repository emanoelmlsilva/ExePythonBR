print("Valida e corrige número de telefone")
numTelefone = input("Telefone: ")
numTelefone=list(numTelefone)
cont=0
formato = False
for i in numTelefone:
	if i == "-":
		formato = True
		index = numTelefone.index(i)+1
	elif int(i) >= 0 and int(i) <= 9:
		cont+=1
#Adicionado 0 a lista numTelef se a quantidade de numeros for iqual a 7,ordenando 0 para o inicio e mudando o valor dele para 3
if cont == 7:
	print("+"*75)
	print("Telefone possui 7 digitos. Vou acrescentar o digito três na frente.")
	numTelef = list(numTelefone)+["0"]
	aux=0
	for i in range(len(numTelef)-1,0,-1):
		aux = numTelef[i]
		numTelef[i] = numTelef[i-1]
		numTelef[i-1] = aux
	numTelef[0]="3"
	num = numTelef
	numTelefone=list(numTelef)
#colocando formato no numero de telefone (formato for False),adicionado o sinal(-) no ultimo valor e movendo ele para o meio.
	if formato == False:
		numTelefone+=["-"]
		for i in range(len(numTelefone)-1,4,-1):
			aux = numTelefone[i]
			numTelefone[i] = numTelefone[i-1]
			numTelefone[i-1] = aux
	else: #se nao removendo o sinal(-).
		del numTelef[index]
#convertendo as lista para string
numTelefone="".join(numTelefone)
numTelef ="".join(numTelef)

print("="*80)
print("telefone corrigido sem formatação: {}".format(numTelef))
print("telefone corrigido com formatação: {}".format(numTelefone))
