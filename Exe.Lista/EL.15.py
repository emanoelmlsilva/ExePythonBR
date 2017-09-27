nota = 0
cont = 0
v = []
soma = 0
conts = 0
while nota != -1:
	nota = int(input('Digite a nota '))
	if nota != -1:
		v.append(nota)
		soma += nota
		cont += 1
		if nota < 7:
			conts += 1

print('A. Quantidade de valores lidos foram {} '.format(cont))
print('B. Ordem que foram informados {} '.format(v))
#v.reverse() reverte usando modulo
#print('Ordem inversa {} '.format(v)) #v[::-1]))

conti = len(v)
print('C. Ordem inversa')
while conti > 0:
	conti -= 1
	print('{} '.format(v[conti]))
print('D. Soma dos valores {} '.format(soma))

media = soma/cont
print('E. Media dos valores {} '.format(media))

contm = 0
contb = 0
for i in range(len(v)):
	if v[i] > media:
		contm += 1
print('F. Quantidade de valores acima da media {} '.format(contm))

print('G. Quantidade de valores abaixo de sete {} '.format(conts))

print('H. Fim do Programa')
