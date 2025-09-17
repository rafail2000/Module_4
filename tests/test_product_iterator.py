import pytest


def test_product_iterator(product_iterator):
    """ Тест класса ProductIterator """

    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator) == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert next(product_iterator) == 'Iphone 15, 210000.0 руб. Остаток: 8 шт.'
    assert next(product_iterator) == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'
    assert next(product_iterator) == ''

    with pytest.raises(StopIteration):
        next(product_iterator)
