import json
from models.cart import Cart
from models.articles import Articles
from models.delivery_fee import DeliveryFee


ARTICLES_DATA = [
    { "id": 1, "name": "water", "price": 100 },
    { "id": 2, "name": "honey", "price": 200 },
    { "id": 3, "name": "mango", "price": 400 },
    { "id": 4, "name": "tea", "price": 1000 },
    { "id": 5, "name": "ketchup", "price": 999 },
    { "id": 6, "name": "mayonnaise", "price": 999 },
    { "id": 7, "name": "fries", "price": 378 },
    { "id": 8, "name": "ham", "price": 147 }
]

DELIVERY_DATA = [
    {
        "eligible_transaction_volume": {
            "min_price": 0,
            "max_price": 1000
        },
        "price": 800
    },
    {
        "eligible_transaction_volume": {
            "min_price": 1000,
            "max_price": 2000
        },
        "price": 400
    },
    {
        "eligible_transaction_volume": {
            "min_price": 2000,
            "max_price": None
        },
        "price": 0
    }
]


def test_total_without_delivery_fee():
    articles = Articles(data=ARTICLES_DATA)
    delivery = DeliveryFee(data=DELIVERY_DATA)

    items = [
        { "article_id": 1, "quantity": 6 },
        { "article_id": 2, "quantity": 2 },
        { "article_id": 4, "quantity": 1 }
    ]

    cart = Cart(id=1, items=items, articles=articles, delivery=delivery)

    assert cart.total == (100 * 6 + 200 * 2 + 1000)


def test_total_with_delivery_fee():
    articles = Articles(data=ARTICLES_DATA)
    delivery = DeliveryFee(data=DELIVERY_DATA)

    items = [
        { "article_id": 1, "quantity": 6 },
        { "article_id": 2, "quantity": 2 },
    ]

    cart = Cart(id=1, items=items, articles=articles, delivery=delivery)

    assert cart.total == (100 * 6 + 200 * 2) + 400


def test__calculate_items_total():
    articles = Articles(data=ARTICLES_DATA)
    delivery = DeliveryFee(data=DELIVERY_DATA)

    items = [
        { "article_id": 1, "quantity": 6 },
        { "article_id": 2, "quantity": 2 },
    ]

    cart = Cart(id=1, items=items, articles=articles, delivery=delivery)

    assert cart._calculate_items_total() == 100 * 6 + 200 * 2


def test__apply_delivery_fee():
    articles = Articles(data=ARTICLES_DATA)
    delivery = DeliveryFee(data=DELIVERY_DATA)

    items = [
        { "article_id": 1, "quantity": 6 },
        { "article_id": 2, "quantity": 2 },
    ]

    cart = Cart(id=1, items=items, articles=articles, delivery=delivery)

    cart_price = 1000
    assert cart._apply_delivery_fee(price=cart_price) == cart_price + 400