import csv
from os import write
import default
import datetime
import time
import sys
import hashlib
#import main

def client_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    
    #user_data = data_clients[login_index]
    title = user_data[2] + ", welcome back"
    menu = ["Profile Settings", "Rent a car", "View Personal Rental History", "Update Password","Exit"]
    #print(user_data)
    while(1):
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5'):
                break
        
        if(choice == '1'):
            profile_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        elif(choice == '2'):
            rentcar_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        elif(choice == '3'):
            view_indhistory(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        elif(choice == '4'):
            update_password(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        elif(choice == '5'):
            title = user_data[2] + ", you have successfully log out."
            default.print_title(title)
            print("")
            return 

def profile_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):    
        print("\n")
        for i in range(2,9):
            if(i ==3):
                continue
            print(data_clients[0][i] + ": " + user_data[i])
    
        menu = ["Edit", "Return"]
    
        while(1): 
            print("\n")   
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
                
            print("Error!")
    
        if(choice == '1'):
            edit_profile(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        elif(choice == '2'):
            return
        
def edit_profile(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    print("\nWhat do you want to edit?")
    menu = ["Name", "Date of Birth", "License", "Phone Number", "Email", "Card", "Return"]
    
    while(1):
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7'):
            break
    if(choice == '7'):
        return
    
    
    if(choice == '1'):
        temp = default.validation_length(space_clients[2])
        user_data[2] = temp
    
    elif(choice == '2'):
        temp = default.validation_date()
        user_data[4] = temp
       
    elif(choice == '3'):
        temp = default.validation_length(space_clients[5])
        user_data[5] = temp    
    
    elif(choice == '4'):
        temp = default.validation_number(space_clients[6])
        user_data[6] = temp
    
    elif(choice == '5'):
        temp = default.validation_email(space_clients[7])
        user_data[7] = temp

    elif(choice == '6'):
        temp = default.validation_number(16)
        user_data[8] = temp
    
    
        
    data_clients[login_index] = user_data
    
    #print(data_clients)
    
    with open("./data/clients.csv",  mode = 'w', newline = '') as clients_file:
        write = csv.writer(clients_file)
        write.writerows(data_clients)
        
    return
        
def rentcar_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):    
        menu = ["View All Available Cars", "Search for a  Car", "Book a Car","Return"]
        title = user_data[2] + ", do you want to rent a car?"
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4'):
                break
        
        if(choice == '1'):
            default.print_table(data_carlist, 4, space_cars, login_index)
            view_allcars(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        if(choice == '2'):
            searchcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        if(choice == '3'):
            bookcar_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
        if(choice == '4'):
            return

def view_allcars(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):
        menu = ["Sort the List", "Return"]
        while(1):
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
    
        if(choice == '1'):
            sortcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            
        elif(choice == '2'):
            return
        
def sortcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):
        menu = ["Car ID", "Car Types", "Car Brand", "Model Year", "Price per Hour", "Passenger Capacity","Weight Load","Return"]
        title = user_data[2] + ", you can sort the list here"
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice =='2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8'):
                break
    
        if(choice == '8'):
            return
        
        if(choice == '1'):
            header = "Car ID"
            sequence = sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '2'):
            header = "Car Types"
            sequence = sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '3'):
            header = "Car Brand"
            sequence = sub_sort_menu(header, data_carlist, 2)
    
        if(choice == '4'):
            header = "Model Year"
            sequence = sub_sort_menu(header, data_carlist, 2)
    
        if(choice == '5'):
            header = "Price per Hour"
            sequence = sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '6'):
            header = "Passenger Capacity"
            sequence = sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '7'):
            header = "Weight Load"
            sequence = sub_sort_menu(header, data_carlist, 2)
    
        
        default.print_sorttable(data_carlist, 4, sequence, space_cars)
        print("")
        
            
        
    
