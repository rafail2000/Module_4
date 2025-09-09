class Product:
    """ Класс информации о продукте"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """ Дандер метод для строкового вывода атрибутов """

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Дандер метод для сложения продуктов """

        return self.price * self.quantity + other.price * other.quantity

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
