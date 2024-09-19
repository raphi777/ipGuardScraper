from marketplace.marketplace import Marketplace
from marketplace.mp_cookies_config import CookiesConfig
from marketplace.mp_number_of_articles_config import NumberOfArticlesConfig
from selenium.webdriver.common.by import By

TRENDYOL_DE = Marketplace(
    "TRENDYOL_DE",
    CookiesConfig(By.ID, "onetrust-accept-btn-handler"),
    NumberOfArticlesConfig(By.CLASS_NAME, "search-result", "data-resultcount")
)
