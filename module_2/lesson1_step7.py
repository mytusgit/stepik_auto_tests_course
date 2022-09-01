from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем картинку
    el_picture = browser.find_element(By.ID, "treasure")

    # Считывание x и вычисление ответа
    x_element = el_picture.get_attribute("valuex")
    x = x_element
    print(x)
    y = calc(x)

    # Ввод ответа
    y_element = browser.find_element(By.CSS_SELECTOR, "#answer")
    y_element.send_keys(y)

    # Отмечаем checkbox и radiobutton
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
    button.click()
    time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
