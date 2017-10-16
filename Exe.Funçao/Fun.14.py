def quadroMagico(vetor):
	i=0
	while i < 9:
		print(vetor[i:i+3])
		i+=3
	if vetor[0] + vetor[1] + vetor[2] == vetor[3] + vetor[4] + vetor[5] == vetor[6] + vetor[7] + vetor[8] == vetor[0]+vetor[3]+vetor[6] == vetor[1] + vetor[4] + vetor[7] == vetor[2]+vetor[5]+vetor[8]==vetor[0]+vetor[4]+vetor[8]==vetor[2]+vetor[4]+vetor[6]:
		return "Quandro Magico"
	else:
		return "Não é quadro magico"

vetor = [0]*9
for x,i in enumerate(vetor):
	vetor[x]+=int(input("Digite o {} valor: ".format(x+1)))
print(quadroMagico(vetor))
