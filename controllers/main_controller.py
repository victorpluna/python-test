import json
from models.articles import Articles
from models.cart import Cart


class MainController:
    def __init__(self, input_data, level):
        self.input_data = input_data
        self.level = level
    
    def generate_output(self):
        articles = Articles(data=self.input_data.get('articles', []))

        checkout_list = []

        for cart_data in self.input_data.get('carts', []):
            cart = Cart(
                id=cart_data.get('id'), items=cart_data.get('items'),
                articles=articles
            )
            
            checkout_list.append({'id': cart.id, 'total': cart.total})
        
        return {'carts': checkout_list}