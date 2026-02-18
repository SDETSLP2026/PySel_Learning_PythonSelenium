"""
Task 1 - The Internet - http://the-internet.herokuapp.com/windows

1. Open the above URL
2. From the parent page, click on the "Click Here" button.
3. The moment you click on that button, it will open a child page, which is another tab.
4. You need to switch to that tab and verify that there is a particular text available on the page source - yes or no.
5. Then, if you want, you can switch back to the parent as well.
"""

import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


@allure.title("Windows switching demo")
@allure.description("This will demonstrate you how to switch between windows and return to home window")
def test_windows_switching():
    driver = webdriver.Edge()

    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    # 1. Capture parent window handle & print it
    parent_window_handle = driver.current_window_handle
    print("\n The parent window handle ID is -> ", parent_window_handle)

    # 2. Click on the 'Click here' link
    link_click_here = driver.find_element(By.XPATH, "//a[contains(normalize-space(),'Click Here')]")
    link_click_here.click()

    # 3. Capture all the window handles that are opened after a click event
    all_window_handles = driver.window_handles
    print("\n The open window handles are -> ", all_window_handles)

    # 4. Check each opened handle (only if it is not the parent handle) - switch to that window
    for handle in all_window_handles:
        if handle != parent_window_handle:
            driver.switch_to.window(handle)
            time.sleep(2)

            text_new_window = driver.find_element(By.XPATH, "//h3[contains(normalize-space(),'New Window')]").text
            assert "New Window" in text_new_window

    time.sleep(2)
    driver.quit()
