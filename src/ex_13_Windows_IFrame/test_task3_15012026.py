"""
Automate the Payment Page section - Xpath Practice Page | Shadow dom, nested shadow dom, iframe, nested iframe and more complex automation scenarios.
https://selectorshub.com/xpath-practice-page/

Name on Card - "Jackson Thompson"
Card Number - "4047584829451267"
Expiry Date - "02/31"
CVV - "840"
Click on Pay Rs.999 button

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

    # Scroll down & Locating form and elements
    form_heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Payment Details')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", form_heading)

    name_on_card = driver.find_element(By.ID, "cardName")
    name_on_card.send_keys("Jackson Thompson")

    card_number = driver.find_element(By.ID, "cardNumber")
    card_number.send_keys("4047584829451267")

    expiry_date = driver.find_element(By.ID, "expiry")
    expiry_date.send_keys("02/31")

    cvv = driver.find_element(By.ID, "cvv")
    cvv.send_keys("840")

    pay_rs_999 = driver.find_element(By.XPATH, "//button[contains(text(),'Pay ₹999')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", pay_rs_999)
    pay_rs_999.click()

    time.sleep(2)
    driver.quit()
