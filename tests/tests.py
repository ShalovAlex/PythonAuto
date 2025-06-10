import time
import unittest
from selenium import webdriver
from auth import Auth  # Убедитесь, что auth.py содержит класс Auth
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_filter import OpenTest, FilterTest
from test_add import AddTest


class TestMyApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.auth = Auth(cls.driver, 'rkbshalov', 'Alesha123')
        cls.auth.log_in()
        # Можно добавить проверку успешного входа

    def setUp(self):
        # Открываем нужный раздел перед каждым тестом
        test_open_register = OpenTest(self.driver)
        test_open_register.open_hpn()

    def test_filter_by_date(self):
        test_filter = FilterTest(self.driver)
        test_filter.test_filter_by_date()

    def test_add_person(self):
        add_test = AddTest(self.driver)
        add_test.test_add_person()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Порядк выполнения тестов
def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    suite.addTest(TestMyApp('test_filter_by_date'))
    suite.addTest(TestMyApp('test_add_person'))
    return suite

if __name__ == "__main__":
    unittest.main()

