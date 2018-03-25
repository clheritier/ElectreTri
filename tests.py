import csv

import csv
with open("test2.csv") as csvfile:
    reader = csv.reader(csvfile,delimiter=';')
    for row in reader:
        print(row)

