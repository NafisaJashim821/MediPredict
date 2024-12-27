import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import joblib

data = pd.read_csv('./dataset/training.csv')

X = data.drop('prognosis', axis=1)  
y = data['prognosis']

clf_DT = DecisionTreeClassifier()
clf_knn=KNeighborsClassifier()
clf_RF=RandomForestClassifier()
clf_NB=GaussianNB()


clf_DT.fit(X, y)
clf_knn.fit(X, y)
clf_RF.fit(X, y)
clf_NB.fit(X, y)

joblib.dump(clf_DT, 'trained_models/DTmodel.pkl')
joblib.dump(clf_knn, 'trained_models/KNNmodel.pkl')
joblib.dump(clf_RF, 'trained_models/RFmodel.pkl')
joblib.dump(clf_NB, 'trained_models/NBmodel.pkl')
print("Model trained and saved successfully")
