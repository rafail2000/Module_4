class Category:
    """ Класс информации о категории товаров, количестве категорий и количестве товаров"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products\
            else []
        Category.category_count += 1
        Category.product_count += len(products) if products\
            else 0
