from selenium.webdriver.common.by import By


def get_title(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='product-info-product-name').text


def get_brand(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='brand-name').text


def get_description(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='product-feature').text


def get_price(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='selling-price').text


def get_category(driver, mp):
    if mp.id == "TRENDYOL_DE":
        category = "["
        subcategories = driver.find_elements(by=By.CLASS_NAME, value='product-detail-new-breadcrumbs-item')

        for i in range(len(subcategories) - 1):
            if "schuhe" in subcategories[i].text:
                return "shoes"
            if "socken" in subcategories[i].text:
                return "socks"
            if "pullover" or "sweatshirt" or "hoodie" in subcategories[i].text:
                return "pullovers & hoodies"
            if "t-shirt" or "tshirt" in subcategories[i].text:
                return "t-shirt"

            category += subcategories[i].text + ","
        return category.rstrip(',') + "]"


def get_seller(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return driver.find_element(by=By.CLASS_NAME, value='merchant-name').text


def get_published_at(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return ""


def get_image_url(driver, mp):
    if mp.id == "TRENDYOL_DE":
        return (driver.find_element(by=By.CLASS_NAME, value='carousel-item').find_element(by=By.TAG_NAME, value='div')
                .find_element(by=By.TAG_NAME, value='img').get_attribute('src'))
