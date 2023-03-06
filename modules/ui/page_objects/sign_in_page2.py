from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class Selenium(BasePage):
    URL = 'http://suninjuly.github.io/simple_form_find_task.html'

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(Selenium.URL)

    def try_fill_in_simple_form(self, firstname, lastname, city, country):
        # знаходимо поле, в яке будемо вводити імʼя користувача
        fname_elem = self.driver.find_element(By.NAME, 'first_name')

        # вводимо неправильне імʼя користувача
        fname_elem.send_keys(firstname)

        # знаходимо поле, в яке будемо вводити прізвище
        lname_elem = self.driver.find_element(By.NAME, 'last_name')

        # вводимо неправильне прізвище
        lname_elem.send_keys(lastname)

        # знаходимо поле, в яке будемо вводити місто користувача
        email_elem = self.driver.find_element(By.NAME, 'firstname')

        # вводимо місто
        email_elem.send_keys(city)

        # знаходимо поле, в яке будемо вводити країну
        pass_elem = self.driver.find_element(By.ID, 'country')

        # вводимо країну
        pass_elem.send_keys(country)

        # знаходимо кнопку
        # btn_elem = self.driver.find_element(By.ID, 'submit_button')

        # тиснемо
        # btn_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title
