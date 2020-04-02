

class Discount:
    AMOUNT = 'amount'
    PERCENTAGE = 'percentage'

    def __init__(self, data):
        self.discounts = data

    def _get_discount_by_article_id(self, article_id):
        for discount in self.discounts:
            if discount.get('article_id') == article_id:
                return discount
    
    def _apply_discount_on_price(self, discount, price):
        if discount.get('type') == self.AMOUNT:
            return price - discount.get('value')
        elif discount.get('type') == self.PERCENTAGE:
            return int(price - discount.get('value') * price / 100)
        return price


    def get_article_price(self, article):
        price = article.get('price')
        discount = self._get_discount_by_article_id(
            article_id=article.get('id')
        )
        if not discount:
            return price

        return self._apply_discount_on_price(discount=discount, price=price)