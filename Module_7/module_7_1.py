# module_7_1
# Задача "Учёт товаров":
class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)  # Название товара
        self.weight = float(round(weight, 2))  # Вес товара
        self.category = str(category)  # Категория товара

    def __str__(self):
        """
        Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'.
        Все данные в строке разделены запятой с пробелами.
        """
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    """Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
Ин капсулированный атрибут __file_name = 'products.txt'."""
    __file_name = 'products.txt'  # Имя файла с данными товаров. Ин капсулированный атрибут __file_name = 'products.txt'.

    # def __init__(
    #         self):  # Реализация создания/пересоздания файла. Если закомментировать, то файл не будет пересоздаваться
    #     __file_name = open(self.__file_name, 'w')  # Открытие файла для
    #     __file_name.close()  # Закрытие файла

    def get_products(self):  # Получение списка продуктов из файла
        """Метод get_products(self), который считывает всю информацию из файла __file_name,
        закрывает его и возвращает единую строку со всеми товарами из файла __file_name."""
        file = open(self.__file_name, 'r')  # Открытие файла для чтения
        product_list = file.read().splitlines()  # Чтение всех строк из файла и преобразование их в список
        file.close()
        return product_list

    def add(self, *products):
        """Метод add(self, *products), который принимает неограниченное количество объектов класса Product.
        Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию).
        Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине"""
        # product_list = self.get_products()
        for product in products:
            product_list = self.get_products()
            if str(product) in product_list:
                # if product_list.index(str(product)):
                print(f'Продукт {product} уже есть в магазине')
            elif product not in self.get_products():
                product_str = str(product)  # Строковое представление продукта
                file = open(self.__file_name, 'a')  # Открытие файла для добавления
                file.write(product_str)  # Добавление данных в файл
                file.write(f'\n')
                file.close()  # Закрытие файла


# Пример работы программы:
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)  # , p3, p2)

print(s1.get_products())
