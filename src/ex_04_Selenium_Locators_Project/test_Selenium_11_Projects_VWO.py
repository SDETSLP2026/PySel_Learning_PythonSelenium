import time
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Negative TC: app.vwo.com - Wrong Email/Passowrd -> Capture & verify the error message shown.")
@allure.description("To verify that the error message is shown if incorrect credentials are given.")
def test_verify_login_app_VWO():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    # Interact with input box of username and password - Enter incorrect credentials
    # Click on the submit button
    # After waiting for some time, verify the error message.

    # These are the valid locators -
    # email_id = driver.find_element(By.ID, "login-username")
    # email_id = driver.find_element(By.XPATH, "//input[@id='login-username']")
    # email_id = driver.find_element(By.XPATH, "//input[@name='username']")
    email_id = driver.find_element(By.XPATH, "//input[@data-qa='hocewoqisi']")
    email_id.send_keys("wrongusername@testmail.com")

    password = driver.find_element(By.XPATH, "//input[@id='login-password']")
    password.send_keys("wrongPassword")

    sign_in = driver.find_element(By.ID, "js-login-btn")
    sign_in.click()

    time.sleep(5)

    # Error Message validation - "Your email, password, IP address or location did not match"
    err_msg = driver.find_element(By.XPATH, "//div[@class='notification-box-description']")
    print(err_msg.text)
    assert err_msg.text == "Your email, password, IP address or location did not match"

    time.sleep(2)
    driver.quit()
