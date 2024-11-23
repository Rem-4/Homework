from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements():
    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/")

    username_field = driver.find_element(By.NAME,"username")
    password_field = driver.find_element(By.NAME,"password")
    submit_button = driver.find_element(By.CSS_SELECTOR,"button[type='submit']")

    if username_field and password_field and submit_button:
        print("Элементы найдены")
    else:
        print("Элементы не найдены")
