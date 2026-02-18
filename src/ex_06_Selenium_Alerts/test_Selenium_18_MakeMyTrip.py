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

@allure.title("Modal")
@allure.description("Verify Modal")
def test_alerts_js_alert():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()

    # Adding explicit wait
    WebDriverWait(driver=driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Mobile Number']")))

    mobile_no = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    mobile_no.send_keys("8793676667")

    continue_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_btn.click()