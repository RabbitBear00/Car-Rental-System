import csv
import hashlib

with open("./Data/new.csv",'rb')  as file:
    with open("./Data/Hashed.csv",'w')  as output:
        for line in file: 
           line=line.strip() 
           print(line)
           print(hashlib.md5(line).hexdigest()) 
           output.write(hashlib.md5(line).hexdigest() +'\n')