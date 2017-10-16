def imprimi(n):
	for i in range(n+1):
		for x in range(i):
			print(i,end=' ')
		print()

num = int(input("digite o numero desejado: "))
imprimi(num)
