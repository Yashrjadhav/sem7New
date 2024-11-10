import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix ,accuracy_score ,recall_score ,f1_score ,precision_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

df=pd.read_csv("diabetes.csv")
df.info()

x=df.iloc[:,:-1]
y=df.iloc[:,-1]

x_train ,x_test , y_train, y_test =train_test_split(x,y,test_size=0.20, random_state=8)

knn=KNeighborsClassifier()
knn.fit(x_train ,y_train)
knn_pred =knn.predict(x_test)

conf=confusion_matrix(y_test,knn_pred)
acc=accuracy_score(y_test, knn_pred)
recall=recall_score(y_test,knn_pred)
f1=f1_score(y_test, knn_pred)
error_rate=1-acc
prec=precision_score(y_test,knn_pred)

print(conf)
print(acc)
print(recall)
print(f1)
print(error_rate)
print(prec)

plt.figure(figsize=(8,6))
sns.heatmap(conf,annot=True , cmap='Blues' ,fmt='d', xticklabels=['No Diabetes' ,'Diabetes'] ,yticklabels=['No Diabetes', 'Diabetes'])
plt.xlabel("actual")
plt.ylabel("predicted")
plt.show()