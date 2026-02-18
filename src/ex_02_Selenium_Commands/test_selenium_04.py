import allure
from selenium import webdriver


@allure.title("Print the Page Source of the page.")
def test_selenium():
    # Selenium 4
    driver = webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print(driver.page_source)