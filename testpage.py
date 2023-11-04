import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# from Page_Objects.Login_page import Login_page
from page_objects import Login_page

driver=webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

Login_page_object=Login_page(driver)
Login_page_object.enter_username()
Login_page_object.enter_password()
Login_page_object.login_button_click()

