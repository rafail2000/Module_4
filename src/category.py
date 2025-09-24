from abc import ABC, abstractmethod

from src.exceptions import ZeroProductQuantity
from src.product import Product


class OrderCategoryAbstract(ABC):
    """ Абстрактный класс для Заказа и Категории """

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Order(OrderCategoryAbstract, ABC):
    """ Класс Заказ """

    product_count = 0

    def __init__(self, name: str, description: str, link: Product, quantity: int, price: float) -> None:
        self.name = name
        self.description = description
        self.link = link
        self.quantity = quantity
        self.price = price
        self.__products = []

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.quantity} шт."

    @property
    def products(self) -> str:
        """ Геттер для вывода списка объектов класса Order """

        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"

        return product_str

    @products.setter
    def products(self, product: Product) -> None:
        """ Ceттер для записи объекта Order в список self.__products """

        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductQuantity("Нельзя добавлять продукт с нулевым кол-вом")
            except ZeroProductQuantity as e:
                print(e)
            else:
                Order.product_count += 1
                self.__products.append(product)
                print("Продукт добавлен в категорию")
            finally:
                print("Операция выполнена")
        else:
            raise TypeError


class Category(OrderCategoryAbstract):
    """ Класс информации о категории товаров, количестве категорий и количестве товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products\
            else []
        Category.category_count += 1
        Category.product_count += sum([i.quantity for i in products]) if products\
            else 0

    def __str__(self):
        """ Дандер метод для строкового вывода атрибутов """

        return f"{self.name}, количество продуктов: {self.product_count} шт."

    @property
    def products(self) -> str:
        """ Геттер для вывода списка объектов класса Product"""

        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"

        return product_str

    @products.setter
    def products(self, product: Product) -> None:
        """ Ceттер для записи объекта класса Product в список self.__products """

        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroProductQuantity("Нельзя добавлять продукт с нулевым кол-вом")
            except ZeroProductQuantity as e:
                print(e)
            else:
                Category.product_count += 1
                self.__products.append(product)
                print("Продукт добавлен в категорию")
            finally:
                print("Операция выполнена")
        else:
            raise TypeError

    def add_product(self, product: Product) -> None:
        """ Метод для записи объекта класса Product в список self.__products """

        self.products = product

    def middle_price(self):
        """ Метод подсчёта среднего ценника всех товаров """

        try:
            return round(
                sum([i.price * i.quantity for i in self.__products]) / sum([i.quantity for i in self.__products]), 2
            )
        except ZeroDivisionError:
            return 0
