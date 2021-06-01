import csv
import datetime
import hashlib
import time 
import sys
import clients

        
#First menu -startup menu
def startup_menu(main_title):
    print_title(main_title)
    menu = ["Registered", "Unregistered","Exit"]
    general_menu(menu)
    choice = input("Please Select: ")
    
    return choice
    

#login menu for existing users, returning username and password for checking later
def login_menu(main_title):
    lists = []
    print_title(main_title)
    username = input("Username/ID: ")
    password = input("   Password: ")
    lists.append(username)
    lists.append(password)
    
    return lists

#Reading datas from file and storing it in an array
def input_dataclients():
    data = []
    with open("./data/clients.csv") as csv_file:
        read = csv.reader(csv_file, delimiter = ',')
        for row in read:
            data.append(row)
            
    return data
        

#Reading datas from file and storing it in an array
def input_datacars():
    data_cars = []
    with open("./data/cars_lists.csv") as csv_file:
        read = csv.reader(csv_file, delimiter = ',')
        for row in read:
            data_cars.append(row)
        
    return data_cars

#Reading datas from file and storing it in an array
def input_datatransactions():
    data = []
    with open("./data/transactions.csv") as csv_file:
        read = csv.reader(csv_file, delimiter = ',')
        for row in read:
            data.append(row)
        
    return data 
    
#Check password if it is correct
def check_password(data, username, password):
    rows = len(data)
    #MD5 hash encoding
    hash_object = hashlib.md5(password.encode())
    md5_hash = hash_object.hexdigest()
    password = md5_hash
    #loop to see if it matches username/id and password 
    for i in range(1, rows):
        if(username == data[i][0]):
            if(password == data[i][3]):
                login_index = i
                return login_index
        if(username == data[i][2]):
            if(password == data[i][3]):
                login_index = i
                return login_index
        
    return 0
    
    
#check Username/ID if it is correct
def check_usernameID(data, username):
    rows = len(data)
    for i in range(1, rows):
        #Check ID
        if(username == data[i][0]):
            return 1
        
        #Check username
        if(username == data[i][2]):
            return 1
    
    return 0 

#print all major titles for super car rental system
def print_title(title):
    print("================================================================")
    print(" " * int((64-len(title))/2) + title)
    print("================================================================")

#Widely use function, input list, and then this function will generate a list accordingly with numbers 1-xxx,2-xxx,3-xxx
def general_menu(list):
    length = len(list)
    for i in range(length):
        print(str(i+1), "-", list[i])
        
    print("\n")

#The login interface that checks and hints of a user login in
def login_interface(main_title, data_clients, data_carlist, space_cars, space_clients):
    
    i = 0 
    while(1):
        login_details = login_menu(main_title)
        username_key = check_usernameID(data_clients, login_details[0])
        password_key = check_password(data_clients, login_details[0], login_details[1])
    
        if(username_key == 1 and password_key >= 1):
            print("You have successfully login!")
            break
    
        elif(username_key == 1 and password_key == 0):
            print("Wrong password. Failed to login.")

        else:
            print("Username does not exist. Failed to login.")
        
        i = i + 1
        if(i > 4):
            break
        
    #If tried for 5 times, this will appear and offer a route to escape the current page and return to startup_interface
    if(i > 4):
        menu = ["Continue","Return"]
            
        while(1):
            general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
            
        #If continue, recursion
        if(choice == '1'):
            password_key = login_interface(main_title, data_clients, data_carlist, space_cars, space_clients)
            return password_key
            
        if(choice == '2'):
            login_index = startup_interface(main_title, data_clients, data_carlist, space_cars, space_clients)
            return login_index
            
    return password_key
                        
                    
