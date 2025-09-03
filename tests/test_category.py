def test_category_init(category_smartphones, category_tv):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == ("Смартфоны, как средство не только коммуникации, но и получение"
                                                "дополнительных функций для удобства жизни")
    assert len(category_smartphones.products) == 3

    assert category_smartphones.category_count == 2
    assert category_tv.category_count == 2

    assert category_smartphones.product_count == 4
    assert category_tv.product_count == 4
