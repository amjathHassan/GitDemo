import time
from selenium.webdriver.common.by import By
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup")
# Parent class BaseClass knows about fixture
class TestOne(BaseClass):

    def test_e2e(self):
        # no need to give fixture parameter here when utility using
        # initialisation
        # create a fixture and create a driver to this test -- conftest.py
        # user @pytest.mark.usefixtures("setup")
        # create objects in another class and actions performed in test methods

        log = self.getLogger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("getting all the card titles")
        cards = checkoutpage.getCardTilte()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if card.text == "Blackberry":
                checkoutpage.getCardFooter(i).click()
        time.sleep(2)
        checkoutpage.getConfirmButtton()
        confirmpage = checkoutpage.getCheckOutItem()
        time.sleep(2)
        # self.verifySearchBoxPresence("country")  # try to place wait methods in BaseClass as methods
        log.info("Entering country name as ind")
        confirmpage.sendCountyName("Ind")
        # time.sleep(5)
        self.verifyLinkPresence("India")
        confirmpage.clickCountyName()
        confirmpage.checkTermsAndCondition()
        confirmpage.clickConfirmButton()
        textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
        log.info(f"Text received from application is {textMatch}")

        assert ("Success! Thank you!" in textMatch)


# =====================================================================================================================

#
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import pytest
#
# from pageObject.CheckoutPage import CheckOutPage
# from pageObject.HomePage import HomePage
# from utilities.BaseClass import BaseClass
#
#
# # @pytest.mark.usefixtures("setup")
# # Parent class BaseClass knows about fixture
# class TestOne(BaseClass):
#
#     def test_e2e(self):  # no need to give fixture parameter here when utility using
#
#         # initialisation
#         # create a fixture and create a driver to this test -- conftest.py
#         # user @pytest.mark.usefixtures("setup")
#
#         # self.driver.find_element(By.CSS_SELECTOR, "a[href='/angularpractice/shop']").click()
#         # create objects in another class and actions performed in test methods
#         homepage = HomePage(self.driver)
#         checkoutpage = homepage.shopItems()
#
#         cards = checkoutpage.getCardTilte()
#         i = -1
#         for card in cards:
#             i = i + 1
#             cardText = card.text
#             print(cardText)
#             if card.text == "Blackberry":
#
#                 # self.driver.find_element(By.CSS_SELECTOR, ".card-footer button")[i].click()
#                 # button = CheckOutPage(self.driver)
#                 checkoutpage.getCardFooter(i).click()
#         time.sleep(2)
#
#         # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
#         # confirmButton = CheckOutPage(self.driver)
#         # confirmButton.getConfirmButtton().click()
#         checkoutpage.getConfirmButtton()
#         confirmpage = checkoutpage.getCheckOutItem()
#         time.sleep(2)
#
#         # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
#         # checkOutItem = CheckOutPage(self.driver)
#         # checkOutItem.getCheckOutItem().click()
#
#         # confirmpage = checkoutpage.checkOutItems()
#         # log.info("Entering country name as ind")
#         wait = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.ID, "country"))
#         )
#         # self.driver.find_element(By.ID, "country").send_keys("ind")
#         confirmpage.sendCountyName("Ind")
#         # time.sleep(5)
#         # self.verifyLinkPresence("India")
#         element = WebDriverWait(self.driver, 10).until(
#             EC.visibility_of_element_located((By.LINK_TEXT, "India"))
#         )
#         # self.driver.find_element(By.LINK_TEXT, "India").click()
#         confirmpage.clickCountyName()
#         # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
#         confirmpage.checkTermsAndCondition()
#         # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
#         confirmpage.clickConfirmButton()
#         textMatch = self.driver.find_element(By.CSS_SELECTOR, "[class*='alert-success']").text
#         # log.info("Text received from application is " + textMatch)
#
#         assert ("Success! Thank you!" in textMatch)

