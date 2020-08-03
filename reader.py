#!/usr/bin/env python
# conda execute
# env:
#  - python >=3
#  - pandas
import csv
with open('innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)