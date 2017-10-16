from random import randrange
listaPalavras = ["musicista","futebolista","mangaba","paralelepipedo"]
palavra = listaPalavras[randrange(1,3)]
nome = "-"*len(palavra)
erro = "".join(palavra)
errar = 0
cont=len(palavra)
print("A palavra é {}".format(nome))
while errar <6:
	letra = input("Digite uma letra: ")
	a=0
	for x,i in enumerate(palavra):
		if letra == i:
			p=palavra.index(i)
			nome=list(nome)
			nome[p]=letra
			palavra=list(palavra)
			palavra[p]="x"
			palavra="".join(palavra)
			cont-=1
			a+=1
			nome="".join(nome)
	print("A palavra é {}".format(nome))
	if a == 0:
		errar+=1
		print("Você errou pela {}ª vez.Tente de novo!\n".format(errar))
	if errar==6:
		print("A palavra erra {}".format(erro))
	if cont == 0:
		print("\nParabenz, você venceu!!!!\n")
		break

