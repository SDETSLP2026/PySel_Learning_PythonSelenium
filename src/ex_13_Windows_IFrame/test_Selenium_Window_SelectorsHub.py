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
    driver.get("https://selectorshub.com/iframe-scenario/")
    driver.maximize_window()

    driver.switch_to.frame("pact1")

    crush_finder_input_box= driver.find_element(By.XPATH, "//input[@id='inp_val']")
    crush_finder_input_box.send_keys("Swapnil")

    driver.switch_to.frame("pact2")

    jex_input_box = driver.find_element(By.XPATH, "//input[@id='jex']")
    jex_input_box.send_keys("Padekar")

    # To switch back to previous frame - first shift to Parent frame and then to pact1
    driver.switch_to.default_content() # To parent frame

    # Again switching to iFrame pact1
    driver.switch_to.frame("pact1")

    crush_finder_input_box= driver.find_element(By.XPATH, "//input[@id='inp_val']")
    crush_finder_input_box.clear()
    crush_finder_input_box.send_keys("Snehal")

    time.sleep(5)