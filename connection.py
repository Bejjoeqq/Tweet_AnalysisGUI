import sqlite3
def insert(hasil):
	connection = sqlite3.connect('tweet.db')
	crud_query = "INSERT INTO data(tweet_id,screen_name,tweet_text,tanggal) VALUES(?,?,?,?);"
	cursor = connection.cursor()

	y=0
	z=0
	for x in hasil:
		try:
			cursor.execute(crud_query,x)
			y+=1
		except:
			z+=1
	connection.commit()
	cursor.close()
	connection.close()
	return f"Pesan : {y} data di tambahkan dan {z} data sudah ada dalam database."
def select(query):
	connection = sqlite3.connect('tweet.db')
	cursor = connection.cursor()
	cursor.execute(query)

	hasil =  cursor.fetchall()

	cursor.close()
	connection.close()
	return hasil
def update(data):
	connection = sqlite3.connect('tweet.db')
	cursor = connection.cursor()

	y=0
	for x in data:
		crud_query = f"Update data set sentimen = {x[4]} where tweet_id = {x[0]}"
		cursor.execute(crud_query)
		y+=1

	connection.commit()
	cursor.close()
	connection.close()

	if y>0:
		return f"Pesan : {y} data di update."
	else:
		return "Pesan : Semua data sudah di analisis"