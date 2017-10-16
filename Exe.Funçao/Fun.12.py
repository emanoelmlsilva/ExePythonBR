from random import shuffle
def embaralha(palavra):
	lista=list(palavra)
	shuffle(lista)
	palavra= "".join(lista)
	return palavra

nome = input("Informe a palavra desejada: ")
print(embaralha(nome))
