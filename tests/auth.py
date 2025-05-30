import time

import Utilites
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

        wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@cmpparse='Edit'])[1]"))).send_keys(self.username)
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//input[@cmpparse='Edit'])[2]"))).send_keys(self.password)
        wait.until(EC.element_to_be_clickable((By.XPATH, "(//*[contains(text(), 'Войти')])[2]"))).click()

        time.sleep(2)

        self.driver.find_element(By.XPATH, "//div[@name='LPU']//input/../..//div[@class='cmbb-button']").click()
        self.driver.find_element(By.XPATH, "//span[text()='6202 - Министерство Здравоохранения Республики Татарстан \"Республиканская Клиническая Офтальмологическая Больница\"']").click()
        self.driver.find_element(By.XPATH, "//div[@name='Btn']//div[text()='Выбор']").click()
