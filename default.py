import datetime
import hashlib
import time 
import sys

        
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
    with open("./data/clients.txt") as csv_file:
        for line in csv_file:
            temp = line.strip().split(",")
            data.append(temp)
            
    return data
        

#Reading datas from file and storing it in an array
def input_datacars():
    data_cars = []
    with open("./data/cars_lists.txt") as csv_file:
        for line in csv_file:
            temp = line.strip().split(",")
            data_cars.append(temp)
            
        
    return data_cars

#Reading datas from file and storing it in an array
def input_datatransactions():
    data = []
    with open("./data/transactions.txt") as csv_file:
        for line in csv_file:
            temp = line.strip().split(",")
            data.append(temp)
            
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

# register interface is for the unregister clients
def register_interface(data_clients, space_clients):
    print_title("You can register here")
    prev_id = data_clients[-1][0]
   
    while(1):
        sign = 0
        data = []
        id = int(prev_id) + 1
        data.append(id)
        data.append("Normal")
        print("Plase enter your Username")
        name = validation_length(space_clients[2])
        
        i = 0
        for i in range(len(data_clients)):
            if(name == data_clients[i][2]):
                print("This username has been used. ")
                print("")
                sign = 1
                break
        if(sign == 1):
            continue
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
            k = 0 
            for i in data:
                data[k] = str(i)
                k = k + 1
            data_clients.append(data)
            #print(data)
            with open("./data/clients.txt", mode = 'w') as clients_file:
                for line in data_clients:
                    temp = ",".join(line)
                    clients_file.write(temp + '\n')
            
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

            
            
    
#It is a menu to direct into login/unregister and exit
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

#Use to print all the tables
def print_table(data, mode, space, login_name = ""):
    rows = len(data)
    start = 1
    if(mode == 1):
        #mode 1: admin view clients table(all columns can be viewed)
        columns = 11
        start = 2
        blanks = 180
        
    elif(mode == 2):
        #mode 2: admin view cars table(all columns can be viewed)
        columns = 13
        blanks = 214
        
    elif(mode == 3 or mode == 5):
        #mode 3: admin view transactions table(all columns can be viewed)
        #mode 5: client view transactions table(view their own transactions only)
        columns = 19
        blanks = 299
        
    elif(mode == 4):
        #mode 4: client view cars table(four columns of quantity and columis not included)
        columns = 13
        blanks = 143
    
    elif(mode == 6):
        #mode 6: unregistered client view car table(Car ID, Car type, Car Brand, Car Model)
        columns = 4
        blanks = 61
    
    elif(mode == 7 or mode == 8):
        #mode 7: admin wanted to filter transactions details using specific client ID 
        #mode 8: admin wanted to filter transactions details using specific client name 
        columns = 19
        blanks = 299
    
    #Section for printing headers
    k = 0 
    for i in data[0]:
        #skip four columns of quantity
        if(mode == 4 and (i == "Total Quantity" or i == "Available" or i == "Unavailable" or i == "In Service" )):
            k = k + 1
            continue
        #skip the fourth column till the last column
        if(mode == 6 and (k >= 4 and k <= 12)):
            k = k + 1
            continue
        #skip password column
        if(mode == 1 and k == 3):
            k = k + 1
            continue
        
        print(i + " " * (int(space[k]) - int(len(i))) + " | ", end = "")
        k = k + 1
    
    #printing the "-----------" line seperator between headers and data    
    print("")
    print("-" * blanks)
    
    
    #printting the data
    for i in range(start,rows):#user variable start to skip clients.csv first row of admin data
        
        for k in range(columns):
            
        #Skipping columns
            #skip four columns of quantity
            if(mode == 4 and (k == 5 or k == 6 or k ==7 or k == 8)):
                continue
            
            #skip transactions for others
            if(mode == 5 and data[i][0] != login_name):
                continue
            
            #skip transactions for other client ID
            if(mode == 7 and data[i][0] != login_name):
                continue
            
            #skip transaction for other client names
            if(mode == 8 and data[i][1] != login_name):
                continue
            
            #skip password column for admin
            if(mode == 1 and k == 3):
                continue

            print(str(data[i][k]) + " " * (int(space[k]) - int(len(str(data[i][k])))) + " | ", end = "")
        
        #skipping rows
        if((mode == 5 and data[i][0] != login_name) or (mode == 7 and data[i][0] != login_name) or (mode == 8 and data[i][1] != login_name)):
            pass
        else:
            print("")

