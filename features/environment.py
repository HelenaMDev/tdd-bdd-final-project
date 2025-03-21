"""
Environment for Behave Testing
"""
from os import getenv
from selenium import webdriver

WAIT_SECONDS = int(getenv('WAIT_SECONDS', '30'))
BASE_URL = getenv('BASE_URL', 'http://localhost:5000')
DRIVER = getenv('DRIVER', 'abrowser').lower()


def before_all(context):
    """ Executed once before all tests """
    context.base_url = BASE_URL
    context.wait_seconds = WAIT_SECONDS
    # Select either Chrome or Firefox
    if 'abrowser' in DRIVER:
        context.driver = get_abrowser()
    elif 'firefox' in DRIVER:
        context.driver = get_firefox()
    else:
        context.driver = get_chrome()
    context.driver.implicitly_wait(context.wait_seconds)
    context.config.setup_logging()


def after_all(context):
    """ Executed after all tests """
    context.driver.quit()

######################################################################
# Utility functions to create web drivers
######################################################################

def get_chrome():
    """Creates a headless Chrome driver"""
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    return webdriver.Chrome(options=options)


def get_firefox():
    """Creates a headless Firefox driver"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)    


def get_abrowser():
    """Creates a headless Abrowser driver"""
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    options.binary_location = "/usr/bin/abrowser"  # Path to the Abrowser binary
    return webdriver.Firefox(options=options)    
    
