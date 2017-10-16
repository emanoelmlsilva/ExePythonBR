def imprimiCont(cont):
	for i in range(1,cont+1):
		for x in range(1,i+1):
			print(x,end=' ')
		print()

num = int(input("digite um valor: "))
imprimiCont(num)
