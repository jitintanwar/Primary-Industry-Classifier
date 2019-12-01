from stemmingtext import parseOutText
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

df = pd.read_excel('../data/clean_data.xlsx')

# print(df.head())

temp_counter = 0
bd_data = []
ic_data = []

# months_list = ['january', 'june']
# stop_words = ['compani', 'limited', 'public', 'subsidiaries', 'manufactur', '']

for index, row in df.iterrows():
	# print(row['IC'])
	# temp_counter += 1
	bd = parseOutText(str((row['BusinessDescription'])).encode('utf-8'))	
	bd_data.append(bd)
	ic_data.append(row['Category'])

print("business descriptions are processed.")

pickle.dump( bd_data, open("../data/bd_data.pkl", "w"))
pickle.dump( ic_data, open("../data/ic_data.pkl", "w"))