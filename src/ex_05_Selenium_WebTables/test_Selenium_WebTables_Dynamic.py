import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webTables_dynamic():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/webtable1.html")
    driver.maximize_window()
    time.sleep(5)

    #Step - 1 - Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")

    # //table[@summary='Sample Table']/tbody/tr
    rows_table = table.find_elements(By.TAG_NAME, "tr")

    for row in rows_table:
        cols = row.find_elements(By.TAG_NAME, "td")
        for col in cols:
            print(col.text)





    driver.quit()
