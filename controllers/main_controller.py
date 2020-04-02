from models.articles import Articles
from models.cart import Cart
from models.delivery_fee import DeliveryFee
from models.discount import Discount


class MainController:
    def __init__(self, input_data, level):
        self.input_data = input_data
        self.level = level

    def generate_output(self):
        articles = Articles(data=self.input_data.get('articles', []))
        delivery = DeliveryFee(data=self.input_data.get('delivery_fees', []))
        discount = Discount(data=self.input_data.get('discounts', []))

        checkout_list = []

        for cart_data in self.input_data.get('carts', []):
            cart = Cart(
                cart_id=cart_data.get('id'), items=cart_data.get('items'),
                articles=articles, delivery=delivery, discount=discount
            )

            checkout_list.append({'id': cart.id, 'total': cart.total})

        return {'carts': checkout_list}
