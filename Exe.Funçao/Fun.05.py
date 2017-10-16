def somaImposto(custo,imposto):
	return custo*(imposto/100) + custo
cust = float(input("Digite o custo: "))
impost = float(input("Digite o imposto (100%): "))
print(somaImposto(cust,impost))
