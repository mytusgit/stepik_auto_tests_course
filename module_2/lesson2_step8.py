from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение полей
    firstName = browser.find_element(By.NAME, "firstname")
    firstName.send_keys("Ivan")
    lastName = browser.find_element(By.NAME, "lastname")
    lastName.send_keys("Ivanov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("Ivanov")

    # Отправка файла
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    fileElement = browser.find_element(By.ID, "file")
    fileElement.send_keys(file_path)

    # Нажимаем кнопку
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()
    time.sleep(5)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
