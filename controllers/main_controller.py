import json
from models.articles import Articles
from models.cart import Cart
from models.delivery_fee import DeliveryFee


class MainController:
    def __init__(self, input_data, level):
        self.input_data = input_data
        self.level = level
    
    def generate_output(self):
        articles = Articles(data=self.input_data.get('articles', []))
        delivery = DeliveryFee(data=self.input_data.get('delivery_fees', []))

        checkout_list = []

        for cart_data in self.input_data.get('carts', []):
            cart = Cart(
                id=cart_data.get('id'), items=cart_data.get('items'),
                articles=articles, delivery=delivery
            )

            checkout_list.append({'id': cart.id, 'total': cart.total})
        
        return {'carts': checkout_list}