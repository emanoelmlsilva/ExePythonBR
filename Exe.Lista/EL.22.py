lista = []
listaQuant = []
while True:
  numIdent = int(input("Digite o numero de indentificação do mouse: "))
  if numIdent == 0:
      break
  print("1 - para necessita de esfera\n2 - para necessita de limpeza")
  print("3 - para necessita troca do cabo ou conector \n4 - para quebra ou inutilizado")
  tipo = int(input("Digite o tipo de defeito: "))
  lista.append([numIdent,tipo])
  print()

l=lista[:]
for x, i in enumerate(lista):
    cont=0
    l = lista[:]
    for c, j in enumerate(l):
        if i[1] == j[1] :
            cont+=1
            l.remove(j)
    listaQuant.append(cont)
print(listaQuant)


"""print("Quantidade de mouses: {}".format(len(lista)))
print("Situação                       Quantidade           Percentual")
print("1 - necessita de esfera                 {}                  %".format(listaQuant[0]))
print("2 - necessita de limpesa                {}                  %".format(listaQuant[1]))
print("3 - necessita troca do cabo ou conector {}                  %".format(listaQuant[2]))
print("4 - tipo de defeito                     {}                  %".format(listaQuant[3]))"""
