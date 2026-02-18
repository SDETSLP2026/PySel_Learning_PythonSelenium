import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException

@allure.title("Exception Handling")
@allure.description("To verify exception handling")
def test_exception_handling():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    try:
        element = driver.find_element(By.ID, "this_id_doesnt_exist") #The element which doesnot exist
    except NoSuchElementException as nse:
        print(nse.msg)

        # response =
        # {'status': 404, 'value': '
        # {"value":{"error":"no such element","message":
        # "no such element: Unable to locate element:

        # NoSuchElementException