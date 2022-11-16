''' Mini Project week3'''

from ast import Break
from itertools import product
from pickle import FALSE, TRUE
from turtle import clear

def display_Main_Menu():
    str_Mesg = """ ***********Welcome to the store***********
    ***********Main Menu***********
    Please choose one of the following options : 
    0 -- exit || 1 -- Product Menu || 2 -- Order Menu || 3 -- Courier Menu 
    """
    print(str_Mesg)

def display_Product_Menu():
    str_Product_Mesg = """\t***********Product Menu***********
Please choose one of the following options: 
5 --Retrun to main menu ||6 --View Products||2 --Add new Product||3 -- Update Product||4--Delete Product 
"""
    print(str_Product_Mesg)


def display_Order_Menu():
    # print("\t***********Order Menu***********")
    # print("Press 7 to retrun to main menu")
    # print("8 to print the available Orders")
    # print("9 to place New Order")
    # print("10 to update existing order List")
    # print("11 to update any order information")
    # print("12 to delete the order")
    str_Order_Mesg = """\t***********Order Menu***********
    Please choose one of the following options: 
    7 --Retrun to main menu ||8 --View Order||9 --Place Order||10 -- Update Order status List||11--Update Order||12--Delete Order 
    """
    print(str_Order_Mesg)

def display_Courier_Menu():
    # print("\t***********Courier Menu***********")
    # print("Press 13 to retrun to main menu")
    # print("14 to print the Available Courier List")
    # print("15 to add new Courier in List")
    # print("16 to update existing Courier")
    # print("17 to delete any courier item from list")
    str_Courier_Mesg = """\t***********Courier Menu***********
    Please choose one of the following options: 
    13 --Retrun to main menu ||14 --View Courier List||15 --Add New Courier||16 -- Update Existing Courier||17--Delete Existing Courier  
    """
    print(str_Courier_Mesg)
    
def add_Item_List(str_item, exiting_list):
    exiting_list.append(str_item)
    return exiting_list

def del_Item_List(item_index, exiting_list=[]):
    exiting_list.pop(item_index)    
    return exiting_list

def del_Order_Dict_List(item_index, exiting_list=[]):
    exiting_list.pop(item_index)    
    return exiting_list

def update_Item_List(item_index, item,exiting_list=[]):
    exiting_list[item_index]=item
    return exiting_list

def print_order_status_List(order_list):
    indent = 2
    for i in range(len(order_list)):
        print(' ' * indent, 'Index ',i, ':', order_list[i])

def print_Courier_List(courier_list):
    indent = 2
    for i in range(len(courier_list)):
        print(' ' * indent, 'Index ',i, ':', courier_list[i])

def Load_Product_List():
    file=None
    try:
        product_list = []
        file = open("products.txt", "r")
        lines = file.readlines()
        for line in lines:
            product_list.append(line.strip())
        # file.close()
        # return product_list
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return product_list
    finally:
        file.close()
        return product_list
        

def dump_Product_List_File(product_list):
    file=None
    try:
        file = open("products.txt", "w")
        for i in range(len(product_list)):
            file.write(product_list[i]+"\n")
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        file.close()

def Load_Courier_List():
    file=None
    try:
        courier_list = []
        file = open("courier.txt", "r")
        lines = file.readlines()
        for line in lines:
            courier_list.append(line.strip())
    # file.close()
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
        return courier_list
    finally:
        file.close()
        return courier_list

def dump_Courier_List_File(courier_list):
    file=None
    try:
        file = open("courier.txt", "w")
        for i in range(len(courier_list)):
            file.write(courier_list[i]+"\n")
    except FileNotFoundError as fnfe:
        print('Unable to open file: ' + str(fnfe))
    finally:
        file.close()

