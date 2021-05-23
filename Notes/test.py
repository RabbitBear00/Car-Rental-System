# Python 3 code to demonstrate the 
# working of MD5 (byte - byte)
  
import hashlib
import csv
from io import StringIO
  
# encoding GeeksforGeeks using md5 hash
# function 
result = hashlib.md5(b'444')
  
# printing the equivalent byte value.
temp = str(result.digest())
print(temp)



with open("./data/new.csv", mode = "w", newline="") as new:
    write = csv.writer(new)
    write.writerow(temp)