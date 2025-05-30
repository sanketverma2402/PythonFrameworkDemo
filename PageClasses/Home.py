from selenium.webdriver.common.by import By
from selenium import webdriver

class SwagLabHomePage:

    #1: declare web elements globally
    textBackpackProductXpath="//div[text()='Sauce Labs Backpack']"
    clickSauceLabsBikeLightXpath="//div[text()='Sauce Labs Bike Light']"
    textSauceLabsBikeLightPriceXpath="//div[text()='9.99']"
    totalProductsNameXpath="//div[@class='inventory_item_name ']"
    priceOfProducts="//div[@class='inventory_item_price']"



    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    #3: perform actions
    def getBackpackProductName(self):
        productName=self.driver.find_element(By.XPATH,self.textBackpackProductXpath).text
        return productName

    def getBikeLightPrice(self):
        Price=self.driver.find_element(By.XPATH,self.textSauceLabsBikeLightPriceXpath).text
        BikeLightPrice=Price.strip("$")
        return BikeLightPrice

    def clickOnBikeLightProduct(self):
         self.driver.find_element(By.XPATH,self.clickSauceLabsBikeLightXpath).click()

    def getProductSizeFromHomePage(self):
        AllProducts=self.driver.find_elements(By.XPATH,self.totalProductsNameXpath)
        NoOfProducts=len(AllProducts)
        return NoOfProducts

    def totalPriceOfAllProducts(self):
        price_elements=self.driver.find_elements(By.XPATH,self.priceOfProducts)
        total=0
        for i in price_elements:
            prices=i.text.strip("$")
            prices=float(prices)
            total=total+prices
        return total






