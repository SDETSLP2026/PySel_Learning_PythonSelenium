"""
## Mini Project Selenium. #1
1. navigate to this website - ﻿[katalon-demo-cura.herokuapp.com/](https://katalon-demo-cura.herokuapp.com/)
2. Open this and verify that this test exists on the page.
    >> Verify that this exist
> CURA Healthcare Service
>
"""

import pytest
import allure
from selenium import webdriver

@allure.title("Print the page source of the web-page")
def test_selenium():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/") # Navigate to URL
    page_source_as_html = driver.page_source
    print("The webpage title is => ", driver.title)
    print("The webpage URL is => ",driver.current_url)

    assert "CURA Healthcare Service" in page_source_as_html

    driver.quit() # To closer all the instances of the browsers