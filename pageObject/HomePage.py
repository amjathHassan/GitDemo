from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.CheckoutPage import CheckOutPage


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    submit = (By.XPATH, "//input[@type='submit']")
    gender = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    message = (By.CLASS_NAME, "alert")

    shop = (By.CSS_SELECTOR, "a[href='/angularpractice/shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def checkBox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getMessage(self):
        return self.driver.find_element(*HomePage.message).text

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def shopItems(self):

        # self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

