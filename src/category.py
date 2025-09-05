from src.product import Product


class Category:
    """ Класс информации о категории товаров, количестве категорий и количестве товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products\
            else []
        Category.category_count += 1
        Category.product_count += len(products) if products\
            else 0

    @property
    def products(self) -> list:
        """ Геттер для вывода списка объектов класса Product"""

        return self.__products

    @products.setter
    def products(self, product: Product) -> None:
        """ Ceттер для записи объекта класса Product в список self.__products """

        Category.product_count += 1
        self.__products.append(product)

    def add_product(self, product: Product) -> None:
        """ Метод для записи объекта класса Product в список self.__products """

        self.products = product

    def get_str_lst(self):
        """ Возврат строковой информации из self.__products """

        product_str = ""
        for product in self.products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"

        return product_str
