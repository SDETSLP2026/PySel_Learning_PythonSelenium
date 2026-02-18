import allure
from selenium import webdriver

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@allure.title("Actions - Mouse Events")
@allure.description("Verify Click and Hold")

def test_mouse_click_and_hold():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    # Click on draggable
    draggable = driver.find_element(By.ID, "draggable")
    droppable = driver.find_element(By.ID, "droppable")
    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold - Actions Chains - Click and Hold (don'T RELEASE)

    time.sleep(2)

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=draggable).move_to_element(to_element=droppable).perform()

    time.sleep(2)
    driver.quit()
