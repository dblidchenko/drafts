from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Selenium(BasePage):
    URL = 'http://suninjuly.github.io/find_link_text'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Selenium.URL)

    def try_find_link(self, code):
        # знаходимо потрібний лінк
        input1 = self.driver.find_element(By.LINK_TEXT, code)
        input1.click()

        # знаходимо кнопку
        # btn_elem = self.driver.find_element(By.ID, 'submit_button')

        # тиснемо
        # btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
