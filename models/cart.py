

class Cart:
    def __init__(self, id, items, articles, delivery):
        self.id = id
        self.items = items
        self.articles = articles
        self.delivery = delivery

    @property
    def total(self):
        price = self._calculate_items_total()
        return self._apply_delivery_fee(price=price)

    def _calculate_items_total(self):
        total = 0
        for item in self.items:
            article = self.articles.get_article_by_id(id=item.get('article_id'))
            total += (article.get('price') * item.get('quantity'))
        return total

    def _apply_delivery_fee(self, price):
        delivery_fee = self.delivery.get_delivery_fee(price=price)
        return price + delivery_fee