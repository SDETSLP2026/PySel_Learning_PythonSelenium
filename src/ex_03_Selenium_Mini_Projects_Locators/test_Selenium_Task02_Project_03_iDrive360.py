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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_iDrive360():

    # # If the test need to run with Chrome browser
    # chrome_options = Options()
    # chrome_options.add_argument("--start-maximized")
    # driver = webdriver.Edge(options=chrome_options)

    # If the test need to run with Edge browser
    driver = webdriver.Firefox()
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

    # act_error_message = driver.find_element(By.CLASS_NAME, "id-card-title")
    # print(act_error_message.text)
    # assert "Your free trial has expired!" == act_error_message.text

    payment_info_form = driver.find_element(By.XPATH, "//div[@id='payment1']//fieldset[@class='id-fldst-crd']")
    driver.execute_script("arguments[0].scrollIntoView(true);", payment_info_form)

    # ---------- Testing of Payment Information form on Dashboard page
    # Switching to iFrame

    # Wait until any Stripe iframe is present
    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[name^='__privateStripeFrame']"))
    )
    driver.switch_to.frame(iframe)

    card_number = driver.find_element(By.XPATH, "//input[@name='cardNumber']")
    card_number.send_keys("4047584829451267")

    exp_date = driver.find_element(By.XPATH, "//input[@name='exp-date']")
    exp_date.send_keys("02/31")

    cvc_number = driver.find_element(By.XPATH, "//input[@name='cvc']")
    cvc_number.send_keys("840")



    time.sleep(5)

    driver.quit()