#Interface for the unregistered to register as clients
def unregistered_interface(data_clients, data_carlist, space_cars,space_clients):
    title = "Guest, Welcome to Super Car Rental System"
    menu = ["Register", "View Available Cars", "Return"]
    while(1):
        print_title(title)
        general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2' or choice == '3'):
            break
        
    if(choice == '1'):
        register_interface(data_clients, space_clients)
        
    if(choice == '2'):
        print_table(data_carlist, 6, space_cars)
        print("")
        while(1):
            menu = ["Return"]
            general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1'):
                break
        if(choice == '1'):
            return
            
    if(choice == '3'):
        return
            
def register_interface(data_clients, space_clients):
    print_title("You can register here")
    prev_id = data_clients[-1][0]
   
    while(1):
        data = []
        id = int(prev_id) + 1
        data.append(id)
        data.append("Normal")
        print("Plase enter your Username")
        name = validation_length(space_clients[2])
        print("")
        data.append(name)
        while(1):
            print("Plase enter your password")
            password_1 = validation_length(space_clients[3])
            print("")
            print("Please confirm your password")
            password_2 = validation_length(space_clients[3])
            if(password_1 == password_2):
                hash_object = hashlib.md5(password_1.encode())
                md5_hash = hash_object.hexdigest()
                password_1 = md5_hash
                data.append(password_1)
                break
            else:
                print("The password you enter are not the same. Please try again")
                print("")
            
        print("")
        
        print("Please enter your date of birth: ")
        birth_date = validation_date()
        print("")
        data.append(birth_date)
        
        print("Please enter your license: ")
        license = validation_length(space_clients[5])
        print("")
        data.append(license)
        
        print("Please enter your phone number: ")
        phone = validation_number(space_clients[6])
        print("")
        data.append(phone)
        
        print("Please enter your email: ")
        email = validation_email(space_clients[7])
        print("")
        data.append(email)
        
        print("Please enter your credit/debit card number: ")
        card = validation_number(12)
        print("")
        data.append(card)
        data.append(0)
        data.append(0)
        
        
        print_title("Confirm Registeration Details")
        k = 0
        for i in data:
            if(k == 3):
                k += 1
                continue
                
            print(data_clients[0][k] + ": " + str(i))
            k += 1
            
        menu = ["Confirm", "Return"]
        while(1):
            general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
        
        if(choice == '1'):
            data_clients.append(data)
            #print(data)
            with open("./data/clients.csv", mode = 'w', newline = "") as clients_file:
                write = csv.writer(clients_file)
                write.writerows(data_clients)
            
            print_title("Registeration information has successfuly recorded.")
            for remaining in range(5, -1, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Will be directed in {:2d}......".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\n")
            return
        
        if(choice == '2'):
            return                

            
            
    

def startup_interface(main_title, data_clients, data_carlist, space_cars, space_clients):
    
    while(1):
        while(1):
            choice = startup_menu(main_title)
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4'):
                break  
                     
        if(choice == '1'):
            login_index = login_interface(main_title, data_clients, data_carlist, space_cars, space_clients)
            return login_index
    
        elif(choice == '2'):
            unregistered_interface(data_clients, data_carlist, space_cars, space_clients)

        elif(choice == '3'):
            for remaining in range(5, 0, -1):
                sys.stdout.write("\r")
                sys.stdout.write("System will exit in {:2d}.............".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)
        
            exit()
    