def sub_sort_menu(header, data, mode):
    sub_menu = ["Ascending", "Descending"]
    title = "You have chosen " + header + ": "
    while(1):
        default.print_title(title)
        default.general_menu(sub_menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2'):
            break
        
    if(choice == '1'):
        sequence = default.sort_data(data, header, 1, mode)
    
    elif(choice == '2'):
        sequence = default.sort_data(data, header, 0, mode)
        
    return sequence
            
def searchcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):
        menu = ["Car ID", "Car Types", "Car Brand", "Car Model", "Passenger Capacity","Weight Load","Return"]
        title = user_data[2] + ", you can search a car here"
        sequence = []
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice =='2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7'):
                break   
        
        if(choice == '1'):
            header = "Car ID"
            sequence = sub_search_menu(header, data_carlist, 2)
        
        if(choice == '2'):
            header = "Car Types"
            sequence = sub_search_menu(header, data_carlist, 2)
        
        if(choice == '3'):
            header = "Car Brand"
            sequence = sub_search_menu(header, data_carlist, 2)
    
        if(choice == '4'):
            header = "Car Model"
            sequence = sub_search_menu(header, data_carlist, 2)
    
        if(choice == '5'):
            header = "Passenger Capacity"
            sequence = sub_search_menu(header, data_carlist, 2)
        
        if(choice == '6'):
            header = "Weight Load"
            sequence = sub_search_menu(header, data_carlist, 2)
        
        if(choice == '7'):
            return
        
        
        default.print_sorttable(data_carlist, 4, sequence, space_cars)
        print("")
    
        
def sub_search_menu(header, data, mode):
    title = "You have chosen " + header + ": "     
    
    default.print_title(title)
    keyword = input("Please enter your keyword: ")
    print("")
    sequence = default.search_data(data, keyword, header, mode)
    
    return sequence

