import pandas
import numpy as np
import heapq


fileName ="data_in_numeric_form.csv"


data= pandas.read_csv(fileName)

#data
features = [2,3,4,5,6]
label = 1
data_mat = data.values[:,1:]
print(data_mat)
pivot = int(len(data_mat)*.8)
X_tr = data_mat[:pivot,features].astype(np.int)
Y_tr = data_mat[:pivot,label].astype(np.int)
X_test = data_mat[pivot:,features].astype(np.int)
Y_test = data_mat[pivot:,label].astype(np.int)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
#clf = KNeighborsClassifier(n_neighbors=5)
#clf = GaussianNB()
#clf = tree.DecisionTreeClassifier(max_depth = 20)
clf = RandomForestClassifier(n_estimators=100, max_depth=2,random_state=0)
#clf = svm.SVC(gamma=0.001, decision_function_shape='ovo', max_iter=2)
#print(type(X_tr[0][0]))
clf.fit(X_tr, Y_tr)


testNum = 5
highestProbabN = 40
probab = clf.predict_proba(X_test[testNum].reshape(1, -1))[0]
maxIndex = np.argsort(probab)[::-1][:highestProbabN]
print("Max idx",probab[maxIndex])
print(clf.classes_[maxIndex])
print(X_test[testNum])
print(Y_test[testNum])



temp = np.where((X_test[:,0] == X_test[testNum][0]) & (X_test[:,1] == X_test[testNum][1]))
print(temp)
y_ = Y_test[temp]
np.where(y_==5149)



### for decision tree

