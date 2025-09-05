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


def test_get_str_lst(category_smartphones):
    """ Тест вывода строковой информации из списка"""

    assert category_smartphones.get_str_lst() == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                                  "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                                  "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")
