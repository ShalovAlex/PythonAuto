import time
from time import sleep

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

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='btn_caption btn_center minwidth']"))).click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@name='LPU']//input/../..//div[@class='cmbb-button']").click()
        self.driver.find_element(By.XPATH, "//*[starts-with(text(), '6202')]").click()
        self.driver.find_element(By.XPATH, "//div[@name='Btn']//div[text()='Выбор']").click()

        time.sleep(3)

        self.driver.find_element(By.XPATH, "//span[text()='Учет']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Нозологические регистры']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Регистр ХПН']").click()

