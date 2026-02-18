import allure
from selenium import webdriver


@allure.title("To verify that we can open a webpage by using Selenium.")
@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
def test_first_tc():
    driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Ie()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    print(driver.current_url)

    assert driver.title == "TheTestingAcademy | Learn Software Testing and Automation Testing"

    driver.quit()
