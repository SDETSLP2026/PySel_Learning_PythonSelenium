import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_webTables_static():
    driver = webdriver.Firefox()
    driver.get("https://awesomeqa.com/webtable.html")
    driver.maximize_window()
    time.sleep(5)

    # This is the static table
    # Rows - //table[@id='customer']/tbody/tr
    row_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr")
    row_count = len(row_elements)
    print("\nTotal row count is -> ", row_count)

    # Col - //table[@id='customer']/tbody/tr[0]/td
    col_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    col_count = len(col_elements)
    print("Total col count is -> ", col_count)

    # To access a particular element
    # //table[@id='customers']/tbody/tr[ - First part
    # 2 - i
    # ]/td[ - Second part
    # 3 - j
    # ] - Third part

    # To create a dynamic xPath
    fp = "//table[@id='customers']/tbody/tr["
    sp = "]/td["
    tp = "]"

    # To traverse within the webtables
    for i in range(2, row_count + 1):  # range(1,10) - 1 to 9
        for j in range(1, col_count + 1):
            dynamic_xpath = f"{fp}{i}{sp}{j}{tp}"
            # print(dynamic_xpath)
            # To print the table data
            data = driver.find_element(By.XPATH, dynamic_xpath).text
            #     print(data, end="  |   ")
        # print() # Just to print on the new line

            # To print Helen Bennett's country
            if "Helen Bennett" in data:
                country_path = f"{dynamic_xpath}/following-sibling::td"
                country_text = driver.find_element(By.XPATH, country_path).text
                print(f"Helen Bennett is living in {country_text}.")

    driver.quit()
