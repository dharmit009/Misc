import numpy as np
import csv

# opens the csv file in read-only mode.
with open('winequality-red.csv', 'r') as f:  
    wines = list(csv.reader(f,delimiter=';'));


quality = [(float(eachRow[-1])) for eachRow in wines[1:]]; # creates a list of quality 

averageQuality = sum(quality)/len(quality);
print("Average Quality Of Wine: ", averageQuality); 
