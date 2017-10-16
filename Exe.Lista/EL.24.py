import random

def numeroAleatorio():
	return random.randrange(1,7)
vetor = [0,0,0,0,0,0]
for i in range(100):
	num = numeroAleatorio()
	vetor[num-1]+=1
for x,i in enumerate(vetor):
	print("numero {} apareceu {}".format(x+1,i))

