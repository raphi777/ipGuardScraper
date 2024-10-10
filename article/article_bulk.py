from article import Article
import pandas as pd


class ArticleBulk:
    def __init__(self, articles: list[Article]):
        self.articles = articles
        self.title = []
        self.description = []
        self.price = []
        self.seller = []
        self.published_at = []
        self.marketplace = []
        self.url = []
        self.image_url = []
        self.search_term = []
        for article in self.articles:
            self.title.append(article.title)
            self.description.append(article.description)
            self.price.append(article.price)
            self.seller.append(article.seller)
            self.published_at.append(article.published_at)
            self.marketplace.append(article.marketplace)
            self.url.append(article.url)
            self.image_url.append(article.image_url)
            self.search_term.append(article.search_term)

    def get_as_dataframe(self):
        data = {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "seller": self.seller,
            "published_at": self.published_at,
            "marketplace": self.marketplace,
            "url": self.url,
            "image_url": self.image_url,
            "search_term": self.search_term
        }
        df = pd.DataFrame(data)
        print(df)
        return df
