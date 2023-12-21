import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# load the dataset
data = pd.read_excel('otu1.xlsx')

# convert left/right to 0/1
le = LabelEncoder()
data['Class'] = le.fit_transform(data['Sample1'])  # 0: Left, 1: Right

# split dataset into feature target
X = data.iloc[:, 1:]
y = data['Class']

# training dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=0)

# train Gaussian Naive Bayes model
model = GaussianNB()
model.fit(X_train, y_train)

# use cross validation
scores = cross_val_score(model, X_train, y_train, scoring='accuracy', cv=5)
print('Cross-validated scores:', scores)

# accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print('Accuracy:', accuracy)

# confusion matrix
confusion = confusion_matrix(y_test, predictions)
print('Confusion matrix: ')
print(confusion)

# sensivity and specificity
sensitivity = confusion[1, 1] / (confusion[1, 0] + confusion[1, 1])
specificity = confusion[0, 0] / (confusion[0, 0] + confusion[0, 1])
print('   Sensitivity:', sensitivity)
print('   Specificity:', specificity)
