__author__ = 'meril'

import csv

inputFile = []  #List to store rows of the csv file

#Reading csv file and storing into list
with open('New_York_City_Leading_Causes_of_Death.csv', 'rb') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        inputFile.append(row)

print inputFile
