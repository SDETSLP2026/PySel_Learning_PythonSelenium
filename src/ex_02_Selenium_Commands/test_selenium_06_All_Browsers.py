import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_edge_current_url_verification():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_firefox_current_url_verification():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

# Sequential run -  pytest .\src\ex_02_Selenium_Commands\test_selenium_06_All_Browsers.py
# Parallel run -  pytest -n auto .\src\ex_02_Selenium_Commands\test_selenium_06_All_Browsers.py