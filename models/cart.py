

class Cart:
    def __init__(self, id, items, articles):
        self.id = id
        self.items = items
        self.articles = articles

    @property
    def total(self):
        total = 0
        for item in self.items:
            article = self.articles.get_article_by_id(id=item.get('article_id'))
            total += (article.get('price') * item.get('quantity'))
        return total