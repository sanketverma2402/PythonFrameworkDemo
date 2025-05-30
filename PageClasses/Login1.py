from selenium.webdriver.common.by import By
from selenium import webdriver


class SwagLabLoginPage:

    #1: declare web elements globally
    inpUsernameXpath="//input[@id='user-name']"
    inpPasswordXpath = "//input[@id='password']"
    clickLoginXpath = "//input[@id='login-button']"

    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    #3: perform actions
    def enterUsername(self,UnValue):
        self.driver.find_element(By.XPATH,self.inpUsernameXpath).send_keys(UnValue)

    def enterPassword(self,PwdValue):
        self.driver.find_element(By.XPATH,self.inpPasswordXpath).send_keys(PwdValue)

    def clickOnLoginBtn(self):
        self.driver.find_element(By.XPATH, self.clickLoginXpath).click()