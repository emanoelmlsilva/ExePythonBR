A = 0
B = 1

cresci_A = 0
cresci_B = 0
anos = 0

while A < B:
	A = int(input('informe as populações de A: '))
	B = int(input('Informe as populações de B: '))
	cresci_A = float(input('informe a taxa de Crescimento de A (x%): '))
	cresci_B = float(input('Informe a taxa de Crescimento de B (x%): '))
	A += A * (cresci_A/100)
	B += B * (cresci_B/100)
	anos += 1
print('A quantidade de anos para a população de B ser maior ou igual a A é de {} '.format(anos))







