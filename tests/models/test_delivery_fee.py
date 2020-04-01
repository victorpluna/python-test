import json
from models.delivery_fee import DeliveryFee

DELIVERY_FEES_DATA = [
    {
        'eligible_transaction_volume': {
            'min_price': 0,
            'max_price': 1000
        },
        'price': 800
    },
    {
        'eligible_transaction_volume': {
            'min_price': 1000,
            'max_price': 2000
        },
        'price': 400
    },
    {
        'eligible_transaction_volume': {
            'min_price': 2000,
            'max_price': None
        },
        'price': 0
    }
]


def test_get_delivery_fee_first_range_success():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=100) == 800


def test_get_delivery_fee_second_range_success():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=1200) == 400


def test_get_delivery_fee_third_range_success():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=2200) == 0


def test_get_delivery_fee_price_zero():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=0) == 800


def test_get_delivery_fee_big_price():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=9999999) == 0


def test_get_delivery_fee_limit_min():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=1000) == 400


def test_get_delivery_fee_limit_max():
    delivery = DeliveryFee(data=DELIVERY_FEES_DATA)

    assert delivery.get_delivery_fee(price=2000) == 0