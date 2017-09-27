A = 80000
B = 200000

cresci_A = 0.03
cresci_B = 0.015
anos = 0

while A < B:
	A += A * cresci_A
	B += B * cresci_B
	anos += 1
print('A quantidade de anos para a população de B ser maior ou igual a A é de {} '.format(anos))
