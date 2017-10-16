string1 = input("String: ")
string2 = input("string: ") 
print("Tamanho de {} {}".format(string1,len(string1)))
print("Tamanho de {} {}".format(string2,len(string2)))
if len(string1) == len(string2):
	print("As duas string são do mesmo tamanho")
elif len(string1) > len(string2):
	print("String1 é maior que string2")
else:
	print("String2 é maior que string1")

if string1 == string2:
	print("As duas string tem o mesmo conteudo")
else:
	print("As duas string são diferente")