#print tables according to a given sequence
def print_sorttable(data, mode, sequence, space):
    
    if(mode == 1):
        #mode 1: admin sort list of clients
        columns = 11
        blanks = 180
        
    elif(mode == 2):
        #mode 2: admin sort list of cars(include all columns)
        columns = 13
        blanks = 180
        
    elif(mode == 3):
        #mode 3: admin filter certain dates of transactions
        columns = 19
        blanks = 302
        
    elif(mode == 4):
        #mode 4: client sort list of cars(exclude four columns of quantity)
        columns = 13
        blanks = 143
    
    #insert headers row inside the sequence               
    sequence.insert(0, 0)
    
    for i in sequence:
        for k in range(columns):
            #skipping columns
            if(mode == 4 and (k == 5 or k == 6 or k ==7 or k == 8 )):
                continue

            if(mode == 1 and k == 3):
                continue
            
                
            print(data[i][k] + " " * (int(space[k]) - int(len(data[i][k]))) + " | ", end = "")
                
        if(i == 0):
            print("")
            print("-" * blanks, end = "")
                
        print("")

#sorting data according to target, with ascending(order == 1) & descending(order == 0)           
def sort_data(data, target, order, mode):
    #skipping headers line in data
    start = 1
    count = 1    

    #mode 1: skipping the header and admin line in clients.csv
    #mode 2: mainly for car lists
    if(mode == 1):
        start = 2
        count = 2
    sample = []
    index = 0
    rows = len(data)
    #finding certain column equals to target
    for i in data[0]:
        if(i == target):
            break
        index = index + 1
     
     #append the whole column(target column) inside sample
    for i in range(start, rows):
        sample.append(data[i][index])
        
    len_sample = len(sample)
    
    #giving values to sequence accordance to the row number
    sequence = [*range(start, len_sample+count, 1)]
    
    #if the values in the column, turns out to be numbers, it must be converted to integers to compare the sizes
    if(mode == 2 and ((index >=5 and index <=9) or index == 12 or index == 13)):
        for i in range(len(sample)):
            sample[i] = int(sample[i])
        
    #Changing sequence and sample at the same time, so when it's done we know the ascending/descending sequence with the variable 'sequence'
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
    
    #return the sequence of how it sorts and later printed via print_sorttabble           
    return sequence

#searching "keyword" in "data" list of "attribute" column
def search_data(data, keyword, attribute, mode):
    start = 1
    #skipping the admin line if want to search for clients
    if(mode == 1):
        start = 2
    sequence = []
    sample = []
    rows = len(data)
    #convert keyword to lower case so the search is not case sensitive
    keyword = keyword.lower()
    
    #fingding the respective index of attribute
    k = 0
    for i in data[0]:
        if attribute == i :
            index = k
        k = k + 1        
    
    #append everything in the attribute column into sample         
    for i in range(start, rows):
        sample.append(data[i][index])
        
    #turning every element in sample to lower case
    for i in range(len(sample)):
        sample[i] = sample[i].lower()
    
    #checking if it matches with the sequence
    i = 0
    for i in range(len(sample)):
        if keyword in sample[i]:
            sequence.append(i)
    

    
    #mode 1: everything have to add 2 to make the row number exact to how it shows in clients list    
    if(mode == 1):
        sequence = [x + 2 for x in sequence]
    #mode 2: add 1 to skip headers
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
            print("You can only enter " + "at most " + str(length) +" digit of numbers" )
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
        
            
            
 #If total quantity is different than previous      
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
                
#If total quantity is the same as previous
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

#Ensuring the temp return is capitalised in the first alphabet and small for the rest
def validation_carnormal(target):
    
    temp = input("Please enter " + str(target) +": ")
    
    temp = temp[0].upper() + temp[1:len(temp)].lower()
    return temp