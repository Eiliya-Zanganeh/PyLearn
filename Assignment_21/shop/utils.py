from qrcode import make
import sqlite3


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
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    conct.close()
    for product in rows:
        code, name, count, price = product
        print(f'{code}\t {name}\t {count}\t {price}\t')
    conct.close()
    


def edit_product(name_or_code):
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM product WHERE id=? OR name=?", (name_or_code, name_or_code))
    rows = cur.fetchall()
    if len(rows) > 0:
        user_input = input('Edit Name Or Count Or Price or All or Exit? ').strip().title()
        if user_input == 'Name':
            name = input('Please Enter New Name: ').strip()
            cur.execute("UPDATE product SET name=? WHERE id=?", (name, rows[0]))
            conct.commit()
        elif user_input == 'Count':
            count = input('Please Enter New Count: ').strip()
            cur.execute("UPDATE product SET count=? WHERE id=?", (count, rows[0]))
            conct.commit()
        elif user_input == 'Price':
            price = input('Please Enter New Price: ').strip()
            cur.execute("UPDATE product SET price=? WHERE id=?", (price, rows[0]))
            conct.commit()
        elif user_input == 'Exit':
            return
        elif user_input == 'All':
            name = input('Please Enter New Name: ').strip()
            count = input('Please Enter New Count: ').strip()
            price = input('Please Enter New Price: ').strip()
            cur.execute("UPDATE product SET name=?, count=?, price=? WHERE id=?", (name, count, price, rows[0][0]))
            conct.commit()
        else:
            print('mese adam vared kon :| ...')
    else:
        print('Product Not Found')
    conct.close()


def delete_product(name_or_code):
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("DELETE FROM product WHERE id=? OR name=?", (name_or_code, name_or_code))
    conct.commit()
    conct.close()


def buy_product(name_or_code):
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM product WHERE id=? OR name=?", (name_or_code, name_or_code))
    rows = cur.fetchall()
    if len(rows) > 0:
        user_input = int(input('Please Enter Count: '))
        if rows[0][2] < user_input:
            print('The Number Of goods Is Not Enough...')
            return
        else:
            if rows[0][2] == 0:
                delete_product(code)
            else:
                cur.execute("UPDATE product SET count=? WHERE id=?", (rows[0][2] - user_input, rows[0][0]))
                conct.commit()
                print('The Item Has Been Successfully Added To The Shopping Cart')
                return {
                        'code_product': rows[0][0],
                        'name_product': rows[0][1],
                        'count_product': user_input,
                        'price_product': rows[0][3]
                    }
    else:
        print('Product Not Found')
    conct.close()

    
def search_product(name_or_code):
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("SELECT * FROM product WHERE id=? OR name=?", (name_or_code, name_or_code))
    rows = cur.fetchall()
    print(f"{rows[0][0]}\t {rows[0][1]}\t {rows[0][2]}\t {rows[0][3]}\t")
    conct.close()


def add_product(code, name, count, price):
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("INSERT INTO product VALUES (NULL, ?, ?, ?) ", (name, count, price))
    conct.commit()
    conct.close()


def get_discount():
    img = make('Eiliya Token')
    img.save('token.png')


def exit_shop():
    exit()


def connect():
    conct = sqlite3.connect("database.db")
    cur = conct.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS product (ID INTEGER PRIMARY KEY, name text, count INTEGER, price INTEGER )")
    conct.commit()
    conct.close()

connect()