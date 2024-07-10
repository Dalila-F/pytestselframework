
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen


class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_homepageTitle(self, setup):
        self.logger.info("**************************Testing homepage title**********************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**********************************Testing test_login Page***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False


