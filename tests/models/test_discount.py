import json
from models.discount import Discount


DISCOUNT_DATA = [
    { 'article_id': 2, 'type': 'amount', 'value': 25 },
    { 'article_id': 5, 'type': 'percentage', 'value': 30 },
    { 'article_id': 6, 'type': 'percentage', 'value': 30 },
    { 'article_id': 7, 'type': 'percentage', 'value': 25 },
    { 'article_id': 8, 'type': 'percentage', 'value': 10 }
]


def test__get_discount_by_article_id_with_existing_id():
    discount = Discount(data=DISCOUNT_DATA)

    assert discount._get_discount_by_article_id(article_id=2) == {
        'article_id': 2,
        'type': 'amount',
        'value': 25
    }


def test__get_discount_by_article_id_with_nonexistant_id():
    discount = Discount(data=DISCOUNT_DATA)

    assert discount._get_discount_by_article_id(article_id=1) == {}


def test__apply_discount_on_price_with_amount_value():
    discount = Discount(data=DISCOUNT_DATA)
    discount_value = 10
    price = 200 
    item = {'article_id': 8, 'type': 'amount', 'value': discount_value}

    assert discount._apply_discount_on_price(discount=item, price=price)\
        == price - discount_value


def test__apply_discount_on_price_with_percentage_value():
    discount = Discount(data=DISCOUNT_DATA)
    discount_value = 10
    price = 200 
    item = {'article_id': 8, 'type': 'percentage', 'value': discount_value}

    assert discount._apply_discount_on_price(discount=item, price=price)\
        == (price - price * discount_value / 100)


def test__apply_discount_on_price_with_nonexistant_value():
    discount = Discount(data=DISCOUNT_DATA)
    discount_value = 10
    price = 200 
    item = {'article_id': 8, 'type': 'nonexistant', 'value': discount_value}

    assert discount._apply_discount_on_price(discount=item, price=price)\
        == price


def test_get_article_price_with_discount():
    discount = Discount(data=DISCOUNT_DATA)
    article = {'id': 8, 'price': 400}

    assert discount.get_article_price(article=article) == 360


def test_get_article_price_without_discount():
    discount = Discount(data=DISCOUNT_DATA)
    article = {'id': 70, 'price': 400}

    assert discount.get_article_price(article=article) == 400

