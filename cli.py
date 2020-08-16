
from twitter import getTweet
from connection import *
from analysis import *
from plot import bar
import numpy as np
import os,sys
def cls():
	if os.name=="nt":
		os.system("cls")
	else:
		os.system("clear")
	print("Tweet Analysis Using Tweepy")
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━")
def tcli():
	cls()
	exit=False
	print("Tampilan CLI, Selamat Datang :)")
	input("Enter...")
	while True:
		try:
			cls()
			print("1. Update Data\n2. Update Nilai Sentiment\n3. Lihat Data\n4. Visualisasi\n5. Exit")
			n=int(input("\nPilih Program : "))
			if n==1:
				cls()
				hasil = getTweet(int(input("Banyak data : ")))
				print(insert(hasil))
				input("\nEnter...")
			elif n==2:
				cls()
				q = "SELECT * FROM data WHERE sentimen IS NULL;"
				data = select(q)
				dataSentiment = getSentiment(data)
				print(update(dataSentiment))
				input("\nEnter...")
			elif n==3:
				cls()
				fdate = list(map(str, input("Tanggal awal (format: yyyy-mm-dd) : ").split("-")))
				ldate = list(map(str, input("Tanggal akhir (format: yyyy-mm-dd) : ").split("-")))
				q = f"SELECT screen_name,tanggal,tweet_text FROM data WHERE tanggal BETWEEN '{fdate[0]}-{fdate[1]}-{fdate[2]}' AND '{ldate[0]}-{ldate[1]}-{ldate[2]}';"
				data = select(q)
				prettify(data)
				input("\nEnter...")
			elif n==4:
				cls()
				q = "SELECT * FROM data WHERE sentimen IS NOT NULL;"
				data = select(q)
				hasil,plt = bar(data)
				print("Nilai rata-rata: "+str(np.mean(hasil["Sentiment"])))
				print("Nilai median: "+str(np.median(hasil["Sentiment"])))
				print("Standar deviasi: "+str(np.std(hasil["Sentiment"])))
				plt.show()
				input("\nEnter...")
			elif n==5:
				exit=True
				sys.exit()#the way to except
		except Exception as e:
			print(e);input()
			if exit==True:
				sys.exit()