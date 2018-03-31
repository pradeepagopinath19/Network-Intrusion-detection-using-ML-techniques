import numpy as np
import csv


# Load a CSV file
def load_csv(filename):
    file = open(filename, "r")
    lines = csv.reader(file)
    data_set = list(lines)
    return data_set

def get_data():
    fname = "C:\\Users\\vdha3\\Documents\\Prac\\kdd\\KDDTrain+.csv"
    data = load_csv(fname)
    print(data)

if __name__=='__main__':
    get_data()


