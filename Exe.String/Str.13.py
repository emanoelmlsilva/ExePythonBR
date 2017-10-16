from random import randrange,shuffle
listaPalavra =["cachorro","numero","parodias"]
palavra=listaPalavra[randrange(0,len(listaPalavra))]
embaralha=list(palavra)
shuffle(embaralha)
embaralha="".join(embaralha)
erro = 0
print("Palavra {}".format(embaralha))
while erro < 6:
	certo = input("Qual é a palavra: ")
	if certo == palavra:
		print("PARABENZ,VOCÊ ACERTOU!!!!")
		break
	else:
		erro+=1
		print("{} Erro, tente novamente\n".format(erro))
