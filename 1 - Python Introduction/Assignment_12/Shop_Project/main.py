from utils import *

shop = Eiliya_Shop()

while True:

    shop.show_menu()

    user_input = int(input('Enter Number: '))

    if user_input == 1: 
        shop.product_list()
        continue

    elif user_input == 2:
        id = int(input("Please Enter Id: "))
        name = input("Please Enter Name: ")
        count = int(input("Please Enter Count: "))
        price = int(input("Please Enter Price: "))
        shop.add_product(id, name, count, price)
        continue

    elif user_input == 3:
        id = int(input("Please Enter Id: "))
        shop.edit_product(id)
        continue

    elif user_input == 4:
        id = int(input("Please Enter Id: "))
        shop.delete_product(id)
        continue

    elif user_input == 5:
        id = int(input("Please Enter Id: "))
        shop.search_product(id)
        continue

    elif user_input == 6:
        id = int(input("Please Enter Id: "))
        shop.buy_product(id)
        continue

    elif user_input == 7:
        exit()
