cpf = input("Digite o seu CPF: ")
contDigit=0
for i in cpf:
	if i >= "0" and i <="9":
		contDigit+=1

if cpf[3] == "." and cpf[7] == "." and cpf[11] == "-" and contDigit == 11:
	print("CPF Valido!")
else:
	print("CPF Invalido!")