def print_table(data, mode, space, login_name = ""):
    rows = len(data)
    start = 1
    if(mode == 1):
        #space = space_clients
        columns = 11
        start = 2
        blanks = 180
        
    elif(mode == 2):
        #space = space_cars
        columns = 13
        blanks = 183
        
    elif(mode == 3 or mode == 5):
        #space = space_transactions
        columns = 19
        blanks = 302
        
    elif(mode == 4):
        #space = space_cars
        columns = 13
        blanks = 143
    
    elif(mode == 6):
        #space = space_cars
        columns = 4
        blanks = 61
    
    elif(mode == 7 or mode == 8):
        #space = space_transactions
        columns = 19
        blanks = 302
        
    k = 0 
    for i in data[0]:
        if(mode == 4 and (i == "Total Quantity" or i == "Available" or i == "Unavailable" or i == "In Service" or i == "Status" )):
            k = k + 1
            continue
        if(mode == 6 and (k >= 4 and k <= 12)):
            k = k + 1
            continue
        
        if(mode == 1 and k == 3):
            k = k + 1
            continue
        
        print(i + " " * (int(space[k]) - int(len(i))) + " | ", end = "")
        k = k + 1
        
    print("")
    print("-" * blanks)
    
    
  
    for i in range(start,rows):
        for k in range(columns):
            if(mode == 4 and (k == 5 or k == 6 or k ==7 or k == 8)):
                continue
            if(mode == 4 and data[i][8] == "Unavailable"):
                continue
            
            if(mode == 5 and data[i][0] != login_name):
                continue
            
            if(mode == 7 and data[i][0] != login_name):
                continue
            if(mode == 8 and data[i][1] != login_name):
                continue
            
            if(mode == 1 and k == 3):
                continue

            print(str(data[i][k]) + " " * (int(space[k]) - int(len(str(data[i][k])))) + " | ", end = "")
        
        #if(i == 0):
        #    print("")
        #    print("-" * blanks, end = "")
        if((mode == 4 and data[i][8] == "Unavailable") or (mode == 5 and data[i][0] != login_name) or (mode == 7 and data[i][0] != login_name) or (mode == 8 and data[i][1] != login_name)):
            pass
        else:
            print("")
                
def print_sorttable(data, mode, sequence, space):
    
    if(mode == 1):
        #space = space_clients
        columns = 11
        blanks = 180
        
    elif(mode == 2):
        #space = space_cars
        columns = 13
        blanks = 180
        
    elif(mode == 3):
        #space = space_transactions
        columns = 19
        blanks = 302
        
    elif(mode == 4):
        #space = space_cars
        columns = 13
        blanks = 143
    
                   
    sequence.insert(0, 0)
    
    for i in sequence:
        for k in range(columns):
            if(mode == 4 and (k == 5 or k == 6 or k ==7 or k == 8 )):
                continue
            if(mode == 4 and data[i][8] == "Unavailable"):
                continue
            if(mode == 1 and k == 3):
                continue
            
                
            print(data[i][k] + " " * (int(space[k]) - int(len(data[i][k]))) + " | ", end = "")
                
        if(i == 0):
            print("")
            print("-" * blanks, end = "")
                
        if(mode == 4 and data[i][8] == "Unavailable"):
            pass
        else:
            print("")
            
def sort_data(data, target, order, mode):
    start = 1
    count = 1    

    if(mode == 1):
        start = 2
        count = 2
    sample = []
    index = 0
    columns = len(data[0])
    rows = len(data)
    for i in data[0]:
        if(i == target):
            break
        index = index + 1
     
    for i in range(start, rows):
        sample.append(data[i][index])
        
    len_sample = len(sample)
    
    sequence = [*range(start, len_sample+count, 1)]
    
    if(mode == 2 and ((index >=5 and index <=9) or index == 12 or index == 13)):
        for i in range(len(sample)):
            sample[i] = int(sample[i])
        
    
    #Descending
    if(order == 0):
        for i in range(len_sample -1):
            for k in range(0, len_sample-i-1):
                if (sample[k] < sample[k+1]):
                    sample[k], sample[k+1] = sample[k+1], sample[k]
                    sequence[k], sequence[k+1] = sequence[k+1], sequence[k]
    
    #Ascending           
    elif(order == 1):
        for i in range(len_sample -1):
            for k in range(0, len_sample-i-1):
                if (sample[k] > sample[k+1]):
                    sample[k], sample[k+1] = sample[k+1], sample[k]
                    sequence[k], sequence[k+1] = sequence[k+1], sequence[k]
                
    return sequence

