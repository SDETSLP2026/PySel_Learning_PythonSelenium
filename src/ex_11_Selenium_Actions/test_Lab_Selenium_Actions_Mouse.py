import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions - Mouse events")
@allure.description("Verify Mouse events")
def test_verify_actions_mouse():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")
    driver.maximize_window()

    # To click on "Click for Results Page" link

    click_for_results_page = driver.find_element(By.ID, "click")
    click_for_results_page.click()
    time.sleep(2) # This is to ensure redirection happened

    # Move back to previous page using mouse actions - Actions Builder class

    actions_builder = ActionBuilder(driver=driver)
    actions_builder.pointer_action.pointer_up(MouseButton.BACK)
    actions_builder.perform()

    # driver.back()

    time.sleep(5) # This is to ensure return on the page

    driver.quit()