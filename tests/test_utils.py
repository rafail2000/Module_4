import json
from unittest.mock import mock_open, patch

from src.category import Category
from src.product import Product
from src.utils import read_json, create_object_from_json


def test_read_json(file):
    """ Тест функции для чтения данных из JSON """

    mock_json = json.dumps(file)

    m = mock_open(read_data=mock_json)

    with patch("builtins.open", m), patch("json.load", return_value=file) as mock_json_load:
        result = read_json("fake_path.json")

        m.assert_called_once_with("fake_path.json", "r", encoding="UTF-8")
        mock_json_load.assert_called_once()
        assert result == file


def test_create_object_from_json(file):
    """ Тест функции для преобразования в объект класса Category и Product  """

    categories = create_object_from_json(file)

    assert len(categories) == 1
    category = categories[0]
    assert isinstance(category, Category)
    assert category.name == "Телевизоры"
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет\
        вашим другом и помощником"

    assert hasattr(category, "products")
    assert len(category.products) == 1

    for product_tv in category.products:
        assert isinstance(product_tv, Product)
        assert hasattr(product_tv, "name")
        assert hasattr(product_tv, "description")
        assert hasattr(product_tv, "price")
        assert hasattr(product_tv, "quantity")
