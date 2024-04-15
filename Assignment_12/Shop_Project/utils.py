class Eiliya_Shop:
    def __init__(self, products=[]):
        self.products = products

    @staticmethod
    def show_menu():
        print('1_ Show List Of Products')
        print('2_ Add New Product')
        print('3_ Edit Products')
        print('4_ Delete Products')
        print('5_ Search Products')
        print('6_ Buy Products')
        print('7_ Exit')

    def product_list(self):
        for product in self.products:
            print(product)

    def add_product(self, id, name, count, price):
        product = Product(id, name, count, price)
        self.products.append(product)

    def edit_product(self, id):
        for product in self.products:
            if product.id == id:
                product.id = int(input("PLease Enter New Id: "))
                product.name = input("PLease Enter New Name: ")
                product.count = int(input("PLease Enter New Count: "))
                product.price = int(input("PLease Enter New Price: "))
                break
            else:
                continue
        else:
            print("Product Not Found :| ")

    def delete_product(self, id):
        for product in self.products:
            if product.id == id:
                self.products.remove(product)
                break
            else:
                continue
        else:
            print("Product Not Found :| ")

    def search_product(self, id):
        for product in self.products:
            if product.id == id:
                return product
            else:
                continue
        else:
            print("Product Not Found :| ")

    def buy_product(self, id):
        for product in self.products:
            if product.id == id:
                if product.count > 0:
                    product.count -= 1
                else:
                    print("The Count Of Product Is Not Enough :| ")
            else:
                continue
        else:
            print("Product Not Found :| ")

    def __str__(self):
        return "Eiliya Shop"

class Product:
    def __init__(self, id, name, count, price):
        self.id = id
        self.name = name
        self.count = count
        self.price = price

    def __str__(self):
        return f'{self.id}\t|{self.name}\t|{self.count}\t|{self.price}'