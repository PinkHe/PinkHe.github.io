from selenium import webdriver

driver = webdriver.Firefox(executable_path="E:\geckodriver")

driver.get("https://kyfw.12306.cn/otn/resources/login.html")


search_input = driver.find_element_by_id("kw")
search_input.clear()
search_input.send_keys("")

driver.find_element_by_id("su").click()