# product_list = ["Coke Zero","Coke Regular","Orange Juice","Apple Juice"]
product_list = Load_Product_List()
order_Dict = [{"customer_name":"Joe","customer_address": "Preston","customer_phone": "0213685","customer_courier":0,"status": "Delivered"}]
# order_list = [{"customer_name":"Joe","Order_status":"Delivered"}]
order_list =["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
courier_list = Load_Courier_List()
bMainFlag = True

while bMainFlag:
    display_Main_Menu()
    main_menu_inp = int(input())

    if (main_menu_inp == 0):
        print("Thanks for visiting the store, See you Again")
        ''' need to call write methods of files
        '''
        dump_Product_List_File(product_list)
        dump_Courier_List_File(courier_list)
        bMainFlag=FALSE
        break
        # exit

    elif(main_menu_inp == 1):
        # display_sub_Menu()
        # sub_menu_inp = int(input())
        
        while True:    
            display_Product_Menu()
            sub_menu_inp = int(input())

            if (sub_menu_inp == 5):
                bMainFlag=TRUE
                break

            elif (sub_menu_inp == 6):
                print("Available product List is:",product_list)
                
            elif(sub_menu_inp == 2):
                Append_product_item = str(input("please provide the product name to add in List"))
                print(add_Item_List(Append_product_item,product_list))
                
            elif(sub_menu_inp == 3):

                for i in range(len(product_list)):
                    print(i,product_list[i])
                index_update = int(input("Enter the index where you want to update product"))
                product_update = input("Enter the product name you want to add")
                print("updated List",update_Item_List(index_update,product_update,product_list))

            elif(sub_menu_inp == 4):
                
                print("Existing Product List")
                for i in range(len(product_list)):
                    print(i,product_list[i])
                
                index_delete = int(input("Enter the index where you want to delete product : "))
                print("updated List after deletion",del_Item_List(index_delete,product_list))
            else:
                print("Incorrect selection")

    elif(main_menu_inp == 2):
        display_Order_Menu()
        order_menu_input = int(input())
        
        if (order_menu_input == 7):
            bMainFlag=TRUE

        elif (order_menu_input == 8):
            print("*** Order Dictionary is ***")
            indent = 2
            for i in range(len(order_Dict)):
                print(' ' * indent, 'Index ',i, ':', order_Dict[i],'\n')

        elif (order_menu_input == 9):
            
            cust_name= input("Please Enter your name: ")
            cust_add = input("Please enter your address: ")
            cust_phone  = input("Enter phone number: ")
            print("Available courier List")
            print_Courier_List(courier_list)
            cust_courier = input("Please select index number of the courier service for your order:")
            cust_order_status = order_list[0]
            #check for incorrect input
            # order_Dict.append({"customer_name":cust_name,"customer_address":cust_add,"cust_phone":cust_phone,"status":"Preparing"})
            order_Dict.append({"customer_name":cust_name,"customer_address":cust_add,"cust_phone":cust_phone,"customer_courier":cust_courier,"status":cust_order_status})
            # order_list.append({"customer_name":cust_name,"Order_status":"Preparing"})
            print("Your Order is on the way!")

        elif (order_menu_input == 10):
            
            print("List of existing order status List")
            print_order_status_List(order_list)
            # indent = 4
            # for i in range(len(order_list)):
            #     print(' ' * indent, 'Index ',i, ':', order_list[i],'\n')

            index_order_status = int(input("Enter the index you want to update order status"))
            if 0 <= index_order_status < len(order_list):
                print()
            else:
                print("Index doesn't exist in the List")
                break
            order_status = input("Enter the status you want to update: ")
            order_list[index_order_status] = order_status
            print("updated Order status List")
            # for i in range(len(order_list)):
            #     print(' ' * indent, 'Index ',i, ':', order_list[i],'\n')
            print_order_status_List(order_list)

        elif (order_menu_input == 11):
            print("Available Orders customers information")
            indent = 2
            for i in range(len(order_Dict)):
                print(' ' * indent, 'Index ',i, ':', order_Dict[i],'\n')
                index_order_update = int(input("Enter the index of order you to update:"))
                
                if 0 <= index_order_update < len(order_Dict):
                    print()
                else:
                    print("Index doesn't exist in the List")
                    break

                cust_name= input("Please the name you want to update or press enter to leave it unchanged")
                if cust_name != "":
                    order_Dict[index_order_update]["customer_name"]=cust_name

                cust_add = input("Please enter your address to update or press enter to leave it unchanged")
                if cust_add != "":
                    order_Dict[index_order_update]["customer_address"] = cust_add

                cust_phone  = input("Enter phone number to update or press enter to leave it unchanged")
                if cust_phone != "":    
                    order_Dict[index_order_update]["customer_phone"] = cust_phone

                cust_courier  = input("Enter index of courier to update or press enter to leave it unchanged")
                if cust_courier != "":    
                    order_Dict[index_order_update]["customer_courier"] = cust_courier
                
                print(' ' * indent, 'Index ',index_order_update, ':', order_Dict[index_order_update])
        
        elif(order_menu_input == 12):
            indent = 2
            for i in range(len(order_Dict)):
                print(' ' * indent, 'Index ',i, ':', order_Dict[i],'\n')
                
            index_del = int(input("Enter the index of order you want to delete: "))
            order_Dict=del_Item_List(index_del,order_Dict)
            if len(order_Dict) == 0:
                print("No more order in List")
            else:
                print("updated Order List",order_Dict)
    elif(main_menu_inp == 3):

        display_Courier_Menu()
        courier_menu_input = int(input())
        if (courier_menu_input == 13):
            bMainFlag = TRUE

        elif (courier_menu_input == 14):
            print_Courier_List(courier_list)

        elif (courier_menu_input == 15):
            courier_Add = input("Enter the courier name you want to add in List")
            courier_list.append(courier_Add)
            print("Updated Courier List")
            print_Courier_List(courier_list)

        elif (courier_menu_input == 16):
            print("Update Courier information in List")
            print_Courier_List(courier_list)
            index_update = int(input("Enter the index where you want to update product"))
            courier_update = input("Enter the product name you want to add")
            print("updated Courier List",update_Item_List(index_update,courier_update,courier_list))


        elif (courier_menu_input == 17):
            print("Available courier List")
            print_Courier_List(courier_list)
            index_del = int(input("Enter the index of order you want to delete: "))
            if 0 <= index_del < len(courier_list):
                print()
            else:
                print("Index doesn't exist in the List")
                bMainFlag=TRUE
                break

            courier_list = del_Item_List(index_del,courier_list)
            if len(courier_list) == 0:
                print("No more courier providers in List")
            else:
                print("updated Courier List",courier_list)
        # else:
        #     print("Incorrect selection")
    else:
        print("Incorrect selection")
        # Print_Main_Menu()
        # main_menu_inp = int(input())