import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def bar(data):
	hasil = panda(data)

	labels, counts = np.unique(hasil["Sentiment"], return_counts=True)
	plt.bar(labels, counts, align='center')
	plt.gca().set_xticks(labels)
	return hasil,plt
def panda(df):
	df = pd.DataFrame(data=df, columns=['ID','Nama','Tweet','Tanggal','Sentiment'])
	return df