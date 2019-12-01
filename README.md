Supervised multi-class classification problem.

Step 1 (Have to be performed manually)
performed in code/datacleaning.py

	Cleaning the data in excel file.
		Removed rows that has IC as 0 (1570/48601), unidentified column(14)
		Removed rows that had BD(423) = '-'
		

Step 2 (takes ~110 secs)
performed in code/stemmingtext.py, code/vectorizetext.py

	Cleaning the Business Descriptions.

		Remove punctuations and digits from the text.
		Stemming (stemmingtext.py)
			stemmer = SnowballStemmer("english")
	    Store cleaned BDs as a pickle object.

Step 3 
	Preprocessing the data (bd_preprocess.py)
		Read pickle files
		Split the data into training and test sets
		Apply TFIDF-Vectorization (Term Frequency Inverse Document Frequency) on text data(training and test features)

step 4
	Apply ML classification algo to solve.
