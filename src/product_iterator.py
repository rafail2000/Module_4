from src.category import Category
from src.product import Product


class ProductIterator:
    """ Класс для итерации по продуктам """

    def __init__(self, category_obj):
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.category.products.split("\n")):
            product = self.category.products.split("\n")[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    category = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение"
                    "дополнительных функций для удобства жизни",
        products=[Product(name="Samsung Galaxy C23 Ultra",
                          description="256GB, Серый цвет, 200MP камера",
                          price=180000.0,
                          quantity=5
                          ),
                  Product(name="Iphone 15",
                          description="512GB, Gray space",
                          price=210000.0,
                          quantity=8
                          ),
                  Product(name="Xiaomi Redmi Note 11",
                          description="1024GB, Синий",
                          price=31000.0,
                          quantity=14
                          )
                  ]
    )

    iterator = ProductIterator(category)

    for task in iterator:
        print(task)

    for task in iterator:
        print(task)
