from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    var = browser.find_element(By.ID, "input_value")
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(calc(var.text))


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()