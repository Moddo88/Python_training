class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            return file.read().strip()

    def add(self, *products):
        existing_products = set()

        try:
            with open(self.__file_name, 'a+') as file:
                file.seek(0)

                for line in file:
                    product_info = line.strip().split(', ')
                    existing_products.add(product_info[0])

                for product in products:
                    if product.name not in existing_products:
                        print(f"Сохранен новый продукт: {product}")
                        file.write(str(product) + '\n')
                    else:
                        print(f"Продукт {product} уже есть в магазине")
        except FileNotFoundError:
            with open(self.__file_name, 'w') as new_file:
                for product in products:
                    new_file.write(str(product) + '\n')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

# Добавление товаров
s1.add(p1, p2, p3)

# Чтение всех товаров
print(s1.get_products())