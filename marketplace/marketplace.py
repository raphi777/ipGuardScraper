from marketplace.mp_search_url_helper import get_search_url
from marketplace.mp_number_of_articles_finder import get_number_of_articles


class Marketplace:
    def __init__(self, id, cookies_config, number_of_articles_config):
        self.id = id
        self.cookies_config = cookies_config
        self.number_of_articles_config = number_of_articles_config

    def get_search_url(self, search_term):
        return get_search_url(self, search_term)

    def accept_cookies(self, driver):
        driver.implicitly_wait(5)
        button_accept = driver.find_element(by=self.cookies_config.by, value=self.cookies_config.value)
        button_accept.click()

    def get_number_of_articles(self, driver):
        return get_number_of_articles(driver, self)
