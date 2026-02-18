"""
// Locators - Find the Web elements
// Open the URL https://www.idrive360.com/enterprise/login
// Find the Email id** and enter the email as augtest_040823@idrive.com
// Find the Pass inputbox** and enter 123456 .
// Find and Click on the sign in button
// Verify that the error message is shown "Your free trial has expired!"

"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_iDrive360():

    # If the test need to run with Chrome browser
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # driver = webdriver.Edge(options=chrome_options)

    # If the test need to run with Edge browser
    driver = webdriver.Edge()
    driver.maximize_window()

    driver.get("https://www.idrive360.com/enterprise/login")

    time.sleep(5)

    inputBox_email_id = driver.find_element(By.NAME, "username")
    inputBox_email_id.send_keys("augtest_040823@idrive.com")

    inputBox_password = driver.find_element(By.NAME, "password")
    inputBox_password.send_keys("123456")

    button_sign_in = driver.find_element(By.ID, "frm-btn")
    button_sign_in.click()

    time.sleep(20)

    act_error_message = driver.find_element(By.CLASS_NAME, "id-card-title")

    assert "Your free trial has expired!" == act_error_message.text

    driver.quit()
