cont = 0
def quantDigitosNum(num):
	num = str(num)
	global cont
	for i in num:
		cont += 1
	return cont

n = int(input("Digite o numero para saber a quantidade: "))
print("Quantidade de Digitos de um numero {}".format(quantDigitosNum(n)))
