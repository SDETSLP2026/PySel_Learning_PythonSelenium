"""
Mini Project #1 (Selenium)
// Locators - Find the Web elements
// Open the URL https://app.vwo.com/#/login
// Find the Email id** and enter the email as admin@admin.com
// Find the Pass inputbox** and enter passwrod as admin.
// Find and Click on the submit button
// Verify that the error message is shown "_**Your email, password, IP address or location did not match"**_
"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_appVWO_Negative():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://app.vwo.com/#/login")

    email_id_input_box = driver.find_element(By.NAME, "username")
    email_id_input_box.send_keys("admin@admin.com")

    password_input_box = driver.find_element(By.NAME, "password")
    password_input_box.send_keys("admin")

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()

    time.sleep(2)

    error_message = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message.text)

    time.sleep(5)

    assert "Your email, password, IP address or location did not match" == error_message.text

    driver.quit()