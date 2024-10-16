from selenium import webdriver
from config.webdriver import get_standard_options
from article.article import Article
from marketplace.mp_article_attribute_finder import (get_title, get_description, get_price, get_seller,
                                                     get_published_at, get_image_url)


class Miner:
    def __init__(self, url, marketplace, search_term):
        self.url = url
        self.marketplace = marketplace
        self.search_term = search_term
        self.driver = webdriver.Chrome(options=get_standard_options())
        self.driver.get(self.url)
        self.marketplace.accept_cookies(self.driver)

    def mine(self):
        article = Article(
            title=get_title(driver=self.driver, mp=self.marketplace),
            description=get_description(driver=self.driver, mp=self.marketplace),
            price=get_price(driver=self.driver, mp=self.marketplace),
            seller=get_seller(driver=self.driver, mp=self.marketplace),
            published_at=get_published_at(driver=self.driver, mp=self.marketplace),
            marketplace=self.marketplace,
            url=self.url,
            image_url=get_image_url(driver=self.driver, mp=self.marketplace),
            search_term=self.search_term
        )
        self.driver.quit()
        return article
