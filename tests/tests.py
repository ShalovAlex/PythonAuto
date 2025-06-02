import time
import unittest
from selenium import webdriver
from auth import Auth  # Импортируйте класс Auth

class TestMyApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.auth = Auth(cls.driver, 'rkbshalov', 'Alesha123')
        cls.auth.log_in()

    def test_way_to_IKBR(cls):

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()