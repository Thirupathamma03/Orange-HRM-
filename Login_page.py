from selenium import webdriver
from selenium.webdriver.common.by import By
class Login_page:
    def __init__(self, driver):
        self.driver=driver
        self.username_textbox_locator="username"
        self.password_textbox_locator="password"
        self.login_button_locator="//button[@type='submit']"
        self.invalid_credentials="//p[text()='Invalid credentials']"

    def enter_username(self):
        self.driver.find_element(By.NAME,self.username_textbox_locator).send_keys("Admin")

    def enter_password(self):
        self.driver.find_element(By.NAME,self.password_textbox_locator).send_keys("admin123")

    def login_button_click(self):
        self.driver.find_element(By.XPATH,self.login_button_locator).click()

    def invalid_credentials(self):
        self.driver.find_element(By.XPATH,self.invalid_credentials)
