import csv

path = 'F:/PROGRAMMING/Networks/CNF_Week_2/CNF_Week_2/'

file=open( path +"data.CSV", "r")
reader = csv.reader(file)
for line in reader:
    t=line[0], line[1],line[2]
    print(t)