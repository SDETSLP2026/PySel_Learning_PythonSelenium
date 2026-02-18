import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Import below 2 settings to add fluent wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


@allure.title("Alerts - JS Alert")
@allure.description("Verify JS Alert")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    click_for_js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    click_for_js_alert.click()

    # Adding explicit wait
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept() # To click on Ok button of the alert pop-up

    result_text = driver.find_element(By.XPATH, "//p[@id='result']").text
    assert result_text == "You successfully clicked an alert"

    time.sleep(5)

@allure.title("Alerts - JS Confirmation Alert")
@allure.description("Verify JS Confirmation Alert")
def test_alerts_js_confirmation_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    click_for_js_confirmation_alert = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    click_for_js_confirmation_alert.click()

    # Adding explicit wait
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.dismiss() # To click on Cancel button of the alert pop-up

    result_text = driver.find_element(By.XPATH, "//p[@id='result']").text
    assert result_text == "You clicked: Cancel"

    time.sleep(5)


@allure.title("Alerts - JS Prompt Alert")
@allure.description("Verify JS Prompt Alert")
def test_alerts_js_prompt_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    click_for_js_prompt_alert = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    click_for_js_prompt_alert.click()

    # Adding explicit wait
    WebDriverWait(driver=driver, timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("PyATB6X")
    alert.accept() # To click on Ok button of the alert pop-up

    result_text = driver.find_element(By.XPATH, "//p[@id='result']").text
    assert result_text == "You entered: PyATB6X"

    time.sleep(5)