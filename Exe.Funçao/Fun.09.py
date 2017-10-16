def inverso(n):
#	n = list(str(n))
#	n.reverse()
	n = str(n)
	for i in range(len(n),0,-1):
		print(n[i-1],end='')
	print()

num = int(input("Digite o numero: "))
#print(inverso(num))
print("Inverso",end=' ')
inverso(num)
