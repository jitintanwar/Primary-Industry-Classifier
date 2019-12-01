import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

def preprocess(bd_file = '../data/bd_data.pkl', ic_file = '../data/ic_data.pkl'):
	
	bd_file_handler = open(bd_file, 'r')
	bd = pickle.load(bd_file_handler)
	bd_file_handler.close()

	ic_file_handler = open(ic_file, 'r')
	ic = pickle.load(ic_file_handler)
	ic_file_handler.close()

	# split the data for training(90%) and testing(10%), test_size is the percentage of events assigned to the test set
	features_train, features_test, labels_train, labels_test = train_test_split(bd, ic, test_size=0.1, random_state=42)

	# text vectorization--go from strings to lists of numbers
	vectorizer = TfidfVectorizer(norm = 'max', sublinear_tf=True, max_df=0.5, stop_words='english')
	features_train_transformed = vectorizer.fit_transform(features_train)
	features_test_transformed  = vectorizer.transform(features_test)

	# feature selection, because text is super high dimensional and can be really computationally chewy as a result
	# selector = SelectPercentile(f_classif, percentile=0.3)
	# chi2 is the scoring function.
	selector = SelectKBest(chi2, k=500)
	# print(selector)
	selector.fit(features_train_transformed, labels_train)
	features_train_transformed = selector.transform(features_train_transformed).toarray()
	features_test_transformed  = selector.transform(features_test_transformed).toarray()

	print('preprocessing done.')

	return features_train_transformed, features_test_transformed, labels_train, labels_test


# preprocess()