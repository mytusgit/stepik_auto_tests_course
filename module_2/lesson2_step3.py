from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считаем сумму
    num1_el = browser.find_element(By.ID, "num1")
    num2_el = browser.find_element(By.ID, "num2")
    sumNum = int(num1_el.text) + int(num2_el.text)
    sumNum_strVal = str(sumNum)

    # Выбираем значение в списке
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(sumNum_strVal)

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
