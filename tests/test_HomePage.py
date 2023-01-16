import time

import pytest

from TestData.HomePageData import HomePageData
from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info(f"First name is {getData['firstname']}")
        homepage.getName().send_keys(getData["firstname"])
        log.info(f"Email is {getData['email']}")
        homepage.getEmail().send_keys(getData["email"])
        # homepage.getPassword().send_keys(getData["password"])
        homepage.checkBox().click()
        self.selectOptionByText(homepage.getGender(), getData["gender"])
        homepage.submitForm().click()
        message = homepage.getMessage()

        assert "Success" in message

        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
        # time.sleep(3)
        # driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("changed the text")

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getData("Testcase4"))
    def getData(self, request):
        return request.param
