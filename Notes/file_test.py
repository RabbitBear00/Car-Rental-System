with open("./Notes/new.txt", mode = "r") as new_file:
    data = []
    print(type(new_file))
    for i in new_file:
        temp = i.strip().split(",")
        data.append(temp)
        
print(data)
print(data[0][2])

temp = ["sdsdsdsdaahhahhahs", "afgagagga", "agaggagaga"]
data.append(temp)
print(data)


with open("./Notes/new.txt", mode = "w") as f:
    
    print(type(data))
    for i in data:
        temp = ",".join(i)
        f.write(temp +'\n')
            