# Start by creating our pageobject class that contains our locator objects
# Create pageobject LoginPage that will contains all the elements or objects related to that login page

from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.ID, "Email").clear()
        self.driver.find_element(By.ID, "Email").send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, "Password").clear()
        self.driver.find_element(By.ID, "Password").send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.CLASS_NAME, "login-button").click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()