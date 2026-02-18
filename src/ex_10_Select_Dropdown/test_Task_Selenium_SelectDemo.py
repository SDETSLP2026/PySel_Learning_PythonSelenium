"""
✅ Task 1:  Select box Automation.
Application URL: https://awesomeqa.com/practice.html
Objective: Automate the interaction with select box elements available on the practice page using Selenium WebDriver
"""


import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Select Demo")
@allure.description("Verify Select Checkbox, Radio, Dropdowns")
def test_select_elements():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.send_keys("Sachin")

    last_name = driver.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Tendulkar")

    gender = driver.find_element(By.XPATH, "//input[@id='sex-0']")
    gender.click()

    yoe = driver.find_element(By.XPATH, "//input[@id='exp-6']")
    yoe.click()

    date = driver.find_element(By.XPATH, "//input[@id='datepicker']")
    date.send_keys("10/01/2026")

    profession = driver.find_element(By.XPATH, "//input[@id='profession-1']")
    profession.click()

    automation_tools = driver.find_element(By.XPATH, "//input[@id='tool-2']")
    automation_tools.click()

    continents = driver.find_element(By.XPATH, "//select[@id='continents']")
    select_dd = Select(continents)
    select_dd.select_by_visible_text("Asia")

    selenium_commands = driver.find_element(By.XPATH, "//select[@id='selenium_commands']")
    select_list = Select(selenium_commands)
    select_list.select_by_visible_text("WebElement Commands")


    time.sleep(5)
    driver.quit()
