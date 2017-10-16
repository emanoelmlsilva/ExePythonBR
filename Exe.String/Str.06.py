lista =["Janeiro","Fevererio","Março","Abril","Maior","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
d,m,a = map(int,input("Data de Nascimento: : ").split())
print("Você nasceu em {} de {} de {}".format(d,lista[m-1],a))

