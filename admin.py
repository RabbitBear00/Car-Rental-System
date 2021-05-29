import default
import clients
import datetime
import csv
import sys
import time

def admin_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions):
    title = user_data[2] + ", welcome back"
    menu = ["View All Clients", "View All Cars", "View All Transactions", "Car Return","Log Out"]
    #print(user_data)
    while(1):
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5'):
                break
        
        if(choice == '1'):
            client_interface(user_data, data_clients, login_index, space_clients)
            pass
            
        elif(choice == '2'):
            car_interface(user_data, data_carlist, login_index, space_cars)
            pass
        elif(choice == '3'):
            #transaction_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            pass
        
        elif(choice == '4'):
            #returncar_interface(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
            pass
        
        elif(choice == '5'):
            title = user_data[2] + ", you have successfully log out."
            default.print_title(title)
            print("")
            return 
        
def client_interface(user_data, data_clients, login_index, space_clients):
    while(1):    
        menu = ["Sort", "Search", "Return"]
        title = user_data[2] + ", what do you want to do?"
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2' or choice == '3'):
                break
        
        if(choice == '1'):
            default.print_table(data_clients, 1, space_clients, login_index)
            sortclient_menu(user_data, data_clients, space_clients)
            
        if(choice == '2'):
            searchclient_menu(user_data, data_clients, space_clients)
            
        if(choice == '3'):
            return

def sortclient_menu(user_data, data_clients, space_clients):
    while(1):
        menu = ["User ID", "Status", "Name", "Email", "Points","Return"]
        title = user_data[2] + ", you can sort the list here"

        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice =='2' or choice == '3' or choice == '4' or choice == '5' or choice == '6'):
                break

        
        if(choice == '1'):
            header = "User ID"
            sequence = clients.sub_sort_menu(header, data_clients, 1)
        
        if(choice == '2'):
            header = "Status"
            sequence = clients.sub_sort_menu(header, data_clients, 1)
        
        if(choice == '3'):
            header = "Name"
            sequence = clients.sub_sort_menu(header, data_clients, 1)
    
        if(choice == '4'):
            header = "Email"
            sequence = clients.sub_sort_menu(header, data_clients, 1)
    
        if(choice == '5'):
            header = "Points"
            sequence = clients.sub_sort_menu(header, data_clients, 1)
        
        if(choice == '6'):
            return
    
        
        default.print_sorttable(data_clients, 1, sequence, space_clients)
        print("")
        
def searchclient_menu(user_data, data_clients, space_clients):
    while(1):
        menu = ["User ID", "Status", "Name", "License", "Phone Number", "Email", "Return"]
        title = user_data[2] + ", you can search a client here"
        sequence = []
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice =='2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7'):
                break   
        
        if(choice == '1'):
            header = "User ID"
            sequence = clients.sub_search_menu(header, data_clients, 1)
        
        if(choice == '2'):
            header = "Status"
            sequence = clients.sub_search_menu(header, data_clients, 1)
        
        if(choice == '3'):
            header = "Name"
            sequence = clients.sub_search_menu(header, data_clients, 1)
    
        if(choice == '4'):
            header = "License"
            sequence = clients.sub_search_menu(header, data_clients, 1)
    
        if(choice == '5'):
            header = "Phone Number"
            sequence = clients.sub_search_menu(header, data_clients, 1)
        
        if(choice == '6'):
            header = "Email"
            sequence = clients.sub_search_menu(header, data_clients, 1)
        
        if(choice == '7'):
            return
        
        
        default.print_sorttable(data_clients, 1, sequence, space_clients)
        print("")
        
def edit_carprofile(user_data, data_clients, login_index, space_clients):
    print("\nWhat do you want to edit?")
    menu = ["Car Types", "Car Brand", "Car Model", "Model Year", "Total Quantity", "Available", "Unavailable", "In Service", "Price per Hour", "Fuel Type", "Return"]
    
    while(1):
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8' or choice == '9' or choice == '10' or choice == '11'):
            break
    if(choice == '11'):
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
    
    elif(choice == '7'):
        temp = default.validation_email(space_clients[7])
        user_data[7] = temp

    elif(choice == '8'):
        temp = default.validation_number(16)
        user_data[8] = temp
        
    elif(choice == '9'):
        temp = default.validation_email(space_clients[7])
        user_data[7] = temp

    elif(choice == '10'):
        temp = default.validation_number(16)
        user_data[8] = temp   
        
    data_clients[login_index] = user_data
    
    #print(data_clients)
    
    with open("./data/clients.csv",  mode = 'w', newline = '') as clients_file:
        write = csv.writer(clients_file)
        write.writerows(data_clients)
        
    return

def car_interface(user_data, data_carlist, login_index, space_cars):
    while(1):    
        menu = ["Sort All Cars", "Search for a  Car", "Edit Car Details","Add a car", "Return"]
        title = user_data[2] + ", what would you like to do"
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5'):
                break
        
        if(choice == '1'):
            default.print_table(data_carlist, 2, space_cars, login_index)
            sort_cars(user_data, data_carlist, space_cars)
        
        if(choice == '2'):
            clients.searchcar_menu(user_data, data_carlist, space_cars)
        
        if(choice == '3'):
            carprofile_menu(data_carlist, space_cars)
            pass  
        
        if(choice == '4'):
            addcar_menu(data_carlist, space_cars)
            pass
        if(choice == '5'):
            return
    
