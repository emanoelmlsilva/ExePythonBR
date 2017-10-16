frase = input("Informe a frase: ")
contBranco=0
contVogais=0
for i in frase:
	if i == ' ':
		contBranco+=1
	elif i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
		contVogais+=1
print("quantos espaços em branco existem na frase: {}".format(contBranco))
print("quantas vezes aparecem as vogais {}".format(contVogais))
