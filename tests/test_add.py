from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddTest:
    def __init__(self, driver):
        self.driver = driver

    def test_add_person(self):
        wait = WebDriverWait(self.driver, 10)

        # Ожидаем кликабельности элемента и кликаем
        vkluchenie = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'включении')]")))
        print("Нашли элемент включения")
        time.sleep(0.5)
        vkluchenie.click()
        print("Кликнули по включению")

        add_izveshenie = wait.until(EC.element_to_be_clickable((By.XPATH, "(//td[text()='Создать извещение'])[1]")))
        print("Нашли кнопку 'Создать извещение'")
        add_izveshenie.click()
        print("Кликнули по 'Создать извещение'")

        try:
            # Проверка открытия формы
            profile_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='WinTitle Title']"))
            )
            if profile_element.is_displayed():
                print("Карта на создание Регистра ХПН открылась")
            else:
                raise Exception("Карта на создание Регистра ХПН не отображается.")
        except Exception as e:
            print("Ошибка при открытии формы:", e)
            self.driver.save_screenshot("form_opening_failed.png")
            raise