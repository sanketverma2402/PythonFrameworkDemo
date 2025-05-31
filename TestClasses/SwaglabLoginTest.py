import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Home import SwagLabHomePage
from PageClasses.Login1 import SwagLabLoginPage
from TestClasses.conftest import openbrowser
from UtilityFiles.ReadExcel import ReadTD
from UtilityFiles.customLogger import LogGen
from UtilityFiles.readProperties import ReadConfig


class Test_SwagLagLogin:

    logger=LogGen.loggen()

    def loginToApp(self,driver):
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppUsername())
        login.enterPassword(ReadConfig.getAppPassword())
        login.clickOnLoginBtn()

    @pytest.mark.regression
    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
        driver=openbrowser
        self.loginToApp(driver)

        actTitle=driver.title
        print(actTitle)
        expTilte=ReadTD.getTestData(9,1)

        if actTitle==expTilte:
            assert True
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    @pytest.mark.regression
    def test_TC2_verifyProductName(self, openbrowser):
        self.logger.info("----test_TC2_verifyProductName-------")
        driver = openbrowser
        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProductName=home.getBackpackProductName()
        expProductName=ReadTD.getTestData(2,2)

        if actProductName == expProductName:
            assert True
            self.logger.info("----Passed- Act & Exp product name match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC2_verifyProductName.png")
            self.logger.error("----Failed- Act & Exp product name mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

     #-------------------------------AssignMent No 1-verifyProductPriceTag-------------------------
    @pytest.mark.sanity
    def test_TC3_verifyProductPriceTag(self,openbrowser):
        self.logger.info("-----test_TC3_verifyProductPriceTag---------")
        driver=openbrowser
        self.loginToApp(driver)
        home1=SwagLabHomePage(driver)
        home1.clickOnBikeLightProduct()
        actBikeLightPrice=str(home1.getBikeLightPrice())
        time.sleep(2)
        print(actBikeLightPrice)
        expBikeLightPrice=str(ReadTD.getTestData(3,3))
        print(expBikeLightPrice)
        time.sleep(2)

        if actBikeLightPrice == expBikeLightPrice:
            assert True
            self.logger.info("----Passed- Act & Exp product Price matched----")
        else:
            driver.save_screenshot(".\\SS\\test_TC3_verifyProductPriceTag.png")
            self.logger.error("----Failed- Act & Exp product Price mist-matched----")
            assert False
        time.sleep(3)
        driver.quit()

    # -------------------------------AssignMent No 2-verifyProductSize-------------------------
    @pytest.mark.smoke
    def test_TC4_verifyProductSize(self, openbrowser):
        self.logger.info("-----test_TC4_verifyProductSize---------")
        driver=openbrowser
        self.loginToApp(driver)
        home2=SwagLabHomePage(driver)
        actProductSize=home2.getProductSizeFromHomePage()
        expProductSize=ReadTD.getTestData(8,2)
        if actProductSize == expProductSize:
            assert True
            self.logger.info("----Passed- Act & Exp Product Size matched----")
        else:
            driver.save_screenshot(".\\SS\\test_TC4_verifyProductSize.png")
            self.logger.error("----Failed- Act & Exp product Size Mist-matched----")

        time.sleep(3)
        driver.quit()

    @pytest.mark.functional
    def test_TC5_verifyTotalProductValue(self, openbrowser):
        self.logger.info("-----test_TC5_verifyTotalProductValue---------")
        driver=openbrowser
        self.loginToApp(driver)
        home2=SwagLabHomePage(driver)
        actTotalPrice=home2.totalPriceOfAllProducts()
        expTotalPrice=ReadTD.getTestData(8,3)
        if actTotalPrice == expTotalPrice:
            assert True
            self.logger.info("----Passed- Act & Exp Total Product Price matched----")
        else:
            driver.save_screenshot(".\\SS\\test_TC5_verifyTotalProductValue.png")
            self.logger.error("----Failed- Act & Exp Total Product Price Mist-matched----")

        time.sleep(3)
        driver.quit()






