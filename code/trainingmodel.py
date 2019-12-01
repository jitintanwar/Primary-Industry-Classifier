
from bd_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from time import time
from sklearn import tree
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier

features_train, features_test, labels_train, labels_test = preprocess()

clf = RandomForestClassifier(n_estimators=40)
clf.fit(features_train, labels_train)
y_pred = clf.predict(features_test)
print(accuracy_score(labels_test, y_pred))
