from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import marketplace_objects as mp
import time


def get_standard_options():
    # Configure headless mode
    options = Options()
    # options.headless = True
    # options.add_argument('--window-size=1920x1080')
    options.add_experimental_option('detach', True)
    return options


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
    article = driver.find_elements(by=By.CLASS_NAME, value='product')
    while len(article) < number_of_articles:
        article = driver.find_elements(by=By.CLASS_NAME, value='product')

        # scroll to bottom to show all elements
        footer = driver.find_element(by=By.TAG_NAME, value="footer")
        ActionChains(driver).move_to_element(footer).perform()

        time.sleep(5)

    print(len(article))

    for i in range(10):
        print(article[i].text)
    print(article[len(article) - 1].text)

    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    main()
