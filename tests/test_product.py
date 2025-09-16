from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product):
    """ Тесты инициализации класса Product """

    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_getter(product):
    """ Тесты геттера price """

    assert product.price == 180000.0


def test_products_list_setter(capsys, product):
    """ Тесты сеттера price """

    product.price = 200000.0
    assert product.price == 200000.0

    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


# Пример теста для метода validate_price
def test_validate_price_decrease(product):
    """ Попытка снизить цену, при этом имитируем ввод 'y' """

    with patch('builtins.input', return_value='y'):
        new_price = 50
        validated_price = product.validate_price(new_price)
        print(f"Validated price: {validated_price}")
        assert validated_price == product.price


def test_validate_price_no_decrease(product):
    """ Попытка снизить цену, имитируем ввод 'n' """

    with patch('builtins.input', return_value='n'):
        new_price = 50
        validated_price = product.validate_price(new_price)
        print(f"Validated price: {validated_price}")
        assert validated_price == new_price


def test_new_product(dictionary, lst_products):
    """ Тесты функции new_product """

    res = lst_products[0].new_product(dictionary, lst_products)
    assert isinstance(res, Product)
    assert res.price == 123000.0
    assert res.quantity == 14

    dictionary["price"] = 5000
    res = lst_products[0].new_product(dictionary, lst_products)
    assert res.price == 123000.0
    assert res.quantity == 14

    dictionary["name"] = "new_product"
    res = lst_products[0].new_product(dictionary, lst_products)
    assert res.price == 5000
    assert res.quantity == 7


def test_magic_product_str(product):
    """ Тесты магического метода класса Product """

    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_magic_product_add(product):
    """ Тесты магического метода класса Product """

    assert product + product == 1800000.0


def test_magic_product_add_error(product):
    """ Тесты магического метода класса Product ошибка TypeError"""
    with pytest.raises(TypeError):
        result = product + 1


def test_smartphone_init(smartphone_product1):
    """ Тесты инициализации класса Smartphone """

    assert smartphone_product1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product1.price == 180000.0
    assert smartphone_product1.quantity == 5
    assert smartphone_product1.efficiency == 95.5
    assert smartphone_product1.model == "S23 Ultra"
    assert smartphone_product1.memory == 256
    assert smartphone_product1.color == "Серый"


def test_magic_smartphone_add(smartphone_product1, smartphone_product2):
    """ Тесты магического метода класса Smartphone """

    assert smartphone_product1 + smartphone_product2 == 2580000.0


def test_magic_smartphone_add_error(smartphone_product1):
    """ Тесты магического метода класса Smartphone ошибка TypeError"""

    with pytest.raises(TypeError):
        result = smartphone_product1 + 1


def test_lawn_grass_init(lawn_grass_product1):
    """ Тесты инициализации класса LawnGrass """

    assert lawn_grass_product1.name == "Газонная трава"
    assert lawn_grass_product1.description == "Элитная трава для газона"
    assert lawn_grass_product1.price == 500.0
    assert lawn_grass_product1.quantity == 20
    assert lawn_grass_product1.country == "Россия"
    assert lawn_grass_product1.germination_period == "7 дней"
    assert lawn_grass_product1.color == "Зеленый"


def test_magic_lawn_grass_add(lawn_grass_product1, lawn_grass_product2):
    """ Тесты магического метода класса LawnGrass """

    assert lawn_grass_product1 + lawn_grass_product2 == 16750.0


def test_magic_lawn_grass_add_error(lawn_grass_product1):
    """ Тесты магического метода класса LawnGrass ошибка TypeError"""

    with pytest.raises(TypeError):
        result = lawn_grass_product1 + 1
