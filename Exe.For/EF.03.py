nome = 'nome'
idade = 0
salario = 1
sexo = 'm'
estado_civil = 'a'
while len(nome) >= 4 and  idade < 150 and salario > 0 and sexo == 'f' or sexo == 'm' or (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v'or estado_civil =='d'):
        nome = str.lower(input('Informe o nome (maior que 3 caracteres): '))
        idade = int(input('Digite a idade (menor que 150): '))
        salario = float(input('Digte o salário (maior que 0): '))
        sexo = str(input('Informe o sexo (f/m): '))
        estado_civil = str(input('Informat o estado civil (s/c/v/d): '))
        