def view_indhistory(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    title = user_data[2] + ", view your rental history here"
    default.print_table(data_transactions, 5, space_transactions, user_data[0])
    print("")
    menu = ["Return"]
    while(1):
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1'):
            break
    
    if(choice == '1'):
        return
    
def update_password(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    title = user_data[2] + ", change your password here."
    menu = ["Change My Password", "Return"]
    while(1):
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2'):
            break
    
    if(choice == '2'):
        return
    
    i = 0
    while(i < 3):
        old_password = input("Please enter your old password: ")
        hash_object = hashlib.md5(old_password.encode())
        md5_hash = hash_object.hexdigest()
        old_password = md5_hash
        if(old_password == user_data[3]):
            break
        
        else:
            print(str(3-i-1) + " attempts are left.")
        i = i + 1
        print("")
            
    if(i == 3):
        return
        
    
    new_password = default.validation_length(space_clients[3])
    hash_object = hashlib.md5(new_password.encode())
    md5_hash = hash_object.hexdigest()
    new_password = md5_hash
    user_data[3] = new_password
    data_clients[login_index] = user_data
    
    with open("./data/clients.csv",  mode = 'w', newline = '') as clients_file:
        write = csv.writer(clients_file)
        write.writerows(data_clients)
        
def bookcar_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    while(1):
        title = user_data[2] + ", you can book a car here"
        menu = ["Book with Car ID", "Return"]
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please select: ")
            if(choice == '1' or choice == '2'):
                break
    
        if(choice == '1'):
            bookcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
    
        if(choice == '2'):
            return

def select_date(header, user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    title = user_data[2] + ", select your time here"
    i = 0
    while(1):
        print(header)
        print("Please enter date in DD-MM-YYYY")
        temp = input("Date: ")
        try:
            datetime.datetime.strptime(temp, "%d-%m-%Y")
            break
        except ValueError:
             print("Error! Incorrect date format.")
             i = i + 1
        if(i > 4):
            menu = ["Continue", "Return"]
            while(1):
                default.general_menu(menu)
                choice = input("Please Select: ")
                if(choice == '1' or choice == '2'):
                    break
            if(choice == '1'):
                return 1
            if(choice == '2'):
                return 2
                   
            
    #print(from_date)
    return temp
        
def select_time(title, user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    i = 0
    while(1):
        print(title)
        print("Please enter time in HH:MM")
        temp = input("Time: ")
        try:
            datetime.datetime.strptime(temp, "%H:%M")
            break
        except ValueError:
             print("Error!")
             i = i + 1
               
        if(i > 4):
            menu = ["Continue", "Return"]
            while(1):
                default.general_menu(menu)
                choice = input("Please Select: ")
                if(choice == '1' or choice == '2'):
                    break
            if(choice == '1'):
                return 1
            if(choice == '2'):
                return 2
            
    return temp
    
    return temp
    #print(from_time)
        
def bookcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    data = []
    time = []
    index = -2
    sum = 0
    k = 0
    while(1):
        car_id = input("Please input the car ID: ")
        
        for i in range(len(data_carlist)):
            if(car_id == data_carlist[i][0]):
                index = i
                break
        
        if(index == i):
            break
        print("Car ID doesn't exists!")
        k = k + 1
        if(k > 4):
            menu = ["Continue","Return"]
            while(1):
                default.general_menu(menu)
                choice = input("Please Select: ")
                if(choice == '1' or choice == '2'):
                    break
            
            if(choice == '1'):
                bookcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
                
            if(choice == '2'):
                return
            
            return
            
        
    data.append(user_data[0])
    data.append(user_data[2])
    for i in range(4):
        data.append(data_carlist[index][i])
    data.append(data_carlist[index][9])
    
    while(1):   
        while(1):
            from_date = select_date("From: ", user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            print("")
            if(from_date == 1):
                pass
            elif(from_date == 2):
                return
            else:
                break
    
        #print(from_date)
    
        while(1):
            from_time = select_time("From: ", user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            print("")
            if(from_time == 1):
                pass
            elif(from_time == 2):
                return
            else:
                break
    
        #print(from_time)
 
#GEtting to time

    
        while(1):
            to_date = select_date("To: ", user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            print("")
            if(to_date == 1):
                pass
            elif(to_date == 2):
                return
            else:
                break
    
        #print(to_date)
    
        while(1):
            to_time = select_time("To: ", user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            print("")
            if(to_time == 1):
                pass
            elif(to_time == 2):
                return
            else:
                break
    
        #print(to_time)
    
        #print(data)
        
        from_datetime = datetime.datetime.strptime(from_date + " " + from_time, "%d-%m-%Y %H:%M")
        to_datetime = datetime.datetime.strptime(to_date + " " + to_time, "%d-%m-%Y %H:%M")
        from_date = from_datetime.strftime("%d-%m-%Y")
        from_date = from_datetime.strftime("%H:%M:%S")
        to_date = to_datetime.strftime("%d-%m-%Y")
        to_time = to_datetime.strftime("%H:%M:%S")
        
        now_datetime = datetime.datetime.now()
        now_date = now_datetime.strftime("%d-%m-%Y")
        now_time = now_datetime.strftime("%H:%M:%S")

        #print(from_datetime)
        #print(to_datetime)
        
        if(from_datetime < to_datetime and now_datetime < from_datetime):
            total_hours = to_datetime - from_datetime
            #print(total_hours)
            total_hours = round(total_hours.total_seconds() / 3600, 2)
            
            total_price = round(total_hours * int(data[6]), 2)
            
            data.append(from_date)
            data.append(from_time)
            data.append(to_date)
            data.append(to_time)
            data.append(now_date)
            data.append(now_time)
            data.append(str(total_hours))
            data.append(str(total_price))
            
            choice = confirm_booking(data_transactions[0], data)
            if(choice == 1):
                data_transactions.append(data)
                with open("./data/transactions.csv", mode = "w", newline = "") as transactions_file:
                    write = csv.writer(transactions_file)
                    write.writerows(data_transactions)
                    
            if(choice == 2):
                return
            break
        
        else:
            print("You can only book a date for a period in the future.")
    return
            
def confirm_booking(headers, data):
    title = "Booking Details"
    print("")
    
    menu = ["Confirm Booking", "Return"]
    while(1):
        default.print_title(title)
        print("")
        
        for i in range(15):
            print(headers[i] + ": " + str(data[i]))
            
        print("")
        print("The total amount to pay is: RM" + data[14])
            
        print("")
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2'):
            break
            
    if(choice == '1'):
        print("Payment is successful!")
        for remaining in range(5, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("Will be directed in {:2d}......".format(remaining)) 
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\n")
        return 1
        
    if(choice == '2'):
        return 2

        
        
        
            
    
    
       
    
        
    
    
    
        
        

    
    
    
    
    
        
        
    

        

    

    

        
        
        
            
    
    

          
    
    
    
    
    
    