import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Home import SwagLabHomePage
from PageClasses.Login1 import SwagLabLoginPage
from TestClasses.conftest import openbrowser
from UtilityFiles.customLogger import LogGen
from UtilityFiles.readProperties import ReadConfig
from UtilityFiles.ReadExcel import ReadTD


class Test_SwagLagLogin:
    logger=LogGen.loggen()

    def loginToApp(self,openbrowser):
        driver = openbrowser
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppUsername())
        login.enterPassword(ReadConfig.getAppPassword())
        login.clickOnLoginBtn()

    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")

        driver=openbrowser
        self.loginToApp(driver)

        actTitle=driver.title
        expTilte=ReadTD.getTestData(1,1)

        if actTitle==expTilte:
            assert True
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(5)
        driver.quit()


    def test_TC2_Verify_ProductName(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC2_Verify_ProductName-------")

        driver = openbrowser
        self.loginToApp(driver)
        time.sleep(3)

        home=SwagLabHomePage(driver)
        actProdctName=home.getBackpackProductName()
        expProductName=ReadTD.getTestData(2,1)

        if actProdctName==expProductName:
            assert True
            self.logger.info("----Passed- Act & Exp product Name match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC2_Verify_ProductName.png")
            self.logger.error("----Failed- Act & Exp product Name mist-match----")
            assert False
        time.sleep(5)
        driver.quit()



