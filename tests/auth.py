import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Auth:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def log_in(self):
        self.driver.get('http://192.168.241.141/med2des/?f=NoUserForms')
        wait = WebDriverWait(self.driver, 10)

        # Авторизация (логи и пароль)
        input_username = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@cmpparse='Edit' and @type='text']")))
        input_username.click()
        input_username.clear()
        input_username.send_keys(self.username)

        input_password = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@cmpparse='Edit' and @type='password']")))
        input_password.click()
        input_password.clear()
        input_password.send_keys(self.password)

        wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@class='btn_caption btn_center minwidth']"))).click()

        time.sleep(2)

        # Выбор МО и кабинет
        choice_mo = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@name='LPU']//input/../..//div[@class='cmbb-button']")))
        choice_mo.click()

        cabinet_selection = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[starts-with(text(), '6202')]")))
        cabinet_selection.click()

        entrance_to_mo = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@name='Btn']//div[text()='Выбор']")))
        entrance_to_mo.click()

        time.sleep(3)

        # Проверка входа
        try:
            # Проверка захода под пользователем
            profile_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//td[text()='Шалов Алексей Владимирович (62028919)']"))
            )
            if profile_element.is_displayed():
                print("Вход в МО выполнен")
            else:
                raise Exception("Вход в МО не выполнен")
        except Exception as e:
            print("Ошибка при входе:", e)
            self.driver.save_screenshot("login_failed.png")
            raise



