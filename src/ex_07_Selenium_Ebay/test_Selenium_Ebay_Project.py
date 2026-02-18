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


@allure.title("Print the Titles of the Ebay sites after searching")
@allure.description("Verify that 62 items are there for macmini")
def test_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.com/b/Desktops-All-In-One-Computers/171957/bn_1643067")
    driver.maximize_window()

    search_box_input_xpath = driver.find_element(By.XPATH, "//input[@placeholder='Search for anything']")
    search_box_input_xpath.send_keys("macmini")
    search_button = driver.find_element(By.XPATH, "//span[@class='gh-search-button__label']")
    search_button.click()

    #//div[@class = "s-item__title"] -> div.s-item__title - class is represented by .

    titles = driver.find_elements(By.CSS_SELECTOR, ".s-item__title")
    prices = driver.find_elements(By.CSS_SELECTOR, ".s-item__price")

    # for items in list_of_items:
    #     print(items.text)
    #
    # for items_price in list_of_item_prize:
    #     print(items_price.text)

    title_texts = [title.text for title in titles] # to convert web element to list
    price_texts = [price.text for price in prices] # to convert web element to list

    for text,price in zip(title_texts, price_texts):  # to combine two lists
        #for price in price_texts:
        print(text, price)

    time.sleep(5)
    driver.quit()