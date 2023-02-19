from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class BasePage:
    PATH = r"/Users/dima/Documents/Python_basics/GitHub/QA_Auto_23/"
    DRIVER_NAME = "chromedriver"
    # властивості класу

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service=Service(BasePage.PATH + BasePage.DRIVER_NAME)
        )

    def close(self):
        self.driver.close()
