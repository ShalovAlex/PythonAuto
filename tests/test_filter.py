from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class OpenTest:
    def __init__(self, driver):
        self.driver = driver

    def open_hpn(self):
        wait = WebDriverWait(self.driver, 10)

        element1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Учет']")))
        element1.click()

        element2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Нозологические регистры']")))
        element2.click()

        element3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Регистр ХПН']")))
        element3.click()

class FilterTest:
    def __init__(self, driver):
        self.driver = driver

    def test_filter_by_date(self):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем кликабельности элемента и кликаем
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'больных')]")))
        element.click()

        # Выбор даты "3"
        input_field1 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@onclick='return showCalendar(this);'])[1]"))
        )
        input_field1.click()
        date_cell = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[text()='3']")))
        date_cell.click()

        # Выбор даты "4"
        input_field2 = wait.until(
            EC.element_to_be_clickable((By.XPATH, "(//div[@onclick='return showCalendar(this);'])[2]"))
        )
        input_field2.click()
        date_cell2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//td[text()='4']")))
        date_cell2.click()

        # Нажатие "Отобрать"
        button_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[text()='Отобрать'])[1]")))
        button_filter.click()

        try:
            # Проверка наличия элемента "Авто Проверка Тест"
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//span[text()='Авто Проверка Тест'])[1]")
            ))
            print("Элемент найден на странице")

        except Exception as e:
            print(f"Ошибка при работе с элементом: {str(e)}")
            self.driver.save_screenshot("error_screenshot.png")  # Используйте self.driver вместо driver