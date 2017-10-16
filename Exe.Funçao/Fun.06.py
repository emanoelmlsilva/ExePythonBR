def conve24Para12(a,b):
	if a > 12 and b <= 60:
		a-=12
		print("{}:{} pm".format(h,b))
	elif a <= 12 and b <= 60:
		print("{}:{} am".format(a,b))
	else:
		print("Forma de minuto invalida")

a,b=map(int,input("Hora Minutos: ").split())
while a != 0:
	conve24Para12(a,b)
	a,b=map(int,input("Hora Minutos: ").split())
