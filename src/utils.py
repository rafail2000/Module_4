import json

from src.category import Category
from src.product import Product


def read_json(path: str) -> list[dict]:
    """ Чтение JSON файла"""

    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def create_object_from_json(data: list[dict]) -> list[Category]:
    """ Создание объектов класса на основе из JSON файла"""

    categories = []

    for category in data:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
