def test_category_init(category_smartphones, category_tv):
    """ Тесты инициализации класса Category """

    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == ("Смартфоны, как средство не только коммуникации, но и получение"
                                                "дополнительных функций для удобства жизни")
    assert len(category_smartphones.products) == 3

    assert category_smartphones.category_count == 2
    assert category_tv.category_count == 2

    assert category_smartphones.product_count == 4
    assert category_tv.product_count == 4


def test_products_list_getter(category_smartphones, product):
    """ Тесты геттера products """

    assert len(category_smartphones.products) == 3


def test_products_list_setter(category_smartphones, product):
    """ Тесты сеттера products """

    assert len(category_smartphones.products) == 3
    category_smartphones.products = product
    assert len(category_smartphones.products) == 4


def test_add_product(category_smartphones, product):
    """ Тесты функции add_product"""

    assert len(category_smartphones.products) == 3
    category_smartphones.add_product(product)
    assert len(category_smartphones.products) == 4
