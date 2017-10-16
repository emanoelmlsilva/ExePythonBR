from random import randrange
cont = 0
guard = None
num = ""
def jogoCraps(dado,dado2):
	global cont
	cont+=1
	fim = ""
	if cont == 1:
		if dado + dado2 == 7 or dado + dado  == 11:
			fim = "natural"
		elif dado +dado2 == 2 or dado + dado2 == 3 or dado + dado2 == 12:
			fim = "craps"
		elif dado+dado2 == 4 or dado+dado2 == 5 or dado+dado2 == 6 or dado+dado2 == 8 or dado+dado2 == 9 or dado+dado2 == 10:
			fim = "ponto"
			global num
			num = dado+dado2
	else:
		if num == dado+dado2:
			fim = "ganhou"
		elif dado+dado2 == 7:
			fim = "perdeu"
	return fim
while True:
	dado = randrange(1,6)
	dado2 = randrange(1,6)
	print("1ª dado = {} , 2ª dado = {}".format(dado,dado2))
	resp = jogoCraps(dado,dado2)
	print(resp)
	if cont == 1 and resp == "natural" or resp == "craps":
		break
	elif resp == "ganhou" or resp == "perdeu":
		break
