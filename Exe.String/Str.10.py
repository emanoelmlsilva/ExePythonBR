extenço = ["Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove","Dez","Onze","Doze","Treze","Catorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove"]
extenço2 = ["Vinte","Trinta","Quarenta","Cinquenta","Sessenta","Setenta","Oitenta","Noventa"]
num = input("Digite um numero entre 1 e 99: ")
if int(num) < 20:
	print(extenço[int(num)-1])
else:
	print("{} e {}".format(extenço2[int(num[0])-2],extenço[int(num[1])-1]))
