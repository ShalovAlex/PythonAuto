import time
import unittest
from selenium import webdriver
from auth import Auth  # Импортируйте класс Auth

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.auth = Auth(self.driver, 'rkbshalov', 'Alesha123')  # Передайте логин и пароль

    def test_example(self):
        self.auth.log_in()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()