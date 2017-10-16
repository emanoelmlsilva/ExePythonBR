def mesExtençao(d,m):
	lista = [["janeiro",31],["fevereiro",28],["março",31],["abril",30],["maio",31],["junho",30],["julho",31],["agosto",31],["setembro",30],["outubro",31],["novembro",30],["dezembro",31]]
	return lista[m-1][0]
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mes: "))
ano = int(input("Digite o ano: "))
if dia == 0 and dia > 31 and mes > 0 and mes < 13 or mes == 2 and dia > 28:
	print("NULL")
else:
	print(mesExtençao(dia,mes))
