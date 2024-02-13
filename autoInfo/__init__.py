from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class Search:
    def __init__(self):
        self.driver = None
        self._BASE_URL = "https://vin01.ru/"

    def get_vin_by_number(self, car_number):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self._BASE_URL)

        time.sleep(2)

        input_form = self.driver.find_element(By.ID, "num")
        input_form.click()
        input_form.send_keys(car_number)

        time.sleep(1.5)

        find_button = self.driver.find_element(By.ID, "searchByGosNumberButton")
        find_button.click()

        time.sleep(1.5)
        try:
            vin = self.driver.find_element(By.ID, "vinNumbers").text
        except Exception as e:
            close = self.driver.find_element(By.CLASS_NAME, "close")
            close.click()
            vin = self.get_vin_by_number(car_number)
        self.driver.close()
        return vin

    def get_car_data_by_number(self, car_number):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self._BASE_URL)

        time.sleep(2)
        input_form = self.driver.find_element(By.ID, "num")
        input_form.click()
        input_form.send_keys(car_number)

        time.sleep(2.5)
        find_button = self.driver.find_element(By.ID, "searchByGosNumberButton")
        find_button.click()

        time.sleep(2.5)
        try:
            vin = self.driver.find_element(By.ID, "vinNumbers").text
        except Exception as e:
            close = self.driver.find_element(By.CLASS_NAME, "close")
            close.click()
            vin = self.get_car_data_by_number(car_number)
        time.sleep(1.5)

        ind = 0
        car_reg = ""
        while ind <= 7:
            time.sleep(2)

            select_element = self.driver.find_element(By.ID, 'checkType')

            elements = select_element.text.split("\n")
            cur_elem = elements[ind]

            select = Select(select_element)

            select.select_by_visible_text(cur_elem)

            check_btn = self.driver.find_element(By.ID, "getCheckButton")
            check_btn.click()

            time.sleep(12)

            modal = self.driver.find_element(By.ID, "modal-body")
            data = str(modal.text).split("\n")

            info = data[0]
            if info != 'Не удалось получить данные с сервера! Пожалуйста повторите запрос позднее.':
                if info != 'Произошла ошибка при выполнении запроса. Попробуйте позднее!':
                    ind += 1
                if info != 'undefined' and cur_elem != 'Поиск судебных решений':
                    car_reg += cur_elem + "\n"
                    car_reg += "\n".join(data[:-13]) + "\n"
        self.driver.close()
        return car_reg

    def get_car_data_vin(self, car_vin):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(self._BASE_URL)

        vin_input = self.driver.find_element(By.ID, "vinToggleButton")
        vin_input.click()

        time.sleep(2)
        input_form = self.driver.find_element(By.ID, "vinNumber")
        input_form.click()
        input_form.send_keys(car_vin)

        time.sleep(2.5)
        find_button = self.driver.find_element(By.ID, "searchByVinNumberButton")
        find_button.click()

        time.sleep(2.5)
        try:
            vin = self.driver.find_element(By.ID, "vinNumbers").text
        except Exception as e:
            close = self.driver.find_element(By.CLASS_NAME, "close")
            close.click()
            vin = self.get_car_data_vin(car_vin)
        time.sleep(1.5)

        ind = 0
        car_reg = ""
        while ind <= 7:
            time.sleep(2)

            select_element = self.driver.find_element(By.ID, 'checkType')

            elements = select_element.text.split("\n")
            cur_elem = elements[ind]

            select = Select(select_element)

            select.select_by_visible_text(cur_elem)

            check_btn = self.driver.find_element(By.ID, "getCheckButton")
            check_btn.click()

            time.sleep(12)

            modal = self.driver.find_element(By.ID, "modal-body")
            data = str(modal.text).split("\n")

            info = data[0]
            if info != 'Не удалось получить данные с сервера! Пожалуйста повторите запрос позднее.':
                if info != 'Произошла ошибка при выполнении запроса. Попробуйте позднее!':
                    ind += 1
                if info != 'undefined' and cur_elem != 'Поиск судебных решений':
                    car_reg += cur_elem + "\n"
                    car_reg += "\n".join(data[:-13]) + "\n"
        self.driver.close()
        return car_reg