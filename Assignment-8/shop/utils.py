from qrcode import make


def show_menu():
    print('1_ Show List Of Products')  # done
    print('2_ Add New Product')  # done
    print('3_ Edit Products')  # done
    print('4_ Delete Products')  # done
    print('5_ Search Products')  # done
    print('6_ Buy Products')  # done
    print('7_ Get Discount')  # done
    print('8_ Exit')


def show_list():
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            code, name, count, price = line.split(',')
            print(f'{code}\t {name}\t {count}\t {price}\t')


def edit_product(name_or_code):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, count, price = data.split(',')
        if code == name_or_code or name == name_or_code:
            while True:
                user_input = input('Edit Code or Name Or Count Or Price or All or Exit? ').strip().title()
                if user_input == 'Code':
                    code = input('Please Enter New Code: ').strip()
                    break
                elif user_input == 'Name':
                    name = input('Please Enter New Name: ').strip()
                    break
                elif user_input == 'Count':
                    count = input('Please Enter New Count: ').strip()
                    break
                elif user_input == 'Price':
                    price = input('Please Enter New Price: ').strip()
                    break
                elif user_input == 'Exit':
                    return
                elif user_input == 'All':
                    code = input('Please Enter New Code: ').strip()
                    name = input('Please Enter New Name: ').strip()
                    count = input('Please Enter New Count: ').strip()
                    price = input('Please Enter New Price: ').strip()
                    break
                else:
                    print('mese adam vared kon :| ...')

            index = datas.index(data)
            datas[index] = f'{code},{name},{count},{price}\n'
            with open('database.txt', 'w') as file:
                for d in datas:
                    file.write(d)
            print('Data Has Been Updated')
            break

    else:
        print('Product Not Found')


def delete_product(name_or_code):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, count, price = data.split(',')
        if code == name_or_code or name == name_or_code:
            index = datas.index(data)
            datas[index] = ''
            with open('database.txt', 'w') as file:
                for d in datas:
                    file.write(d)
            print('The item has been removed')
            break

    else:
        print('Product Not Found')


def buy_product(name_or_code):
    datas = []
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            datas.append(line)
    for data in datas:
        code, name, count, price = data.split(',')
        count = int(count)
        if code == name_or_code or name == name_or_code:
            user_input = int(input('Please Enter Count: '))
            if user_input > count:
                print('The Number Of goods Is Not Enough...')
                return
            else:
                count -= user_input
                if count == 0:
                    delete_product(code)
                else:
                    index = datas.index(data)
                    datas[index] = f'{code},{name},{count},{price}'
                    with open('database.txt', 'w') as file:
                        for d in datas:
                            file.write(d)
                    print('The Item Has Been Successfully Added To The Shopping Cart')
                    return {
                        'code_product': code,
                        'name_product': name,
                        'count_product': user_input,
                        'price_product': price
                    }


    else:
        print('Product Not Found')


def search_product(name_or_code):
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            code, name, count, price = line.split(',')
            if code == name_or_code or name == name_or_code:
                print(f"{code}\t {name}\t {count}\t {price}\t")
                break


def add_product(code, name, count, price):
    with open('database.txt', 'a') as file:
        file.write(f'\n{code},{name},{count},{price}')


def get_discount():
    img = make('Eiliya Token')
    img.save('token.png')


def exit_shop():
    exit()
