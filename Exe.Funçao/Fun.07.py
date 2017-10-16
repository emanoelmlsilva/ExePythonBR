cont = 0
soma = 0
def valorPagamento(valorPrest,numDias):
	if numDias > 0:
		novoValor = round((valorPrest*0.03) + (numDias*0.001)*valorPrest)
	else:
		novoValor = valorPrest
	global cont
	global soma
	cont += 1
	soma += novoValor
	print("Valor a ser pago {}".format(novoValor))

while True:
	valor = float(input("Digite o valor da prestação: "))
	if valor ==  0:
		break
	dias = int(input("Digite o numero de dias de atraso: "))
	print("="*15)
	valorPagamento(valor,dias)
print("="*15)
print("Valor total das prestações {}".format(soma))
print("Quantidade das prestações {}".format(cont))

