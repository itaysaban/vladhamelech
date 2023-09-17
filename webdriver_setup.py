from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = 'http://localhost/'


def driver_setup():
    options = ChromeOptions()
    service = ChromeService(ChromeDriverManager().install())
    options.add_experimental_option('detach', True)
    options.add_argument('--disable-extentions')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


if __name__ == '__main__':
    driver = driver_setup()
    driver.get(url)