def search_data(data, keyword, attribute, mode):
    start = 1
    if(mode == 1):
        start = 2
    sequence = []
    sample = []
    rows = len(data)
    columns = len(data[0])
    keyword = keyword.lower()
    k = 0
    for i in data[0]:
        if attribute == i :
            index = k
        k = k + 1        
             
    for i in range(start, rows):
        sample.append(data[i][index])
        
    #print(index)
    for i in range(len(sample)):
        sample[i] = sample[i].lower()
    
    
    i = 0
    for i in range(len(sample)):
        if keyword in sample[i]:
            sequence.append(i)
    

    
    #print(sample)    
    if(mode == 1):
        sequence = [x + 2 for x in sequence]
    else:
         sequence = [x + 1 for x in sequence]
    #print(sequence)
    
    return sequence

def validation_length(length):
    length = int(length)
    while(1):
        temp = input("Please enter : ")
        if(len(temp) <=length):
            return temp
        else:
            print("You cannot exceed " + str(length) + " characters" )
            print("")

def validation_number(length):
    length = int(length)
    while(1):
        temp = input("Please Enter : ")
        
        if temp.isdecimal() == True and len(temp) <= length:
            return temp
        else:
            print("You can only enter " + str(length) +" digit of numbers" )
            print("")

def validation_email(length):
    length = int(length)
    while(1):
        temp = input("Please Enter : ")
        
        if "@" in temp and ".com" in temp:
            break
        else:
            print("Email format not correct" )
            print("")
            
    while(1):
        if len(temp) <= length:
            break
        else:
            print("You cannot exceed " + str(length) + " characters" )
            print("")
            temp = input("Please Enter : ")
            
    return temp
def validation_date():
    
    while(1):
        print("Please enter date in DD-MM-YYYY")
        temp = input("Please Enter : ")
        try:
            date = datetime.datetime.strptime(temp, "%d-%m-%Y")
            birth = date.strftime("%d-%m-%Y")

            return birth
        
        except ValueError:
            print("Error! Incorrect date format")    
            print("")
            
def validation_totalquantity(data_carlist, car_data, mode = 1):

    while(1):
        print("Total Quantity = Available + Unavailable + In Service")
        print("You can only input upto 4 positive digits")
        print("")
        try:
            temp = int(input("What is the total quantity now? :"))
            if temp < 0:
                print("You cannot enter negative digits")
                print("Please enter again!")
                print("")
                continue
            
            if len(str(temp)) > 4:
                print("You cannot exceed 4 digits")
            
        except ValueError:
            print("You can only enter upto 4 positive integers. ")
            print("Please enter again")
            print("")
            continue
        if(mode == 2):
            car_data = sub_total_quantity_menu2(temp, car_data)
            break
            
        elif(temp > int(car_data[5])):
            car_data = sub_total_quantity_menu1(temp, car_data, 1)
            print_title("This is the current record.")
            for i in range(0,13):
                print(data_carlist[0][i] + ": " + str(car_data[i]))    
            break
            
        elif(temp < int(car_data[5])):
            car_data = sub_total_quantity_menu1(temp, car_data, 0)
            print_title("This is the current record.")
            for i in range(0,13):
                print(data_carlist[0][i] + ": " + str(car_data[i]))    
            break
        
        else:
            print("Total Quantity is the same as before")
            print("Do you want to alter quantity for each section? ")
            menu = ["Yes", "Return"]
            while(1):
                general_menu(menu)
                choice = input("Please Select: ")
                if(choice == '1' or choice == '2'):
                    break
            
            if(choice == '1'):
                car_data = sub_total_quantity_menu2(temp, car_data)
                print_title("This is the current record.")
                for i in range(0,13):
                    print(data_carlist[0][i] + ": " + str(car_data[i])) 
            
            return car_data             
    
    return car_data    
        
            
            
        
 #order == 1, larger than previours; order ==0, smaller than previous   
