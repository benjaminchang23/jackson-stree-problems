import csv

csv_data = "time, some.thing, third.column, fourth\n10, 3, name, -0.5"

for row in csv.reader([csv_data]):
    print(row)