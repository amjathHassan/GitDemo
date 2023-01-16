from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage():

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    confirmButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutItem = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getCardTilte(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self, i):
        return self.driver.find_elements(*CheckOutPage.cardFooter)[i]

    def getConfirmButtton(self):
        return self.driver.find_element(*CheckOutPage.confirmButton).click()

    def getCheckOutItem(self):
        self.driver.find_element(*CheckOutPage.checkOutItem).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
