from pprint import pprint


class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        product_info = str(self.name) + ', ' + str(self.weight) + ', ' + str(self.category)
        return product_info


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(Shop.__file_name, 'r')
        products_string = file.read()
        file.close()
        return products_string

    def add(self, *products):
        product_list = self.get_products()
        for product in products:
            if str(product) not in product_list:
                file = open(Shop.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()
            else:
                print(f'{product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)
s1.add(p1, p2, p3)
print(s1.get_products())
