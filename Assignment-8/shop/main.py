from utils import *

cart = []
while True:
    show_menu()
    user_input = int(input('Enter Number: '))
    if user_input == 1:
        show_list()
    elif user_input == 2:
        code = input("Please Enter Code Add Product: ")
        name = input("Please Enter Name Add Product: ")
        count = input("Please Enter Count Add Product: ")
        price = input("Please Enter Price Add Product: ")
        add_product(code, name, code, price)
    elif user_input == 3:
        product = input("Please Enter Code Or Name Product for Edit: ")
        edit_product(product)
    elif user_input == 4:
        product = input("Please Enter Code Or Name Product for Delete: ")
        delete_product(product)
    elif user_input == 5:
        product = input("Please Enter Code Or Name Product for Search: ")
        search_product(product)
    elif user_input == 6:
        sum_price = 0
        while True:
            product = input("Please Enter Code Or Name Product for Buy Or Exit: ")
            if product == 'Exit' or product == 'exit':
                break
            else:
                cart.append(buy_product(product))
        for product in cart:
            print(
                f'{product["code_product"]}\t {product["name_product"]}\t {product["count_product"]}\t {product["price_product"]}\t')
            sum_price += int(product["count_product"]) * int(product["price_product"])
        print(f'Sum Price: {sum_price}')
        cart = []
    elif user_input == 7:
        get_discount()
    elif user_input == 8:
        exit_shop()