def sub_total_quantity_menu1(temp, car_data, order):
    count = abs(temp - int(car_data[5]))
    if order == 1:
        title = "added"
        
    if order == '2':
        title = "deleted"
    while(1):
        print("You have " + str(title) + " " + str(count) + " cars into the total quantity for car ID: " + str(car_data[0]))
        print("Available + Unavailable + In Service = " + str(count))
        print("Please enter the quantity for each section below: ")
        print("")
        
        try:
            num1 = int(input("Available  : ")) 
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
            
        if(len(str(num1)) <= 4 and num1 >=0 and num1 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue    
                
        try:
            num2 = int(input("Unavailable: ")) 
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
        
        if(len(str(num2)) <= 4 and num2 >=0 and num2 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue    
                
        if(num1 + num2 > count):
            print("The total for three sections cannot exceed " + str(count))
            print("Please enter again!")
            print("")
            continue
                        
        try:
            num3 = int(input("In Service : ")) 
            
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
        
        if(len(str(num3)) <= 4 and num3 >=0 and num3 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue       
                
        if(num1 + num2 + num3 > count):
            print("The total for three sections cannot exceed " + str(count))
            print("Please enter again!")
            print("")
            continue
        print("")
        break
                
    while(1):
        print("Do you confirm the following changes: ")
        print("Available     : " + str(num1))
        print("Unavailable   : " + str(num2))
        print("In Service    : " + str(num3))
                
        menu = ["Confirm", "Return"]
        general_menu(menu)
        choice = input("Please select: ")
        if(choice == '1' or choice == '2'):
            break
                
    if(choice == '1'):
        car_data[5] = temp
        car_data[6] = int(car_data[6]) + num1
        car_data[7] = int(car_data[7]) + num2
        car_data[8] = int(car_data[8]) + num3          
                    
    return car_data
                
def sub_total_quantity_menu2(temp, car_data):
    count = int(temp)
    while(1):
        print("Please reenter the quantity for 'Available', 'Unavailable', 'In Service'.")
        print("Available + Unavailable + In Service = Total Quantity")
        print("The total quantity now is: " + str(temp))
        
        try:
            num1 = int(input("Available  : ")) 
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
            
        if(len(str(num1)) <= 4 and num1 >=0 and num1 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue    
                
        try:
            num2 = int(input("Unavailable: ")) 
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
        
        if(len(str(num2)) <= 4 and num2 >=0 and num2 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue    
                
        if(num1 + num2 > count):
            print("The total for three sections cannot exceed " + str(count))
            print("Please enter again!")
            print("")
            continue
                        
        try:
            num3 = int(input("In Service : ")) 
            
        except ValueError:
            print("You can only enter integers")
            print("Please enter again")
            print("")
            continue
        
        if(len(str(num3)) <= 4 and num3 >=0 and num3 <= count):
            pass
        else:
            print("You can only enter a 4 digit of positive integer not larger than " + str(count))
            print("Please enter again!")
            print("")
            continue       
                
        if(num1 + num2 + num3 > count):
            print("The total for three sections cannot exceed " + str(count))
            print("Please enter again!")
            print("")
            continue
        print("")
        break
                
    while(1):
        print("Do you confirm the following changes: ")
        print("Total Quantity: " + str(temp))
        print("Available     : " + str(num1))
        print("Unavailable   : " + str(num2))
        print("In Service    : " + str(num3))
                
        menu = ["Confirm", "Return"]
        general_menu(menu)
        choice = input("Please select: ")
        if(choice == '1' or choice == '2'):
            break
                
    if(choice == '1'):
        car_data[5] = temp
        car_data[6] = num1
        car_data[7] = num2
        car_data[8] = num3          
                    
    return car_data

def validation_cartypes():
    
    while(1):
        print("You can only enter: City, Electric, Prestige, Van, Truck")    
        print("")
        temp = input("Please enter car type: ")
        temp.lower()
        if temp == 'city' or temp == 'electric' or temp == 'prestige' or temp == 'van' or temp == 'truck':
            break
                
    temp = temp[0].upper() + temp[1:len(temp)]
    return temp          

def validation_carnormal(target):
    
    temp = input("Please enter " + str(target) +": ")
    
    temp = temp[0].upper() + temp[1:len(temp)].lower()
    return temp