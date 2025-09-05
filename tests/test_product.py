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


def test_new_product(dictionary, category_tv):
    lst = category_tv.products
    res = category_tv.products[0].new_product(dictionary, lst)
    assert isinstance(res, Product)
    assert res.price == 123000.0
    assert res.quantity == 14

    dictionary["price"] = 5000
    res = category_tv.products[0].new_product(dictionary, lst)
    assert res.price == 123000.0
    assert res.quantity == 14

    dictionary["name"] = "new_product"
    res = category_tv.products[0].new_product(dictionary, lst)
    assert res.price == 5000
    assert res.quantity == 7
