from email.policy import default

import pytest
from  selenium import  webdriver
from selenium.webdriver.chrome.options import Options

from UtilityFiles.readProperties import ReadConfig


#step3: modify fixture for multiple browser
@pytest.fixture
def openbrowser(browser):
    if browser == "chrome":
        options = Options()
        options.add_argument("--disable notification")
        driver = webdriver.Chrome(options)
    elif browser == "edge":
        driver = webdriver.Edge()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get(ReadConfig.getAppUrl())
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver


#Step2: use to get browser name from command - line & pass value browser to openbrowser fixture
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#step1: set default value of browser
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="provide browser name - chrome, firefox, edge, etc")


###-----Html Report----####
#1: It is hook for adding environment info into Report (customize info in report)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Swag Labs'
    metadata['Module Name'] = 'Login'
    metadata['Tester Name'] = 'Sanket'

