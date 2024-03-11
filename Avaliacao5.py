n = int(input())
wine = []

while n != -1:
	if n == 1:
		name = input()
		wine_type = input()
		amount = int(input())
		
		wine.append([name, wine_type, amount])
		
	elif n == 2:
		name = input()
		aux = 0
		for i in range(len(wine)):
			if wine[i][0] == name:
				print(wine[i][1])
				print(wine[i][2])
				aux = 1
		if not aux:
			print("Nao cadastrado")
	
	elif n == 3:
		wine_type = input()
		amount = 0
		for i in range(len(wine)):
			if wine[i][1] == wine_type:
				amount += wine[i][2]
		
		if amount:
			print(amount)
		else:
			print("Nao cadastrado")
	
	elif n == 4:
		amount = 0
		for i in range(len(wine)):
			amount += wine[i][2]
		print(amount)
	
	else:
		print("Invalido")
	
	n = int(input())