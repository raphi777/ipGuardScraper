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
    # options.add_argument('--window-size=3920x3080')
    # options.add_argument('--auto-open-devtools-for-tabs')
    options.add_experimental_option('detach', True)
    return options


def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='4px solid red'", element)
    time.sleep(0.7)


def unhighlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='none'", element)


def scroll_to_element(driver, element):
    ActionChains(driver).move_to_element(element).perform()
    time.sleep(1)


def main():
    driver = webdriver.Chrome(options=get_standard_options())
    driver.set_window_size(2500, 1400)

    # search for articles
    brand_name = "nike"
    marketplace = mp.TRENDYOL_DE
    driver.get(marketplace.get_search_url(brand_name))

    # accept cookies
    marketplace.accept_cookies(driver)

    # get number of articles
    # number_of_articles = marketplace.get_number_of_articles(driver)

    # get articles
    articles = driver.find_elements(by=By.CLASS_NAME, value='product')
    # while len(article) < number_of_articles:
    #     article = driver.find_elements(by=By.CLASS_NAME, value='product')
    #
    #     # scroll to bottom to show all elements
    #     footer = driver.find_element(by=By.TAG_NAME, value="footer")
    #     ActionChains(driver).move_to_element(footer).perform()
    #
    #     time.sleep(5)

    for i in range(len(articles)):
        articles = driver.find_elements(by=By.CLASS_NAME, value='product')
        print(articles[i].text)
        articles = driver.find_elements(by=By.CLASS_NAME, value='product')
        highlight_element(driver, articles[i])

        articles[i].click()
        time.sleep(1)
        store_name = driver.find_element(by=By.CLASS_NAME, value='merchant-name')
        store_element = driver.find_element(by=By.CLASS_NAME, value='seller-store')
        highlight_element(driver, store_element)
        print("Seller:  " + store_name.text + "\n\n")
        driver.execute_script("window.history.go(-1)")
        time.sleep(2)

        # scroll_to_element(driver, articles[i])
        # unhighlight_element(driver, article)

    time.sleep(2)
    driver.quit()


if __name__ == "__main__":
    main()
