def getSentiment(data):
	hasil = [list(x) for x in data]
	pos_list= open("./kata_positif.txt","r")
	pos_kata = pos_list.readlines()
	neg_list= open("./kata_negatif.txt","r")
	neg_kata = neg_list.readlines()

	for y,x in enumerate(data):
		count_p = 0
		count_n = 0
		for kata_pos in pos_kata:
			if kata_pos.strip() in x[2]:
				count_p +=1
		for kata_neg in neg_kata:
			if kata_neg.strip() in x[2]:
				count_n +=1
		sentiment = count_p - count_n
		hasil[y][4] = str(sentiment)
	return hasil
def prettify(data):
	print("")
	maxxx = str(len(data))
	maxx=0
	for x in data:
		if len(x[0])>maxx:
			maxx = len(x[0])
	for y,x in enumerate(data,start=1):
		row = maxx - len(x[0])
		rows = x[0]+(" "*row)
		num = len(maxxx) - len(str(y))
		nums = str(y) + (" "*num)
		if y==1:
			print("-"*160)
			print(f"|  {' '*(len(maxxx)-1)} | Nama{' '*(maxx-4)} | Tanggal{' '*12} | Tweet")
			print("-"*160)
		print(f"| {nums} | {rows} | {x[1]} | {x[2]}")
	print("-"*160)