import time

from selenium.webdriver.common.by import By
from selenium import webdriver

from article.article_bulk import ArticleBulk
from config.webdriver import get_standard_options
from mining.miner import Miner
import marketplace_objects as mp


def get_all_article_urls(articles):
    urls = []
    for article in articles:
        urls.append(article.find_element(by=By.TAG_NAME, value='a').get_attribute('href'))
    return urls


def main():
    driver = webdriver.Chrome(options=get_standard_options())

    # search for articles
    brand_name = "nike"
    marketplace = mp.TRENDYOL_DE
    driver.get(marketplace.get_search_url(brand_name))

    # accept cookies
    marketplace.accept_cookies(driver)

    # get number of articles
    number_of_articles = marketplace.get_number_of_articles(driver)

    # get articles
    articles = driver.find_elements(by=By.CLASS_NAME, value='product')
    # while len(articles) < number_of_articles:
    #     articles = driver.find_elements(by=By.CLASS_NAME, value='product')
    #
    #     # scroll to bottom to show all elements
    #     footer = driver.find_element(by=By.TAG_NAME, value="footer")
    #     ActionChains(driver).move_to_element(footer).perform()

    print("Number of Articles: " + str(len(articles)))

    urls = get_all_article_urls(articles)
    print(urls)

    # TODO: open all articles
    # TODO: get information about every single article and store in Article class
    list_articles = []
    for url in urls:
        miner = Miner(url, marketplace, brand_name)
        list_articles.append(miner.mine())
    # TODO: collect all articles in ArticleBulk class and convert to pandas dataframe
    article_bulk = ArticleBulk(list_articles)
    # TODO: print pandas dataframe & visualize/store e.g. in database/eleasticserach?
    article_bulk.get_as_dataframe()

    driver.quit()


if __name__ == "__main__":
    main()
