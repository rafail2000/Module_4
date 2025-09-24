import pytest


def test_category_init(category_smartphones, category_tv):
    """ Тесты инициализации класса Category """

    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == ("Смартфоны, как средство не только коммуникации, но и получение"
                                                "дополнительных функций для удобства жизни")
    assert category_smartphones.products.count("\n") == 3

    assert category_smartphones.category_count == 2
    assert category_tv.category_count == 2

    assert category_smartphones.product_count == 34
    assert category_tv.product_count == 34


def test_products_list_getter(category_smartphones, product):
    """ Тесты геттера products """

    assert category_smartphones.products.count("\n") == 3


def test_products_list_setter(category_smartphones, product):
    """ Тесты сеттера products """

    assert category_smartphones.products.count("\n") == 3
    category_smartphones.products = product
    assert category_smartphones.products.count("\n") == 4


def test_products_list_setter_error(category_smartphones):
    """ Тесты сеттера products на возникновение ошибки TypeError"""

    with pytest.raises(TypeError):
        result = category_smartphones.products = 1


def test_add_product(category_smartphones, product):
    """ Тесты функции add_product"""

    assert category_smartphones.products.count("\n") == 3
    category_smartphones.add_product(product)
    assert category_smartphones.products.count("\n") == 4


def test_magic_category_str(category_smartphones):
    """ Тесты магического метода класса Category """

    category_smartphones.product_count = 3
    assert str(category_smartphones) == "Смартфоны, количество продуктов: 3 шт."


def test_middle_price(category_smartphones, category_zero_products):
    """ Тесты для проверки функции middle_price"""

    assert category_smartphones.middle_price() == 111629.63
    assert category_zero_products.middle_price() == 0
