import time
import unittest
from selenium import webdriver
from auth import Auth  # Импортируйте класс Auth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class TestMyApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.auth = Auth(cls.driver, 'rkbshalov', 'Alesha123')
        cls.auth.log_in()

    def test_filter_by_date(self):
        wait = WebDriverWait(self.driver, 10)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'больных')]")))
        time.sleep(0.5)
        element.click()

        input_field1 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@onclick='return showCalendar(this);'])[1]")))
        input_field1.click()
        input_field1 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//td[text()='3']")))
        input_field1.click()

        input_field1 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//div[@onclick='return showCalendar(this);'])[2]")))
        input_field1.click()
        input_field1 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//td[text()='4']")))
        input_field1.click()

        element1 = wait.until(EC.visibility_of_element_located((By.XPATH, "(//td[text()='Отобрать'])[1]")))
        element1.click()

        try:
            # Проверяем наличие элемента
            element = wait.until(EC.presence_of_element_located(
                (By.XPATH, "(//span[text()='Авто Проверка Тест'])[1]")
            ))
            print("Элемент найден на странице")

            # Проверяем, что элемент видимый
            if element.is_displayed():
                print("Элемент отображается на странице")

                # Дожидаемся кликабельности
                element = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "(//span[text()='Авто Проверка Тест'])[1]")
                ))
                time.sleep(0.5)  # небольшая пауза для стабильности

                # Выполняем клик
                element.click()
                print("Клик по элементу выполнен успешно")
            else:
                print("Элемент присутствует в DOM, но не отображается на странице")
                raise Exception("Элемент не видим для взаимодействия")

        except Exception as e:
            print(f"Ошибка при работе с элементом: {str(e)}")
            # Можно сделать скриншот для отладки
            self.driver.save_screenshot("error_screenshot.png")
            raise  # повторно поднимаем исключение, чтобы тест упал

    @classmethod
    def tearDownClass(cls):
        # Закрываем браузер после всех тестов
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
