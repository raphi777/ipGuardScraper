def get_number_of_articles(driver, mp):
    number_of_articles_element = driver.find_element(
        by=mp.number_of_articles_config.by, value=mp.number_of_articles_config.value)

    if mp.id == "TRENDYOL_DE":
        return int(number_of_articles_element.get_attribute(mp.number_of_articles_config.attribute))
