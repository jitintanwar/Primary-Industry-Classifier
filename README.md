It is a Supervised multi-class classification problem where the solution deals in identifying the primary industry of a company by reading the business description. It involves data cleaning, preprocessing of text, removing noiose from the data etc. Following steps were performed in building the solution.

*Step 1* (Have to be performed manually)
performed in code/datacleaning.py

	Cleaning the data in excel file.
	Removed rows that has IC as 0 (1570/48601), unidentified column(14)
	Removed rows that had BD(423) = '-'
		

*Step 2* (takes ~110 secs)
performed in code/stemmingtext.py, code/vectorizetext.py

	Cleaning the Business Descriptions.
	Remove punctuations and digits from the text.
	Store cleaned BDs as a pickle object.

*Step 3* 
Preprocessing the data (bd_preprocess.py)

	Read pickle objects
	Split the data into training and test sets
	Apply TFIDF-Vectorization (Term Frequency Inverse Document Frequency) on text data(training and test features)
	Cleaning the Business Descriptions.
	Remove punctuations and digits from the text.
	Store cleaned BDs as a pickle object.
*Step 4*

	Apply ML classification algorithms to solve the problem.
