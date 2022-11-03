''' Mini Project week2'''

from ast import Break
from itertools import product
from pickle import FALSE, TRUE
from turtle import clear

def display_Main_Menu():
    str_Mesg = """ ***********Welcome to the store***********
    ***********Main Menu***********
    Please choose one of the following options : 
    0 to exit the application, 1 to go in Product menu, 2 to go in Order menu"""
    print(str_Mesg)

def display_Product_Menu():
    print("\t***********Product Menu***********")
    print("Press 5 to retrun to main menu, 6 to print the product List,")
    print("2 to add new product, 3 to update any product, 4 to delete the product")
def display_Order_Menu():
    print("\t***********Product Menu***********")
    print("Press 7 to retrun to main menu, 8 to print the Order Dictionary, 9 to place order")
    print("10 to update existing order status, 11 to update existing order, 12 to delete the order")

def add_Item_List(str_item, exiting_list):
    exiting_list.append(str_item)
    return exiting_list

def del_Item_List(item_index, exiting_list=[]):
    exiting_list.pop(item_index)    
    return exiting_list

def update_Item_List(item_index, item,exiting_list=[]):
    exiting_list[item_index]=item
    return exiting_list

product_list = ["Coke Zero","Coke Regular","Orange Juice","Apple Juice"]
order_Dict = {"customer_name": [None],"customer_address": [None],"customer_phone": [None],"status": [None]}
bMainFlag = True

while bMainFlag:
    display_Main_Menu()
    main_menu_inp = int(input())

    if (main_menu_inp == 0):
        print("Thanks for visiting the store, See you Again")
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
                # display_Main_Menu()
                # main_menu_inp = int(input())
                break

            elif (sub_menu_inp == 6):
                print("Available product List is:",product_list)
                # Print_sub_Menu()
                # sub_menu_inp = int(input())

            elif(sub_menu_inp == 2):
                Append_product_item = str(input("please provide the product name to add in List"))
                print(add_Item_List(Append_product_item,product_list))
                # Print_sub_Menu()
                # sub_menu_inp = int(input())

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
            print("Order Dictionary is: ",order_Dict)
        elif (order_menu_input == 9):
            order_Dict["customer_name"] = input("Please Enter your name: ")
            order_Dict["customer_address"] = input("Please enter your address")
            order_Dict["customer_phone"] = input("Enter phone number:")
            order_Dict["status"] = "PREPARING"
            order_Dict.update
            print("Your Order is on the way!")
    else:
        print("Incorrect selection")
        # Print_Main_Menu()
        # main_menu_inp = int(input())

    '''
https://pythonexamples.org/python-list-of-dictionaries/
'''