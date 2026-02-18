import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Working with windows")
@allure.description("Switching between windows")
def test_verify_windows():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    parent_window_handle = driver.current_window_handle
    print("\n The parent window handle ID is -> ",parent_window_handle)

    # click_here_link = driver.find_element(By.XPATH, "//a[contains(text()='Click Here')]")
    click_here_link = driver.find_element(By.LINK_TEXT, "Click Here")
    click_here_link.click()

    window_handles = driver.window_handles
    print("\n The open window handles are -> ",window_handles)

    for handle in window_handles:
        if handle != parent_window_handle:
            driver.switch_to.window(handle)
            time.sleep(2)
            if "New Window" in driver.page_source:
                print("TC Pass -> New open window is found. ")
                break

            # driver.switch_to.window(window_handles[1])