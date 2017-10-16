def desenhaRetangulo(linha,coluna,caracter):
	print(caracter * linha)
	for i in range(coluna):
		espaço = ' '*(linha-2)
		print("{}{}{}".format(caracter,espaço,caracter))
	print(caracter * linha)
l = int(input("Informe a quantidade de linha: "))
c = int(input("Informe a quantidade de coluna: "))
cara = input("informe o caractere desejado: ")
desenhaRetangulo(l,c,cara)
