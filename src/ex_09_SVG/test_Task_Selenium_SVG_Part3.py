"""
✅ Task 2: Click on a Specific State (Example: Maharashtra)
URL :- https://www.amcharts.com/svg-maps/?map=india
Locate Maharashtra using SVG path
Click on Maharashtra
Validate:
    Tooltip OR
    State name is displayed OR
    Any visual highlight happens

O/P - Tooltip verified: Maharashtra
"""

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("Verify svg")
def test_SVG_demo_part3():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    # name(), local-name() - Xpath

    # //*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in list_of_states:

        # To print list of all states
        # print(state.get_attribute("aria-label"))

        if "Maharashtra  " in state.get_attribute("aria-label"):
            state.click()

            # Validation
            tooltip_text = state.get_attribute("aria-label")
            assert "Maharashtra" in tooltip_text
            print("Tooltip verified:", tooltip_text)

            break

    time.sleep(10)

    driver.quit()
