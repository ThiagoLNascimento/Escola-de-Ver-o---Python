text = input().lower()
text = text.replace(";", "")
text = text.replace(".", "")
text = text.replace(",", "")
text = text.split("_")
words = input().split("_")

while True:
    try:
        text.remove("")
    except ValueError:
        break

print(len(text))

for i in words:
	quant = 0
	for j in text:
		if i.lower() == j:
			quant += 1
			
	if quant > 0:
		print(i + " "  + str(quant))