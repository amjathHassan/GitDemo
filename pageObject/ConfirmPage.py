from selenium.webdriver.common.by import By


class ConfirmPage():

    def __init__(self, driver):
        self.driver = driver

    countryNameInput = (By.ID, "country")
    countryLink = (By.LINK_TEXT, "India")
    t_and_c_checkout = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmButton = (By.CSS_SELECTOR, "[type='submit']")

    def sendCountyName(self, name):
        self.driver.find_element(*ConfirmPage.countryNameInput).send_keys(name)

    def clickCountyName(self):
        self.driver.find_element(*ConfirmPage.countryLink).click()

    def checkTermsAndCondition(self):
        self.driver.find_element(*ConfirmPage.t_and_c_checkout).click()

    def clickConfirmButton(self):
        self.driver.find_element(*ConfirmPage.confirmButton).click()
