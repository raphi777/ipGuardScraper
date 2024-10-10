from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_title(driver, mp):
    if mp.id == "TRENDYOL_DE":
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'brand-name')))
        # TODO: fix retreival of information
        print(driver.find_element(by=By.CLASS_NAME, value='brand-name').text)
        return driver.find_element(by=By.CLASS_NAME, value='brand-name').text


def get_description(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='product-feature')


def get_price(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='selling-price')


def get_seller(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='merchant-name')


def get_published_at(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return ""


def get_image_url(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return (driver.find_element(by=By.CLASS_NAME, value='carousel-item').find_element(by=By.CLASS_NAME, value='')
                .find_element(by=By.TAG_NAME, value='img').get_attribute('src'))
