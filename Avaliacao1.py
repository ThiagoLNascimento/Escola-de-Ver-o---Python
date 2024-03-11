i = 0

while (i < 3):
	n = int(input())
	if (n > 99999 or n < 10000):
		print(False)
		i = i + 1
		continue
	
	fifth = n % 10
	n = n // 10
	forth = n % 10
	n = n // 10
	third = n % 10
	n = n // 10
	second = n % 10
	n = n // 10
	first = n % 10
	
	if ((((second ** 4) % 3) != 0) or (((forth ** 4) % 3) != 0 )):
		print(False)

	
	elif (third == 1 or third == 0):
		print(False)

		
	elif (third + fifth <= 3):
		print(False)

	
	elif (first != 2 and first != 5 and first != 9):
		print(False)
	
	else:
		print(True)
		
	i = i + 1