from selenium.webdriver.chrome.options import Options


def get_standard_options():
    # Configure headless mode
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--window-size=0x0')
    options.add_experimental_option('detach', True)
    return options
