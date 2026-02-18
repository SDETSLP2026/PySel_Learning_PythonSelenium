import time
import selenium
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@allure.title("Negative TC: app.vwo.com - Wrong Email/Passowrd -> Capture & verify the error message shown.")
@allure.description("To verify that the error message is shown if incorrect credentials are given.")
def test_verify_login_app_VWO():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    driver.maximize_window()

    # Click on - Start a free trial link
    # Get the current page url & check if it contains - 'free-trial' word

    # start_a_free_trial = driver.find_element(By.XPATH, "//a[@vwo-html-translate='login:startFreeTrial']")
    # start_a_free_trial = driver.find_element(By.LINK_TEXT, "Start a free trial")
    start_a_free_trial = driver.find_element(By.PARTIAL_LINK_TEXT, "Start")
    start_a_free_trial.click()

    time.sleep(5)

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    print("To print all the links present on this page: ")
    all_links_page = driver.find_elements(By.TAG_NAME, "a")
    print("Count of all links on the webpage: ", len(all_links_page))
    for i in all_links_page:
        print(i.text)


    time.sleep(2)
    driver.quit()
