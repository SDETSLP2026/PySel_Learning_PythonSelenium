import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("app.vwo.com - Implicit Wait")
@allure.description("To verify that the app.vwo.com is loaded with implicit wait.")
def test_neg_app_vwo_com():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    # Adding Implicit Wait - We will never ever use in our automation
    driver.implicitly_wait(5) # This would be applicable to all the elements

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

    # Error Message validation - "Your email, password, IP address or location did not match"
    err_msg = driver.find_element(By.XPATH, "//div[@class='notification-box-description']")
    print(err_msg.text)
    assert err_msg.text == "Your email, password, IP address or location did not match"

    driver.quit()
