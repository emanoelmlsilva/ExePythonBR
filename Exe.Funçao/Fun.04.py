def positivoNeg(n):
	if n > 0:
		return "P"
	else:
		return "N"

arg = int(input("Digite o numero: "))
print(positivoNeg(arg))
