

class Articles:
    def __init__(self, data=[]):
        self.data = data

    def get_article_by_id(self, id):
        for article in self.data:
            if article.get('id') == id:
                return article
        return {}
