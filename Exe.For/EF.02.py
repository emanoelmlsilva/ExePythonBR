nome = 's'
senha = 's'
while nome == senha:
	nome = str.lower(input('Nome de usuario: '))
	senha = str.lower(input('Senha: '))
	if nome == senha:
		print('invalido')
		print('============================')
		print('informe novamente seus dados')
