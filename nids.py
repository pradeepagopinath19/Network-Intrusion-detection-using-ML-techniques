#import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import csv


# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = csv.reader(file)
    data_set = list(lines)
    return data_set


def do_knn():
    train_path = "C:\\Users\\vdha3\\Documents\\Prac\\kdd\\KDDTrain+.csv"
    field_path = "C:\\Users\\vdha3\\Documents\\Prac\\kdd\\Field_Names.csv"
    field_names = load_csv(field_path)
    fields = [i[0] for i in field_names]
    dataset = pd.read_csv(train_path, names=fields)
    X = dataset.iloc[:, 4:39].values
    Y = dataset.iloc[:, 40].values
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    do_knn()


