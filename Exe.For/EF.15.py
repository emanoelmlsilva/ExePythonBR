t1 = 0
t2 = 1
t3 = 0
quant = int(input('Informe a quantidade de números: '))
for i in range(quant):
	print(t3,end=' ')
	t3 = t1 + t2
	t1 = t2
	t2 = t3
print()
