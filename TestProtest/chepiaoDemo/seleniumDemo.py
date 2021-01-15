from selenium import webdriver

driver = webdriver.Firefox(executable_path="E:\geckodriver")

driver.get("https://kyfw.12306.cn/otn/resources/login.html")

driver.find_element_by_link_text("账号登录").click()