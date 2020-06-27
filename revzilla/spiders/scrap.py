import csv

bins = [1,2,3,4,5,]
frequencies = [232,232,3123,14,21]
with open('some.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(zip(bins, frequencies))