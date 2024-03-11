mapa = [
		["I", "O", "O", "X"],
		["X", "3", "O", "1"],
		["X", "X", "2", "X"]]

ant_i = 0
ant_j = 0

atual_i = 0
atual_j = 0

while True:
	n = input().strip()
	
	possible = ["D", "E", "C", "B"]
	if n not in possible:
		print("E")
		break
	
	temp_i = atual_i
	temp_j = atual_j

	if n == "D":
		atual_j = atual_j + 1
	
	elif n == "E":
		atual_j = atual_j - 1
	
	elif n == "C":
		atual_i = atual_i - 1
	
	elif n == "B":
		atual_i = atual_i + 1
		
	if atual_i == ant_i and atual_j== ant_j:
		print("V")
		break
		
	elif mapa[atual_i][atual_j] == "X":
		print("X")
		break
		
	elif mapa[atual_i][atual_j] == "1":
		print("P1")
		break
		
	elif mapa[atual_i][atual_j] == "2":
		print("P2")
		break
	
	elif mapa[atual_i][atual_j] == "3":
		print("P3")
		break

