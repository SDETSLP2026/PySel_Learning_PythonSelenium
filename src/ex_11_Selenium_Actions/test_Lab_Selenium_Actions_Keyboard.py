import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_verify_actions_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")

    # The user input should be entered in Caps
    # The shift key should be pressed while entering input, and release once done
    # User ActionChains class for the same


    actions = ActionChains(driver=driver)

    (actions.key_down(Keys.SHIFT)
     .send_keys_to_element(first_name, "the testing academy")
     .key_up(Keys.SHIFT)
     .perform())

    time.sleep(5)
    driver.quit()