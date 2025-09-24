import pytest

from src.category import Category
from src.product import Product, Smartphone, LawnGrass
from src.product_iterator import ProductIterator


@pytest.fixture
def category_smartphones():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение"
                    "дополнительных функций для удобства жизни",
        products=[Product(name="Samsung Galaxy C23 Ultra",
                          description="256GB, Серый цвет, 200MP камера",
                          price=180000.0,
                          quantity=5
                          ),
                  Product(name="Iphone 15",
                          description="512GB, Gray space",
                          price=210000.0,
                          quantity=8
                          ),
                  Product(name="Xiaomi Redmi Note 11",
                          description="1024GB, Синий",
                          price=31000.0,
                          quantity=14
                          )
                  ]
    )


@pytest.fixture
def category_tv():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим"
                    "другом и помощником",
        products=[Product(name="55\" QLED 4K",
                          description="Фоновая подсветка",
                          price=123000.0,
                          quantity=7
                          )
                  ]
    )


@pytest.fixture
def product():
    return Product(name="Samsung Galaxy C23 Ultra",
                   description="256GB, Серый цвет, 200MP камера",
                   price=180000.0,
                   quantity=5
                   )


@pytest.fixture
def file():
    return [{
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет\
        вашим другом и помощником",
        "products": [
            {
                "name": "55\" QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }]


@pytest.fixture
def dictionary():
    return {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
    }


@pytest.fixture
def lst_products():
    return [Product(name="55\" QLED 4K",
                    description="Фоновая подсветка",
                    price=123000.0,
                    quantity=7
                    )
            ]


@pytest.fixture
def product_iterator(category_smartphones):
    return ProductIterator(category_smartphones)


@pytest.fixture
def smartphone_product1():
    return Smartphone(name="Samsung Galaxy S23 Ultra",
                      description="256GB, Серый цвет, 200MP камера",
                      price=180000.0,
                      quantity=5,
                      efficiency=95.5,
                      model="S23 Ultra",
                      memory=256,
                      color="Серый"
                      )


@pytest.fixture
def smartphone_product2():
    return Smartphone(name="Iphone 15",
                      description="512GB, Gray space",
                      price=210000.0,
                      quantity=8,
                      efficiency=98.2,
                      model="15",
                      memory=512,
                      color="Gray space"
                      )


@pytest.fixture
def lawn_grass_product1():
    return LawnGrass(name="Газонная трава",
                     description="Элитная трава для газона",
                     price=500.0,
                     quantity=20,
                     country="Россия",
                     germination_period="7 дней",
                     color="Зеленый"
                     )


@pytest.fixture
def lawn_grass_product2():
    return LawnGrass(name="Газонная трава 2",
                     description="Выносливая трава",
                     price=450.0,
                     quantity=15,
                     country="США",
                     germination_period="5 дней",
                     color="Темно-зеленый"
                     )


@pytest.fixture
def category_zero_products():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, станет вашим"
                    "другом и помощником",
        products=[]
    )
