from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import marketplace_objects as mp
import time


def get_standard_options():
    # Configure headless mode
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=0x0')
    options.add_experimental_option('detach', True)
    return options


def get_all_article_urls(articles):
    urls = []
    for article in articles:
        urls.append(article.find_element(by=By.TAG_NAME, value='a').get_attribute('href'))
    return urls


def main():
    driver = webdriver.Chrome(options=get_standard_options())

    # search for articles
    brandname = "nike"
    marketplace = mp.TRENDYOL_DE
    driver.get(marketplace.get_search_url(brandname))

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
    # TODO: get infromation about every single article and store in Article class
    # TODO: collect all articles in ArticleBulk class and convert to pandas dataframe
    # TODO: print pandas dataframe & visualize/store e.g. in database/eleasticserach?

    driver.quit()


if __name__ == "__main__":
    main()
