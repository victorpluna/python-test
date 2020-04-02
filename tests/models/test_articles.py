from models.articles import Articles


def test_get_article_by_id_with_existing_id():
    articles_data = [
      {'id': 1, 'name': 'water', 'price': 100},
      {'id': 2, 'name': 'honey', 'price': 200},
      {'id': 3, 'name': 'mango', 'price': 400}
    ]
    articles = Articles(data=articles_data)

    assert articles.get_article_by_id(article_id=1) == {
        'id': 1,
        'name': 'water',
        'price': 100
    }


def test_get_article_by_id_with_nonexistent_id():
    articles_data = [
      {'id': 1, 'name': 'water', 'price': 100},
      {'id': 2, 'name': 'honey', 'price': 200},
      {'id': 3, 'name': 'mango', 'price': 400}
    ]
    articles = Articles(data=articles_data)

    assert articles.get_article_by_id(article_id=4) == {}


def test_get_article_by_id_with_empty_data():
    articles_data = []
    articles = Articles(data=articles_data)

    assert articles.get_article_by_id(article_id=4) == {}
