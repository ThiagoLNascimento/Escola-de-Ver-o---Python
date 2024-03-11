dist = int(input())
fuel = int(input())

for i in range(1, dist + 1):
	pairs_sum = 1
	
	for j in range(i):
		if j % 2 == 0:
			pairs_sum += j
	
	fuel_need = dist / pairs_sum
	
	fuel = fuel - fuel_need
	if fuel <= 0:
		break

	print(str(i) + " " + str(int(fuel)))