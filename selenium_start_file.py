from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import math
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # x = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    # javascript = 'input = document.getElementsByTagName("input")[0];input.scrollIntoView(true);'
    # browser.execute_script(javascript)
    # browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('darova')
    # browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('darova')
    # browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('darova')
    # browser.find_element(By.CSS_SELECTOR, '[name="file"]').send_keys(file_path)

    # browser.find_element(By.ID, 'robotsRule').click()
    # button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # button.click()
    # window = browser.switch_to.window(browser.window_handles[1])

    # x = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    # browser.find_element(By.TAG_NAME, 'input').send_keys(calc(x.text))
    # button1 = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    # button1.click()
    # el = WebDriverWait(browser, 12).until(
    #     EC.text_to_be_present_in_element((By.ID, "price"), "100")
    # )
    button = browser.find_element(By.TAG_NAME, "button")
    print(type(button.get_attribute("id")))
    browser.implicitly_wait(1)
    x = browser.find_element(By.ID, 'input_value')
    browser.find_element(By.ID, 'answer').send_keys(calc(x.text))
    button = browser.find_element(By.ID, "solve")
    button.click()
    # alert = browser.switch_to.alert.text
    # print(alert)
finally:

    time.sleep(10)
    browser.quit()
