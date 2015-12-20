import csv

print "How far do you want to run?" 
distance = raw_input(" 5K, 10K, 15K, 1mile (1M) 5miles (5M), 10miles (10M), 13.1M (1/2 marathon), 26.2M (full marathon), 20K, 30K, 50K")

with open('2016Runs.csv', 'rb') as csvfile:
    runs2016_raw = csv.DictReader(csvfile, delimiter=',', quotechar='|')

    for row in runs2016_raw:
        if distance in row['Distance']:
            print row['Date'], row['Location']
        # print row['Date']
        # print row['Distance']
        # print row['Name']
        # print row['Location']

        