def sort_cars(user_data, data_carlist, space_cars):
    while(1):
        menu = ["Car ID", "Car Types", "Car Brand", "Model Year", "Price per Hour", "Passenger Capacity","Weight Load","Return"]
        title = user_data[2] + ", you can sort the list here"
    
        while(1):
            default.print_title(title)
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice =='2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8'):
                break
    
        
        if(choice == '1'):
            header = "Car ID"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '2'):
            header = "Car Types"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '3'):
            header = "Car Brand"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
    
        if(choice == '4'):
            header = "Model Year"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
    
        if(choice == '5'):
            header = "Price per Hour"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '6'):
            header = "Passenger Capacity"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '7'):
            header = "Weight Load"
            sequence = clients.sub_sort_menu(header, data_carlist, 2)
        
        if(choice == '8'):
            return
        
        
        default.print_sorttable(data_carlist, 2, sequence, space_cars)
        print("")    

def carprofile_menu(data_carlist, space_cars):
    
    
    while(1):
        k = 0
        while(1):
            index = 0
            car_id = input("Please input the car ID: ")
        
            for i in range(1, len(data_carlist)):
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
                    carprofile_menu(data_carlist, space_cars)
                    
                                
                if(choice == '2'):
                    return
            
        
        car_data = data_carlist[index]
        for i in range(0,13):
            print(data_carlist[0][i] + ": " + car_data[i])    
            
        menu = ["Edit", "Return"]
    
        while(1): 
            print("\n")   
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
                
            print("Error!")
    
        if(choice == '1'):
            edit_carprofile(index, car_data, data_carlist, space_cars)
            return
        
        elif(choice == '2'):
            return
              
def edit_carprofile(index, car_data, data_carlist, space_cars):
    print("\nWhat do you want to edit?")
    menu = ["Car Types", "Car Brand", "Car Model", "Model Year", "Quantity", "Price per Hour", "Fuel Type", "Passenger Capacity", "Weight Load", "Return"]
    
    while(1):
        default.general_menu(menu)
        choice = input("Please Select: ")
        if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7' or choice == '8' or choice == '9' or choice == '10'or choice == '11' or choice == '12'):
            break
    if(choice == '10'):
        return
    
    if(choice == '1'):
        temp = default.validation_length(space_cars[1])
        car_data[1] = temp
    
    if(choice == '2'):
        temp = default.validation_length(space_cars[2])
        car_data[2] = temp
       
    if(choice == '3'):
        temp = default.validation_length(space_cars[3])
        car_data[3] = temp    
    
    if(choice == '4'):
        temp = default.validation_number(4)
        car_data[4] = temp
    
    if(choice == '5'):
        car_data = default.validation_totalquantity(data_carlist, car_data)

    if(choice == '6'):
        temp = default.validation_number(4)
        car_data[9] = temp
        
    if(choice == '7'):
        temp = default.validation_length(space_cars[10])
        car_data[10] = temp
    
    if(choice == '8'):
        temp = default.validation_number(3)
        car_data[11] = temp
        
    if(choice == '9'):
        temp = default.validation_number(10)
        car_data[12] = temp
       

    
        
    data_carlist[index] = car_data
    print(index)
    print(car_data)
    
    #print(data_clients)
    
    with open("./data/cars_lists.csv",  mode = 'w', newline = '') as cars_file:
        write = csv.writer(cars_file)
        write.writerows(data_carlist)
        
    return   

def addcar_menu(data_carlist, space_cars):
    default.print_title("You can add a car here")
    prev_id = data_carlist[-1][0]
   
    while(1):
        data = []
        id = int(prev_id) + 1
        data.append(id)
        type = default.validation_cartypes()
        print("")
        data.append(type)
        brand = default.validation_carnormal("car brand")
        print("")
        data.append(brand)
        model = default.validation_carnormal("car model")
        print("")
        data.append(model)
        print("Please enter model year: ")
        year = default.validation_number(4)
        print("")
        data.append(year)
        for i in range(4):
            data.append(0)
        data = default.validation_totalquantity(data_carlist, data, 2)
        #print(data)
      
        print("")
        print("Please enter price per hour: ")
        price = default.validation_number(4)
        data.append(price)
        print("")
        print("Please enter fuel type: ")
        fuel = default.validation_length(space_cars[10])
        data.append(fuel)
        print("")
        print("Please enter passenger number: ")
        passenger = default.validation_number(3)
        data.append(passenger)
        print("")
        print("Please enter price weight load: ")
        weight = default.validation_number(10)
        data.append(weight)
        print("")
        
        default.print_title("Confirm Car Details")
        k = 0
        for i in data:
            print(data_carlist[0][k] + ": " + str(i))
            k += 1
            
        menu = ["Confirm", "Return"]
        while(1):
            default.general_menu(menu)
            choice = input("Please Select: ")
            if(choice == '1' or choice == '2'):
                break
        
        if(choice == '1'):
            data_carlist.append(data)
            print(data)
            with open("./data/cars_lists.csv", mode = 'w', newline = "") as cars_file:
                write = csv.writer(cars_file)
                write.writerows(data_carlist)
            
            default.print_title("Car Information has successfuly recorded.")
            for remaining in range(5, -1, -1):
                sys.stdout.write("\r")
                sys.stdout.write("Will be directed in {:2d}......".format(remaining)) 
                sys.stdout.flush()
                time.sleep(1)
            sys.stdout.write("\n")
            return
        
        if(choice == '2'):
            return
        
                
            
        
        
        