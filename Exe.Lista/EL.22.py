lista = []
quant = [0,0,0,0]
soma = 0
v=[]
while True:
  numIdent = int(input("Digite o numero de indentificação do mouse: "))
  if numIdent == 0:
      break
  print("1 - para necessita de esfera\n2 - para necessita de limpeza")
  print("3 - para necessita troca do cabo ou conector \n4 - para quebra ou inutilizado")
  tipo = int(input("Digite o tipo de defeito: "))
  lista.append([numIdent,tipo])
  print()

while len(lista) > 0:
 for x,i in enumerate(lista):
     cont=0
     l=lista[:]
     for c,j in enumerate(l):
        if i[1] == j[1] :
           cont+=1
           lista.remove(j)
     soma += cont
     if cont > 0:
        if i[1] == 1:
           quant[0]=cont
        elif i[1] == 2:
           quant[1]=cont
        elif i[1] == 3:
           quant[2]=cont
        elif i[1] == 4:
           quant[3]=cont
med1 = quant[0]/soma
med2 = quant[1]/soma
med3 = quant[2]/soma
med4 = quant[3]/soma
print("Quantidade de mouses: {}".format(len(l)))
print("Situação                       Quantidade           Percentual")
print("1 - necessita de esfera                 {}                 {:.2f} %".format(quant[0],med1))
print("2 - necessita de limpesa                {}                 {:.2f} %".format(quant[1],med2))
print("3 - necessita troca do cabo ou conector {}                 {:.2f} %".format(quant[2],med3))
print("4 - tipo de defeito                     {}                 {:.2f} %".format(quant[3],med4))
