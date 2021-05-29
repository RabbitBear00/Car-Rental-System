import admin
import default 
import clients 
import datetime 

def main():
    #The login users index in the csv file
    login_index = 2

    #Data for all Clients
    data_clients = []

    #Data for all cars
    data_carlist = []

    #Data for all transactions
    data_transactions = []

    #Data for login users
    user_data = []

    #Main header
    main_title = "Welcome to Super Car Rental System"

    #Spaces for the table
    space_clients = [11, 6, 20, 20, 13, 15, 13, 35, 16, 8, 10]
    space_cars = [7, 10, 20, 13, 10, 15, 15, 15, 15, 15, 10, 20, 12]
    space_transactions = [11, 20, 7, 10, 20, 13, 15, 10, 10, 10, 10, 15, 15, 12, 12, 10]

    data_clients = default.input_dataclients()
    data_carlist = default.input_datacars()
    data_transactions = default.input_datatransactions()
    
    #while(1):
    login_index = default.startup_interface(main_title, data_clients, data_carlist)
    user_data = data_clients[login_index]
    if(login_index == 1):
        admin.admin_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
    else:
        clients.client_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)
        
    #clients.bookcar_menu(user_data, data_clients, data_carlist, data_transactions, login_index, space_cars, space_clients, space_transactions)   


    
main()