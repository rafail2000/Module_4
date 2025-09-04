class Product:
    """ Класс информации о продукте"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @property
    def price(self):
        """ Геттер для получения цены """

        return self.__price


    @price.setter
    def price(self, value):
        """ Сеттер для изменения цены """

        self.__price = value


    @classmethod
    def new_product(cls, product: dict, lst: list):
        """ Получение экземпляра класса Product и поиск товаров с похожим наименованием """

        for i in lst:
            if i.name == product["name"]:
                name = product["name"]
                description = product["description"]
                price = i.price if i.price >= product["price"]\
                    else product["price"]
                quantity = i.quantity + product["quantity"]
                return cls(name, description, price, quantity)

        return cls(**product)
