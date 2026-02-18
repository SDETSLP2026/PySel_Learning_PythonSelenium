"""
✅ Task 3: NoSuchElementException
URL :- https://www.amcharts.com/svg-maps/?map=india
Action to Perform: Try to locate a state that does NOT exist
Example:
"Atlantis"
"ABCState"
Code will trigger NoSuchElementException

Goal :- Your goal is to handle that exception.
"""

import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@allure.title("SVG")
@allure.description("To verify the exception when a state is searched which does not exist")
def test_SVG_demo_part4():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    # name(), local-name() - Xpath

    # //*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']

    list_of_states = driver.find_elements(By.XPATH,
                                          "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    state_found = False

    for state in list_of_states:

        # To print list of all states
        # print(state.get_attribute("aria-label"))

        if "ABCState  " in state.get_attribute("aria-label"):
            state.click()
            state_found = True
            break

    if not state_found:
        raise NoSuchElementException("State 'ABCState' does not exist on the map")

    time.sleep(10)

    driver.quit()
