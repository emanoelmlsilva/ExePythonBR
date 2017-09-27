lista = list(range(5))
id = []
alt = []

for i in range(len(lista)):
	print('pessoa {}'.format(i+1))
	idade = int(input('Digite a idade: '))
	id.append(idade)
#	id[i] = idade
	altura = float(input('Digite a altura: '))
	alt.append(altura)
#	alt[i] = altura

print('===============')

id.reverse() #invertendo lista
alt.reverse() #invertendo lista
print('idade: {}'.format(id))
print('altura: {}'.format(alt))
#print('idade: {}'.format(id[::-1])) outra forma de inverter
#print('altura: {}'.format(alt[::-1]))
## ou tambem x = lis(id[::-1]

