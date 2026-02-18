"""
Automate the Dummy Form on the below page - Xpath Practice Page | Shadow dom, nested shadow dom, iframe, nested iframe and more complex automation scenarios.
https://selectorshub.com/xpath-practice-page/

User Email - Enter 'dummyemail@testemail.com'
Password - Enter 'DummyPassword'
Company - Enter 'Demo Company'
Mobile Number - Enter '9876543210'
Country - Enter 'India'
Click on Submit button
"""

import allure
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Form submission")
@allure.description("Enter the given details and Submit the form.")
def test_form_submission():
    driver = webdriver.Edge()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    # Locating all elements
    user_email = driver.find_element(By.XPATH, "//input[@name='email']")
    user_email.send_keys("dummyemail@testemail.com")

    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    password.send_keys("DummyPassword")

    company = driver.find_element(By.XPATH, "//input[@name='company']")
    company.send_keys("Demo Company")

    mobile_number = driver.find_element(By.XPATH, "//input[@name='mobile number']")
    mobile_number.send_keys("987654321")

    country = driver.find_element(By.XPATH, "//label[contains(text(),'Country')]")
    country.send_keys("India")

    # Scroll the element into view before clicking - then only it will work
    submit_button = driver.find_element(By.XPATH, "//button[@value='Submit']")
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

    time.sleep(2)
    driver.quit()
