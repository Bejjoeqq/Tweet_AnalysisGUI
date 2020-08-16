from tkinter import *
from tkinter.ttk import *
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo

import pandas as pd
import numpy as np
from twitter import getTweet
from connection import *
from analysis import *
from plot import bar
# from tkinter import ttk
class tgui(Tk):
	def __init__(self):
		super().__init__()
		self.title("Tampilan GUI")
		self.geometry("800x390")

		#~~~~~~~~~~~~~~~~Label~~~~~~~~~~~~~~~~~~~
		lbl_title = Label(self, text="Tweet Analysis Using Tweepy", font=("Helvetica", 11),background = 'green', foreground ="white")
		# lbl_title.grid(row=0, column=0, pady = (10,5), padx=(49,0))
		lbl_title.pack(pady=5)

		lbl_menu = Label(self, text="1. Update Data\n2. Update Nilai Sentiment\n3. Lihat Data\n4. Visualisasi")
		# lbl_menu.grid(row=1, column=0, sticky = W, pady = 2, padx=(5,0))
		lbl_menu.pack(pady=2)

		lbl_input = Label(self, text="Pilih Program : ")
		# lbl_input.grid(row=2, column=0, sticky = W, pady = 2, padx=(5,0))
		lbl_input.pack(pady=2)


		#~~~~~~~~~~~~~~~~Cbox~~~~~~~~~~~~~~~~~~~
		n = StringVar()
		cbx_input = Combobox(self, width = 5,state="readonly",textvariable = n)
		cbx_input['values'] = ("1","2","3","4")
		cbx_input.current(0)
		# print(n)
		# cbx_input.grid(row = 2, column = 5, sticky = W, pady = 2)
		cbx_input.pack()


		#~~~~~~~~~~~~~~~~Entry~~~~~~~~~~~~~~~~~~~
		# txt_input = Entry(self, width=5)
		# # txt_input.grid(row = 2, column = 1, sticky = W, pady = 2, padx=(0,0))
		# txt_input.pack(pady=2)



		#~~~~~~~~~~~~~~~~Button~~~~~~~~~~~~~~~~~~~
		btn_submit = Button(self, text="Go !",command = lambda:self.btn(cbx_input.get()))
		# btn_submit.grid(row=3, column=0, sticky = W, pady = 2, padx=(5,0))
		btn_submit.pack(pady=2)




		#~~~~~~~~~~~~~~~~TView~~~~~~~~~~~~~~~~~~~
		self.tree = Treeview(self)
		# tree.grid(row = 5, column = 0,pady = 2, padx=5)
		self.updt()

	def updt(self,fdate=[[0],[0],[0]],ldate=[[0],[0],[0]]):
		q = f"SELECT screen_name,tanggal,tweet_text FROM data WHERE tanggal BETWEEN '{fdate[0]}-{fdate[1]}-{fdate[2]}' AND '{ldate[0]}-{ldate[1]}-{ldate[2]}';"
		data = select(q)
		self.df = pd.DataFrame(data=data, columns=['Nama','Tweet','Tanggal'])
		# df = pd.DataFrame(sample)
		self.cols = list(self.df.columns)
		self.tree.pack_forget()
		self.tree.pack(pady=2)
		self.tree.delete(*self.tree.get_children())
		self.tree["columns"] = self.cols

		#remove first column
		# self.tree['show'] = 'headings'

		self.tree.column('#0',minwidth=50, width=50)

		for x,i in enumerate(self.cols):
			size=120
			if x==2:
				size = 550
			self.tree.column(i, anchor='w',minwidth = size, width = size)
			self.tree.heading(i, text=i, anchor='w')

		for index, row in self.df.iterrows():
			self.tree.insert('','end',text=index,values=list(row))
	def btn(self,n):
		if n=="1":
			# print("tes")
			jmlh = askstring(':)', 'Banyak data')
			hasil = getTweet(int(jmlh))
			pesan = insert(hasil)
			showinfo(':)',pesan)
		elif n=="2":
			q = "SELECT * FROM data WHERE sentimen IS NULL;"
			data = select(q)
			dataSentiment = getSentiment(data)
			pesan = update(dataSentiment)
			showinfo(':)',pesan)
		elif n=="3":
			fdate = askstring(':)', 'Tanggal awal (format: yyyy-mm-dd)')
			fdate = fdate.split("-",3)
			ldate = askstring(':)', 'Tanggal akhir (format: yyyy-mm-dd)')
			ldate = ldate.split("-",3)
			self.updt(fdate,ldate)
		elif n=="4":
			q = "SELECT * FROM data WHERE sentimen IS NOT NULL;"
			data = select(q)
			hasil,plt = bar(data)
			showinfo(':)',f'Nilai rata-rata: {np.mean(hasil["Sentiment"])}\nNilai median: {np.median(hasil["Sentiment"])}\nStandar deviasi: {np.std(hasil["Sentiment"])}')
			plt.show()
