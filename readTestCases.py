import csv

def readTrainingFile(filepath):
    fieldnames=[]
    with open('FieldNames.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in csvreader:
            fieldnames.append(row[0])
    print(fieldnames)

    with open(filepath, newline='') as csvfile:
        trainingSetReader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in trainingSetReader:
            print(row)






if __name__ == "__main__":
    readTrainingFile("SmallTrainingSet.csv")