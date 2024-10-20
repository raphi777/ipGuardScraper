from selenium.webdriver.common.by import By
from selenium import webdriver

from environment import OUT_FOLDER
from article.article_bulk import ArticleBulk
from config.webdriver import get_standard_options
from mining.miner import Miner
import marketplace_objects as mp
import datetime
import os


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

    list_articles = []
    for url in urls:
        miner = Miner(url, marketplace, brand_name)
        article = miner.mine()
        list_articles.append(article)
        # article.print_props()
    driver.quit()

    # collect all articles in ArticleBulk class and convert to pandas dataframe
    article_bulk = ArticleBulk(list_articles)

    article_bulk.get_as_dataframe()
    outfile_name = marketplace.id + '_' + str(datetime.datetime.now())
    with open(os.path.join(OUT_FOLDER, outfile_name + '.csv'), 'w') as f:
        f.write(article_bulk.get_as_dataframe().to_csv())


if __name__ == "__main__":
    main()
