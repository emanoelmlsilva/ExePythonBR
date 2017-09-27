l = [[123,1],[565,1],[6576,2]]
num = int(input())
print(len(l))
for i in range(len(l)):
	if num == l[i][1]:
		print( l[i])

