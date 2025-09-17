from abc import ABC, abstractmethod

from src.print_mixin import PrintMixin


class BaseProduct(ABC):
    """ Абстрактный класс Продукта """

    @abstractmethod
    def validate_price(self, value):
        """ Абстрактный метод проверки цены """

        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product, lst):
        """ Абстрактный метод получение экземпляра класса Product и поиск товаров с похожим наименованием """

        pass


class Product(BaseProduct, PrintMixin):
    """ Класс информации о продукте """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        """ Дандер метод для строкового вывода атрибутов """

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Дандер метод для сложения продуктов """

        if type(other) is Product:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError

    @property
    def price(self):
        """ Геттер для получения цены """

        return self.__price

    @price.setter
    def price(self, value):
        """ Сеттер для изменения цены """

        value = self.validate_price(value)
        self.__price = value

    def validate_price(self, value):
        """ Проверка цены """

        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif value < self.price:
            user_answer = input("Вы уверены в снижении цены? y/n").lower()
            if user_answer == "y":
                return self.price

        return value

    @classmethod
    def new_product(cls, product: dict, lst: list = None):
        """ Получение экземпляра класса Product и поиск товаров с похожим наименованием """

        if lst is not None:
            for i in lst:
                if i.name == product["name"]:
                    name = product["name"]
                    description = product["description"]
                    price = i.price if i.price >= product["price"]\
                        else product["price"]
                    quantity = i.quantity + product["quantity"]
                    return cls(name, description, price, quantity)

        return cls(**product)


class Smartphone(Product):
    """ Класс смартфон """

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 efficiency: float,
                 model: str,
                 memory: int,
                 color: str
                 ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """ Дандер метод для сложения продуктов """

        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError


class LawnGrass(Product):
    """ Класс трава газонная """

    def __init__(self, name: str,
                 description: str,
                 price: float,
                 quantity: int,
                 country: str,
                 germination_period: str,
                 color: str
                 ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """ Дандер метод для сложения продуктов """

        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
