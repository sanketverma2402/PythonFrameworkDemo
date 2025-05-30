import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getAppUrl():
        urlValue=config.get("login credentials","URL")
        return urlValue

    @staticmethod
    def getAppUsername():
        UNValue = config.get("login credentials", "username")
        return UNValue

    @staticmethod
    def getAppPassword():
        PWDValue = config.get("login credentials", "password")
        return PWDValue

